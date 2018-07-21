import hashlib
from time import time

from flask import json


class Block:
    def __init__(self, index=None, timestamp=None, proof=None, previous_hash=None, transactions=None):
        self.index = index
        self.timestamp = timestamp or time()
        self.proof = proof
        self.previous_hash = previous_hash
        self.transactions = transactions


def hash_block(block_dict):
    block_string = json.dumps(block_dict, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()
