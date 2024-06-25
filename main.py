''' main script to simulate election '''

from election import *


election = Election()

while(True) :
    i = input('enter a prompt - ')
   
    if (  i == 'register' ) :
        name = input('enter your name - ')
        pvt_key = election.register_to_vote(name)
        print(f' your private key is - {pvt_key}','\n','store it somewhere privately and use it to vote. Do not share with anyone.','\n')
    
    elif ( i == 'contest' ) :
        name = input('enter your name - ')
        election.register_contestant(name)

    elif ( i == 'vote' ) :
        print('list of contestants - ','\n')
        print('\n')
        for i in election.contestants :
            print(election.contestants.index(i),i)
        name = input('enter your name - ')
        VoteData = input('enter name of contestant you want to vote')
        
