''' all utility functions defined here.'''
import hashlib
from Crypto.PublicKey import RSA
import base64

def hash_of(message) :
    # use sha-256 for hashing given message.
    
    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    return hashed_message


def create_key_pairs():
    # create private - public key pair.
    private_key = RSA.generate(2048)
    public_key = private_key.publickey()
    return private_key, public_key

def export_keys(pvt_key,pub_key):
    # serialize the keys into ASCII characters
    pvt_key = pvt_key.export_key()
    pvt_key = base64.b64encode(pvt_key).decode('utf-8')
    pub_key = base64.b64encode(pub_key.export_key()).decode('utf-8')
    return pvt_key,pub_key

def prompts () :
    print('------------------------------------------')
    print('All prompts are listed below - ')
    print('"prompts"','- to get list of prompts.')
    print('"register"','- to register for voting.')
    print( '"contest"','- to contest in election.')
    print('"vote"','- to vote in election.')
    print('"print chain"','- to print the whole chain.')
    print('"print latest block"', '- to print the latest block.')
    print('------------------------------------------')


