import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:\n'))
        if guess not in range(1,(x+1)):
            print(f'Sorry,guess is not in between 1 and {x}')
        elif guess < random_number:
            print('Sorry,guess is too low.Try again')
        elif guess> random_number:
            print('Sorry,guess is too high.Try again')
       
    print('Yay,congrats. You have guessed the number.')
    
def computer_guess(x):
    low = 1
    high = x
    feedback =''
    
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high(H),too low(L) or correct(c)??\n').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yay,the computer guessed your number {guess} correctly')
                          
    
computer_guess(10)
    
    
    

