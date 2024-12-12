import hashlib
import time

class Block:
    def __init__(self, previous_hash, data):
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0
        self.hash = None

    def compute_hash(self):
        block_content = f"{self.previous_hash}{self.data}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()

def proof_of_work(block, difficulty):
    target_prefix = "0" * difficulty
    start_time = time.time()

    while True:
        block.hash = block.compute_hash()
        if block.hash.startswith(target_prefix):
            break
        block.nonce += 1

    elapsed_time = time.time() - start_time
    print(f"Proof of Work found: {block.hash} (nonce: {block.nonce}) in {elapsed_time:.2f} seconds")
    return block

if __name__ == "__main__":
    previous_hash = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    data = "Example Block Data"
    difficulty = int(input("Enter the difficulty "))

    block = Block(previous_hash, data)
    print("Mining block...")
    mined_block = proof_of_work(block, difficulty)

    print("\nBlock mined successfully!")
    print(f"Previous Hash: {mined_block.previous_hash}")
    print(f"Data: {mined_block.data}")
    print(f"Nonce: {mined_block.nonce}")
    print(f"Hash: {mined_block.hash}")
