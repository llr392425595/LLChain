import hashlib
from time import time

from flask import json


class Block:
    def __init__(self, block_header, block_body):
        self.block_header = block_header
        self.block_body = block_body

    def hash(self):
        block_string = json.dumps(self, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class BlockHeader:
    def __init__(self, index, proof, previous_hash):
        self.timestamp = time()
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash


class BlockBody:
    def __init__(self, transactions=None):
        if transactions is None:
            transactions = []
        self.index = transactions
