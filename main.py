''' main script to simulate election '''

from election import *
from Block import *

election = Election()

prompts()
while(True) :

    i = input('enter a prompt - ')
   
    if (  i == 'register' ) :
        name = input('enter your name - ')
        if name not in election.voters_name:
            pvt_key,pub_key = election.register_to_vote(name)
            print('\n',f' your private key is -','\n', pvt_key,'\n','store it somewhere privately and use it to vote. Do not share with anyone.','\n')
            print('your public key is given below - ', '\n',pub_key,'\n' )
        else :
            print('already registered.\n')

    elif ( i == 'vote' ) :
        print('list of contestants - ','\n')
        for i in election.contestants :
            print(election.contestants.index(i),i)
        print('\n')
        name = input('enter your name - ')
        Voted_for = input('enter name of contestant you want to vote - ')
        if Voted_for not in election.contestants :
            print('entered wrong contestant name. Please enter valid name from the list given above.\n')
        else :
            private_key = input(' enter your private_key - ')
            election.cast_vote(name,private_key,Voted_for)
            election.Blockchain.create_block()
            election.Blockchain.validate_chain()
            
    elif (i == 'print chain') :
        print('\n')
        election.Blockchain.print_chain()
        print('\n')

    elif ( i == 'print latest block') :
        print('\n')
        election.Blockchain.print_latest_block()

    elif ( i == 'validate' ):
        election.Blockchain.validate_chain()

    elif ( i == 'prompts' ):
        prompts()

    elif(i== 'exit'):
        if election.Blockchain.verified_pending_votes :
            last_prev_block =election.Blockchain.get_latest_block()
            prev_hash= last_prev_block.compute_hash()
            index = last_prev_block.index+1
            last_block = Block(index,prev_hash,election.Blockchain.verified_pending_votes)
            election.Blockchain.proof_of_work(last_block)
            election.Blockchain.add_block(last_block)
            election.Blockchain.verified_pending_votes=[]
        res = election.counting_votes()
        print('election is over. Here is result - \n')
        election.declare_result(res)
        exit()
    else :
        print('Wrong prompt. Please enter a valid prompt. enter "\n')
        prompts()