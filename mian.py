from uuid import uuid4

from flask import Flask, jsonify, request

from block_chain import BlockChain

app = Flask(__name__)

node_address_identifier = str(uuid4()).replace("-", "")

block_chain = BlockChain()


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to LLChain."


@app.route('/mine', methods=['GET'])
def mine():
    last_block = block_chain.last_block
    last_proof = last_block['proof']
    proof = block_chain.proof_of_work(last_proof)

    # 提供奖励，sender为0
    block_chain.new_transaction(
        sender="0",
        recipient=node_address_identifier,
        amount=1,
    )

    block = block_chain.new_block(proof, None)

    response = {
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = block_chain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': block_chain.chain,
        'length': len(block_chain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)
