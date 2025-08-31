
# n = 0
# for i in range(1, 101):
#     n += i
#     print("sum:", n)

# word = input("enter name: ")
# for ch in word:
#     print(ch)

# for i in range(2, 51, 2):
#     print(i)


# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# password = "python123"
# guess = ""

# while guess != password:
#     guess = input("Enter your password: ")
    
# print("Access Granted!")

# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i 
#     i += 1
#     print("Factorial: ", fact) 


# secret = 78
# guess = 0
# while guess != secret:
#     guess = int(input("Guess the secret number: "))
#     if guess == secret:
#         print("Congratulations! You guessed the secret number!")
#         break
#     elif guess < secret:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")


for i in range(1, 21):
    print(i)
    pass

a = 0
while a < 21:
    print(a)
    a += 1
    pass

for i in range(2, 101, 2):
    print(i)
    pass

a = 2
while a < 101:
    print(a)
    a += 2
    pass


for i in range(5, 51, 5):
    print(i)
    pass


a = 5
while a < 51:
    print(a)
    a += 5
    pass

for i in range(1, 11): # square of numbers from 1 to 10
    print(i ** 2)

    pass
a = 0
while a < 11:
    print(a ** 2)
    a += 1
    pass

# calculate the sum of digits of number
num = int(input("Enter your number: "))
sum_of_digits = 0
while num > 0:
    sum_of_digits += num % 10
    num //= 10
    print("Sum of digits:", sum_of_digits)
    pass


a = ('1', 2, 3, 4, 5, 6, 7)
print(type(a[0]))