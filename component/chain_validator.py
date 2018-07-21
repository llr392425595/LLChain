from component.proof_generator import ProofGenerator
from model.block import hash_block


class ChainValidator:

    @staticmethod
    def valid_chain(block_chain):
        current_index = 1
        pre_block = block_chain[current_index - 1]

        while current_index < len(block_chain):
            current_block = block_chain[current_index]
            if current_block.previous_hash != hash_block(pre_block):
                return False
            if not ProofGenerator.valid_proof(pre_block.proof, current_block.proof):
                return False

            pre_block = current_block
            current_index += 1
        return True
