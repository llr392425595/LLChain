from flask import Flask, request, jsonify

from component.my_json_encoder import MyJSONEncoder
from service.chain_service import ChainService
from component.proof_generator import ProofGenerator

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

chain_service = ChainService()
proof_generator = ProofGenerator()


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to LLChain."


@app.route('/mine', methods=['POST'])
def mine():
    last_proof = chain_service.last_block.block_header.proof
    current_proof = proof_generator.proof_of_work(last_proof)
    node_address = request.get_json()["node_address"]
    # 提供奖励，sender为0
    chain_service.new_transaction(
        sender="0",
        recipient=node_address,
        amount=1,
    )

    block = chain_service.new_block(current_proof, None)

    response = {
        'index': block.block_header.index,
        'transactions': block.block_body.transactions,
        'proof': block.block_header.proof,
        'previous_hash': block.block_header.previous_hash
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = chain_service.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': chain_service.block_chain,
        'length': len(chain_service.block_chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
