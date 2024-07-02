from datetime import datetime
from util import *
from Blockchain import Blockchain
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import json
import base64

class Vote :
    ''' handles creation, encryption, verification and storing votes.'''
    def __init__(self,name,voted_for,private_key,authority_pub_key) -> None:
        self.voter_id = hash_of(name + private_key)
        self.timestamp = f'{datetime.now()}'
        self.encrypted_vote = self.encrypt_vote(voted_for,authority_pub_key)
        self.signature = self.sign(private_key)

    
    def encrypt_vote(self,vote_info,authority_public_key): 
        ''' encryption of vote with public key of authority. encryption include political party and timestamp '''
        
        encrypted_vote = PKCS1_OAEP.new(authority_public_key).encrypt(vote_info.encode())
        encrypted_vote_string = base64.b64encode(encrypted_vote).decode('utf-8')

        return encrypted_vote_string
    
    def decrypt_vote(self,authority_private_key):
        # decrypt vote in counting phase by authority.
        
        pass

    def sign(self,private_key):
        # digital signature by registered voter.
        try:
            data_to_be_signed = self.voter_id+self.encrypted_vote + self.timestamp
            hash_object = SHA256.new(data_to_be_signed.encode())
            private_key_pem = base64.b64decode(private_key)
            signature = pkcs1_15.new(RSA.import_key(private_key_pem)).sign(hash_object)    
            return signature
        except :
            print('invalid private key\n')
            
    def print(self) :
        ''' to print the vote in dict fomat'''
        obj_to_dict = {
                "Voter_id" : self.voter_id,
                "timestamp" : self.timestamp,
                "encrypted_vote" : self.encrypted_vote,
                "signature" : base64.b64encode(self.signature).decode('utf-8')
        }
        return obj_to_dict



class Voter :
    ''' eligible voters'''
    def __init__(self,voter_name) -> None:
        self.voter_name = voter_name
        self.private_key,self.public_key = create_key_pairs()
        self.private_key,self.public_key = export_keys(self.private_key,self.public_key)
        self.hashed_id = hash_of(self.voter_name + self.private_key)


    
class Election :
   
    def __init__(self) -> None:
        self.Blockchain = Blockchain()
        self.voters_name = []
        self.voter_verification_details = []        # list of tuple having hash of voter_id+private_key of eligible voters and corresponding public_key.
        self.authority_private_Key, self.authority_public_Key = create_key_pairs() 
        self.contestants = ['kunj','xyz']

    def register_to_vote(self,voter_name):
        # registration of voter and updating voter_details.
            voter = Voter(voter_name)
            self.voters_name.append(voter_name)
            self.voter_verification_details.append((voter.hashed_id,voter.public_key))
            return voter.private_key,voter.public_key
        

    def register_contestant(self, contestant_name):
        # register to contest election.
        if contestant_name not in self.contestants :
            self.contestants.append(contestant_name)
            print('successfully registered to contest.','\n')
        else :
            print('already registered\n')

    def cast_vote(self,voter_name,voter_private_key,voted_for):
        # it will create instance of Vote class. The vote then, will be encrypt,signed and then added to mempool after verification.
            vote = Vote(voter_name.lower(), voted_for,voter_private_key,self.authority_public_Key)
            if self.verify_vote(vote) :
                    self.Blockchain.verified_pending_votes.append(vote)
                    print('\nvote casted successfully.')
            return 
    
    def verify_vote(self,vote):
        ''' verification of vote. to prevent multiple voting by same Id, verify digital signature.'''
        all_voted_ids=[ vote.voter_id for vote in  self.Blockchain.verified_pending_votes]
        if len(self.Blockchain.chain) > 1:
            for block in self.Blockchain.chain :
                for vote in block.votes :
                 all_voted_ids.append(vote.voter_id)
                 print(all_voted_ids)
        if vote.voter_id not in all_voted_ids :
            # verifying signature  
            pub_key = None
            for a,b in self.voter_verification_details :
                    if a == vote.voter_id :
                        pub_key = b
            if pub_key is None :
                print( "Invalid Voter name or Private key")
            else  :
                hash_object = SHA256.new((vote.voter_id + vote.encrypted_vote + vote.timestamp).encode())
                try :
                    pkcs1_15.new(RSA.import_key(base64.b64decode(pub_key))).verify(hash_object,vote.signature)
                    return 1
                except(ValueError) :
                    print("Signature is invalid. Vote is discarded.",'\n')
                    return 0
        else :
            print("Already Voted with this voter id.",'\n')
            return 0

    def counting_votes ( self ):
        # counts votes by decrypting all votes by traversing chain.
        pass

    def declare_result ( self ) :
        # declare results of election.
        pass

# election=Election()
# pvt_key,pub_key=election.register_to_vote('kunj')
# election.cast_vote('kunj',pvt_key,'kunj')
# print(type(pvt_key.decode()))
# print(pvt_key)