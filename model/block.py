import hashlib
from time import time


class Block:
    def __init__(self, block_header, block_body):
        self.block_header = block_header
        self.block_body = block_body

    def hash_block(self):
        return hashlib.sha256(self.str_block().encode()).hexdigest()

    def str_block(self):
        return self.block_header.str_block_header() + self.block_body.str_block_body()


class BlockHeader:
    def __init__(self, index, proof, previous_hash):
        self.timestamp = time()
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash

    def str_block_header(self):
        return str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.proof)


class BlockBody:
    def __init__(self, transactions=None):
        self.transactions = transactions

    def str_block_body(self):
        return str(self.transactions)
