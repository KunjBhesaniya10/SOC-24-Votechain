''' main script to simulate election '''

from election import *


election = Election()

prompts()
while(True) :
    i = input('enter a prompt - ')
   
    if (  i == 'register' ) :
        name = input('enter your name - ')
        pvt_key,pub_key = election.register_to_vote(name)
        print('\n',f' your private key is -','\n', pvt_key,'\n','store it somewhere privately and use it to vote. Do not share with anyone.','\n')
        print('your public key is given below - ', '\n',pub_key,'\n' )
        
    elif ( i == 'contest' ) :
        name = input('enter your name - ')
        election.register_contestant(name)

    elif ( i == 'vote' ) :
        print('list of contestants - ','\n')
        for i in election.contestants :
            print(election.contestants.index(i),i)
        print('\n')
        name = input('enter your name - ')
        Voted_for = input('enter name of contestant you want to vote -')
        private_key = input(' enter your private_key - ')
        election.cast_vote(name,private_key,Voted_for)

        election.Blockchain.create_block()
            
    elif (i == 'print chain') :
        print('\n')
        election.Blockchain.print_chain()
        print('\n')

    elif ( i == 'print latest block') :
        print('\n')
        election.Blockchain.print_latest_block()

    elif ( i == 'prompts' ):
        prompts()