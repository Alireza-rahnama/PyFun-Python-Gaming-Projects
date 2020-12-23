from random import randint

#Generate the computer's move using the randint function 
#in the random module.
#Assume 0 = rock, 1 = paper, and 2 = scissors.
computerMove = randint(0,2)
userMove= input('please enter r for rock, p for paper, and s for scissors or\
 anything else to exit: ')
#Prompt the user to enter r for rock, p for paper or s for scissors.
#Save the user's input in a variable called userMove.
#Validate the user's move.

while (userMove == 'r' or userMove == 'p' or userMove == 's'):
    if computerMove == 0: #Computer played rock.
        if userMove== 'p':
            print(' computer is rock, user is paper, user wins!')
        
        elif userMove== 's':
            print(' computer is rock, user is scissors, computer wins!')
            
        
        


    elif computerMove == 1: #Computer played paper.
        if userMove== 'r':
             print(' computer is paper, user is rock, computer wins!')
             
        elif userMove== 's':
             print(' computer is paper, user is scissors, user wins!')
             

        #Write the if-elif statements to determine outcome of the game.


    elif computerMove == 2: #Computer played scissors.
        #Write the if-elif statements to determine outcome of the game.
        if userMove== 'r':
             print(' computer is scissors, user is rock, user wins!')
             
        elif userMove== 'p':
             print(' computer is scissors, user is paper, computer wins!')
             
    print()
    userMove= input('please enter r for rock, p for paper, and s for scissors or\ anything else to exit: ')
