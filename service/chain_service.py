from urllib.parse import urlparse

import requests

from component.chain_validator import ChainValidator
from model.block import Block, hash_block


class ChainService(object):
    def __init__(self):
        self.block_chain = []
        self.current_transactions = []
        self.nodes = set()
        self.__create_genesis_block()

    @property
    def last_block(self):
        return self.block_chain[-1]

    def new_block(self, proof, previous_hash=None):
        block = Block(
            index=len(self.block_chain) + 1,
            proof=proof,
            previous_hash=previous_hash or hash_block(self.last_block),
            transactions=self.current_transactions
        )
        self.block_chain.append(block)
        self.current_transactions = []
        return block

    def new_transaction(self, sender=None, recipient=None, amount=None):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block.index + 1

    def __create_genesis_block(self):
        self.new_block(previous_hash=1, proof=100)

    def register_node(self, address):
        parsed_url = urlparse(address)
        print(parsed_url)
        self.nodes.add(parsed_url.netloc)

    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None

        max_length = len(self.block_chain)

        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain_data = response.json()['chain']
                print(chain_data[0])
                chain = create_chain_from(chain_data)
                if length > max_length and ChainValidator.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        if new_chain:
            self.block_chain = new_chain
            return True

        return False


def create_chain_from(chain_data):
    result = []
    for item in chain_data:
        result.append(Block(**item))
    print(result)
    return result
