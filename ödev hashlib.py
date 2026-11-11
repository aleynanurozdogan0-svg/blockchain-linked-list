import hashlib

class Block:
    def __init__(self, data, previous_hash=""):
        self.data = data
        self.previous_hash = previous_hash
        self.previous = None
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_content.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        genesis_block = Block("First block", previous_hash="0")
        genesis_block.previous = None
        
        self.head = genesis_block 
        self.tail = genesis_block 

    def add_block(self, data):
        new_block = Block(data, previous_hash=self.tail.hash)
        new_block.previous = self.tail 
        
        self.tail = new_block

    def display_chain(self):
        current = self.tail
        while current is not None:
            print(f"Block → Data: {current.data}, Hash: {current.hash[:7]}..., Previous Hash: {current.previous_hash[:7] if current.previous_hash != '0' else '0'}...")
            current = current.previous

    def verify_chain(self):
        current = self.tail
        
        while current.previous is not None:
            if current.previous_hash != current.previous.hash:
                print("Blockchain is invalid.")
                return False
            current = current.previous
            
        print("Blockchain is valid.")
        return True

if __name__ == "__main__":
    my_blockchain = Blockchain()
    
    my_blockchain.add_block("Second block")
    my_blockchain.add_block("Third block")
    
    my_blockchain.display_chain()
    
    my_blockchain.verify_chain()