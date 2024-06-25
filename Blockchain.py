from Block import Block
from election import Vote
from election import Voter

class Blockchain :
    ''' 
    it will be list of block linked with HASH value of previous block.
    
    '''
    def __init__(self,difficulty=4) -> None:
        self.chain = [self.create_genesis_block()]
        self.verified_pending_votes=[]           #mempool
        self.difficulty = difficulty
        self.vote_per_block =8
        self.voted_record = []             # records of voter who has voted already.
    
    def create_genesis_block(self):
        #creating genesis block - the first block of the blockchain.
        pass

    def add_block(self,Block):
        #verifying and then adding  blocks to the blockchain. it will use verify() method of Block class.
        pass

    def get_last_block(self):
        # accessing latest block of the chain.
        pass
      
    def create_block(self):
        # to create a block and mine()
        pass
    
    def cast_vote(self,voter_id,):
        # it will create instance of Vote class. The vote then, will be encrypt,signed and then added to mempool after verification.
        
        pass

    def print(self) :
        # print the whole list of blocks in JSON format.
        pass

if __name__ == '__main__' :
    vote_chain=Blockchain('12')