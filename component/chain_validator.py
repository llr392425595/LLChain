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
            if current_block['previous_hash'] != pre_block.hash():
                return False

            # Check that the Proof of Work is correct
            if not ProofGenerator.valid_proof(pre_block.block_header.proof, current_block.block_header.proof):
                return False

            pre_block = current_block
            current_index += 1

        return True
