# SNAKE WATER OR GUN GAME
import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'S':
        if you =='W':
            return False
        elif you=='G':
            return True
    elif comp == 'W':
        if you =='G':
            return False
    elif you=='S':
        return True        
    elif comp == 'G':
        if you =='W':
            return False
    elif you=='S':
        return True
    elif comp =='G':
        if you=='S':
            return False
        elif you =='W':
            return True

print("Comp turn:Snake(S) water(W) or gum(G)?")
randNo = random.randint(1,3)
if randNo ==1:
    comp ='S'
elif randNo == 2 :
    comp ='W'
elif randNo == 3:
    comp ='G'

you = input("Player turn:Snake(S) water(W) or gum(G)?")
a = gameWin(comp,you)
print(f"Comp chose {comp}")
print(f"You chose {you}")

gameWin(comp, you)
if a == None:
    print("The game is a tie")
elif a:
    print("You Win")
else:
    print("You Lose")