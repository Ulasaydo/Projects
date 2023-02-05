import random 

def play():

    user = input("'R' for rock,'P' for paper,'S' for scissors :\n").lower()
    computer = random.choice(['r','p','s'])

    #r>s,s>p,p>r
    if computer == user:
        print("Tie")

    if is_win(user, computer):
        return print('USER WON')
    
    return print("Computer won")

def is_win(player,opponent):       
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r')\
        or (player == 's' and opponent == 'p'):
            return True
        
play()    
        
        