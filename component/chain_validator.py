import hashlib

from flask import json

from component.proof_generator import ProofGenerator


class ChainValidator:

    @staticmethod
    def valid_chain(block_chain):
        current_index = 1
        pre_block = block_chain[current_index - 1]

        while current_index < len(block_chain):
            current_block = block_chain[current_index]
            print(f'{pre_block}')
            print(f'{current_block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            print(current_block["block_header"]["previous_hash"])
            if current_block["block_header"]["previous_hash"] != hash_block(pre_block):
                return False

            # Check that the Proof of Work is correct
            if not ProofGenerator.valid_proof(pre_block["block_header"]["proof"], current_block["block_header"]["proof"]):
                return False

            pre_block = current_block
            current_index += 1

        return True


def hash_block(pre_block):
    block_string = json.dumps(pre_block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()
