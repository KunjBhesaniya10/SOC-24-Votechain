from datetime import datetime

class Block :
    '''Block will have Votes, nonce, previous HASH value,height and timestamp. '''

    def __init__(self,index,prev_hash,votes,nonce=1) -> None:
        self.height = index
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.votes= votes
        self.timestamp = f'{datetime.now()}'

    def compute_hash(self):
        ''' calculating hash of the block by SHA-256 algorithm. 
        '''
    def verify(self) :
        '''verify the block's hash value.
        '''
    


