from uuid import uuid4

from flask import Flask, jsonify

from block_chain import BlockChain

app = Flask(__name__)

node_address_identifier = str(uuid4()).replace("-", "")

block_chain = BlockChain()


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to LLChain."


@app.route('/mine', methods=['GET'])
def mine():
    return "We will mine a new block."


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We will add a new transaction."


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': block_chain.chain,
        'length': len(block_chain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)