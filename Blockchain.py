from Block import Block
import json

class Blockchain  :
    ''' 
    it will be list of block linked with HASH value of previous block.
    
    '''
    def __init__(self,difficulty=3) -> None:
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]
        self.verified_pending_votes=[]           #mempool

        self.vote_per_block = 2
    
    def create_genesis_block(self):
        #creating genesis block - the first block of the blockchain.
        index = 0
        prev_hash = '0'*64
        nonce =1
        Votes= None
        genesis_block = Block(index,prev_hash,Votes,nonce)
        hash_of_block = genesis_block.compute_hash()
        while(hash_of_block[:self.difficulty]!='0'*self.difficulty):
            genesis_block.nonce+=1
            hash_of_block = genesis_block.compute_hash()
        return genesis_block

    def add_block(self,Block):
        # adding  blocks to the blockchain.
        self.chain.append(Block)

    def get_latest_block(self):
        # accessing latest block of the chain.
        latest_block = self.chain[-1]
        return latest_block
      
    def create_block(self):    
        # to create a block
        if len(self.verified_pending_votes) >= self.vote_per_block :
            latest_block = self.get_latest_block()
            prev_hash = latest_block.compute_hash()
            new_block = Block(latest_block.index +1,prev_hash, self.verified_pending_votes[:self.vote_per_block])    
            self.proof_of_work(new_block)
            self.add_block(new_block)    
            self.verified_pending_votes = self.verified_pending_votes[self.vote_per_block:]

    def proof_of_work(self,Block):
        # generate proof of work for the block and updates the nonce value.
        new_block_hash = Block.compute_hash()
        while new_block_hash[:self.difficulty] != '0'*self.difficulty :
            Block.nonce +=1
            new_block_hash = Block.compute_hash()
        
    def validate_chain(self,print_default=False):
        # This function validates the whole blockchain by checking the hashes of blocks.
        # 'default' parameter is used to control when to show print statement on terminal and when to not.

        block_index = 1
        prev_block_index = 0
        while block_index < len(self.chain) :
            if self.chain[block_index].prev_hash == self.chain[prev_block_index].compute_hash() :
                pass
            else :
                print(' xxxxxxxxxxxxxxx BlockChain is invalid xxxxxxxxxxxxxxxx')
                print( f'prev_hash of block index {block_index} does not match hash of index{prev_block_index}','\n')
                return
            block_index+=1
            prev_block_index+=1
        if print_default :
            print('\n',' ******************** Blockchain is valid **********************','\n')
             
    def print_latest_block(self) :
        # print the latest  block in JSON format.
        if len(self.chain) >1 :
            data=self.get_latest_block().print()
            print(json.dumps(data,indent=4))
        else :
            data = [{
            "index" : f'{0} Genesis Block',
            "previous_hash" : '0'*64,
            "nonce": 1,
            "votes" : '-------------',
            "timestamp" : self.chain[0].timestamp
        }]
            print(data)
            

    def print_chain(self) :
        data = [{
            "index" : f'{0} Genesis Block',
            "previous_hash" : '0'*64,
            "nonce": 1,
            "votes" : '-------------',
            "timestamp" : self.chain[0].timestamp
        }]
        for block in self.chain[1:] :
           data.append(block.print())
        data = json.dumps(data,indent=4)
        print(data)


