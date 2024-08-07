from datetime import datetime
from Crypto.Hash import SHA256

class Block :
    '''Block will have Votes, nonce, previous HASH value,index and timestamp. '''

    def __init__(self,index,prev_hash,votes,nonce=1) -> None:
        self.index = index
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.votes= votes
        self.timestamp = f'{datetime.now()}'

    def compute_hash(self):
        ''' calculating hash of the block by SHA-256 algorithm. 
        '''
        block_str = str(self.index)+str(self.prev_hash)+str(self.nonce)+str(self.votes)+str(self.timestamp) 
        hash_of_block = SHA256.new(block_str.encode()).hexdigest()
        return hash_of_block

    def print(self) :
            data = {
                "index": self.index,
                "previous_hash" : self.prev_hash,
                "nonce" : self.nonce,
                "Votes" : [vote.print() for vote in self.votes],
                "timestamp" : self.timestamp
            }
            return data
    