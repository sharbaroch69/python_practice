# import random

# def game():
#     print("You are playing game...")
#     score = random.randint(1, 100)
#     print("Your score is:", score)
# # fetch the hiscore
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         # if(score>hiscore):
#             # print("You have just broken the high score")
#         else:
#             hiscore = 0
#             # print("You could not beat the high score")
#     print(f"your score: {score}")
#         # write hiscore in file
#         with open("hiscore.txt", "w") as f:
#             f.write(str(hiscore))

#     return score

# f.close()



import random

def game():
    print("You are playing game...")
    score = random.randint(1, 100)
    # fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"your score: {score}")
        # write hiscore in file
    with open("hiscore.txt", "w") as f:
            f.write(str(hiscore))

    return score

game()


# ...existing code...
# import random
# import os

# def game():
#     print("You are playing game...")
#     score = random.randint(1, 100)

#     path = "hiscore.txt"
#     hiscore = 0
#     # read existing hiscore if file exists and contains a valid integer
#     if os.path.exists(path):
#         try:
#             with open(path, "r", encoding="utf-8") as f:
#                 content = f.read().strip()
#                 if content:
#                     hiscore = int(content)
#         except (ValueError, OSError):
#             hiscore = 0

#     print(f"your score: {score}")
#     # update file only if player beats the hiscore
#     if score > hiscore:
#         print("You have just broken the high score!")
#         with open(path, "w", encoding="utf-8") as f:
#             f.write(str(score))
#     else:
#         print("You did not beat the high score.")

#     return score
# # ...existing code...