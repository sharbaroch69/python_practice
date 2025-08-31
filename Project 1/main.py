import random
'''
1 for snake
-1 for water
0 for gun
'''
mydict = {
        "s": 1,
        "w": -1,
        "g": 0
    }
names = {"s": "snake", "w": "water", "g": "gun"}
def gameWin(comp, you):
    if comp == you:
        return "It's draw"
    if comp == 1 and you == -1:
        return "You lose"
    if comp == -1 and you == 0:
        return "You lose"
    if comp == 0 and you == 1:
        return "You lose"
    if comp == -1 and you == 1:
        return "You win"
    if comp == 1 and you == 0:
        return "You win"
    if comp == 0 and you == -1:
        return "You win"
    

comp_key = random.choice(["s", "w", "g"])
comp = mydict[comp_key]
you_key = input("Your turn  (s/w/g): ")
if you_key not in mydict:
    print("Invalid choice")
    exit()
you = mydict[you_key]

print(f"Computer chose {names[comp_key]}")
print(f"You chose {names[you_key]}")
print(gameWin(comp, you))


