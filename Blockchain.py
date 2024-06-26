from Block import Block


class Blockchain  :
    ''' 
    it will be list of block linked with HASH value of previous block.
    
    '''
    def __init__(self,difficulty=4) -> None:
        self.chain = [self.create_genesis_block()]
        self.verified_pending_votes=[]           #mempool
        self.difficulty = difficulty
        self.vote_per_block = 8
    
    def create_genesis_block(self):
        #creating genesis block - the first block of the blockchain.
        pass

    def add_block(self,Block):
        # verifying and then adding  blocks to the blockchain. it will use verify() method of Block class.
        pass

    def get_latest_block(self):
        # accessing latest block of the chain.
        pass
      
    def create_block(self):    
        # to create a block
        pass

    def proof_of_work(self,Block):
        # generate proof of work for the block and updates the nonce value.
        pass

    def validate_chain(self, chain):
        # This function validates the whole blockchain by checking the hashes of blocks.
        pass
    
    
        
    
    def print_latest_block(self) :
        # print the latest  block in JSON format.
        pass

