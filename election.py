from datetime import datetime
from util import *
from Blockchain import Blockchain

class Vote :
    ''' handles creation, encryption, verification and storing votes.'''
    def __init__(self,name,voteData,private_key) -> None:
        self.voter_id = hash_of(name+private_key)
        self.timestamp = f'{datetime.now()}'
        self.encrypted_vote = self.encrypt_vote(voteData)
        self.signature = self.sign(private_key)

    
    def encrypt_vote(self,authority_public_key): 
        ''' encryption of vote with public key of authority. encryption include political party and timestamp '''
        pass
    
    def decrypt_vote(self,authority_private_key):
        # decrypt vote in counting phase by authority.
        pass

    def sign(self,private_key):
        # digital signature by registered voter.
        pass

    def verify_vote(vote):
        ''' verification of vote. to prevent multiple voting by same Id, verify digital signature.
        '''
        pass


class Voter :
    ''' eligible voters'''
    def __init__(self,voter_name) -> None:
        self.voter_name = voter_name
        # self.private_key,self.public_key = create_key_pairs()
        # self.hashed_id = hash_of(self.voter_name + self.private_key)


    
class Election :
   
    def __init__(self) -> None:
        self.Blockchain = Blockchain()
        self.voter_verification_details = []        # list of tuple having hash of voter_id+private_key of eligible voters and corresponding public_key.
        # self.authority_private_Key, self.authority_public_Key = create_key_pairs() 
        self.contestants = ['kunj','xyz']

    def register_to_vote(self,voter_name):
        # registration of voter and updating voter_details.
        voter = Voter(voter_name)
        return 'ttq 4tt4tqq4[90cuntq[ievjt0q43[q]]]'
    
    def register_contestant(self, contestant_name):
        # register to contest election.
        self.contestants.append(contestant_name)
        print('successfully registered to contest.','\n')
        
    
    def counting_votes ( self ):
        # counts votes by decrypting all votes by traversing chain.
        pass

    def declare_result ( self ) :
        # declare results of election.
        pass
    

    