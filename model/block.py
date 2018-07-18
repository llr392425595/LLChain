import hashlib
from time import time

from flask import json


class Block:
    def __init__(self, block_header, block_body):
        self.block_header = block_header
        self.block_body = block_body

    def hash_block(self):
        block_string = json.dumps(self.serialize(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        # return hashlib.sha256(self.str_block().encode()).hexdigest()

    def str_block(self):
        return self.block_header.str_block_header() + self.block_body.str_block_body()

    def serialize(self):
        return {
            "block_header": self.block_header.serialize(),
            "block_body": self.block_body.serialize()
        }


class BlockHeader:
    def __init__(self, index, proof, previous_hash):
        self.index = index
        self.timestamp = time()
        self.proof = proof
        self.previous_hash = previous_hash

    def str_block_header(self):
        return str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.proof)

    def serialize(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'proof': self.proof,
            'previous_hash': self.previous_hash,
        }


class BlockBody:
    def __init__(self, transactions=None):
        self.transactions = transactions

    def str_block_body(self):
        return str(self.transactions)

    def serialize(self):
        return {
            'transactions': self.transactions
        }
