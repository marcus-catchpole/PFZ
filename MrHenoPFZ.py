# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 07:29:23 2022

PFZ Game

Three random integer digits are created.  The user guesses.  
Each digit is marked P, F, or Z indicating:
    P: perfect (right digit, right location)
    F: digit is in the answer, but in the wrong location
    Z: the digit is not in the answer anywhere

Game created by Mr. Heno

@author: Marcus
"""
from random import randint
from time import sleep
play = True
while play:
    # initilize place to keep track of the answer
    answer = []
    # make a counter for the number of attempts made
    turn = 0
    
    # fill the answer with random integers 0..9 
    for i in range(3):
        answer.append(randint(0,9))
    
    #print the answer (for debugging only, othewise comment this line)
    #print(answer)
    
    # before we check, we'll keep track of the answer 
    pfz = ['z','z','z']
    # Keep going until you get "ppp"
    while not pfz == ['p','p','p']:
        guess = input("Input your guess:\n")
         
        for i in range(len(answer)):
            if answer[i]==int(guess[i]):
                pfz[i]='p'
            elif int(guess[i]) in answer:
                pfz[i]='f'
            else: 
                pfz[i] ='z'
        
        #do some formatting to get pfz on one line
        pfz_string = ''
        for char in pfz:
            pfz_string += char
        turn += 1
        # Tell the user how the guess was
        print(pfz_string, "turn:", turn)
    # If the guess got a 'ppp'
    print("Woo! You did it in", turn, "turns!")
    
    # Dramatically wait to print the next line
    sleep(2)
    
    # Ask if user wants to play again
    play_again = input("Play Again? (y/n)\n")
    if play_again == 'n' or play_again == 'N':
        play=False