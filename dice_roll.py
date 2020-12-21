from random import randint
from math import *
continues='y'
while continues.lower()=='y':
    NumberOfRolls= int(input('How many times should we roll the dice?  '))
    Your_guess= int(input('guess the percentage of\
    total even numbers generated?(0-100) '))/100
    print('5% Error is allowed in your guess!')
    NumberOfEvenValue=0
    NumberOfOddValue=0                  
    #simulate some number of rolls of two 6-sided dice
    for i in range(NumberOfRolls): 
        dice1= randint(1,6)
        dice2= randint(1,6)
        total= dice1+dice2            
        print("You rolled ", dice1, '+ ',dice2, '=',total)                 
        if total%2==0:
            NumberOfEvenValue+=1

        else:
            NumberOfOddValue+=1
    #compute the outputs        
    EvenPercentage=NumberOfEvenValue/NumberOfRolls*100
    OddPercentage=NumberOfOddValue/NumberOfRolls*100
    print('An even value was rolled',EvenPercentage ,'% of the time' )
    print('An odd value was rolled',OddPercentage ,'% of the time' )
    if abs(EvenPercentage-Your_guess)<= 0.05:
        print('you Won!')
    else:
        print('Looser!')
    continues=input('press Y to continue and anything else to exist: ')
    
