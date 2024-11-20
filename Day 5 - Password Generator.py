import os
os.system('cls' if os.name == 'nt' else 'clear')

# # # Loop
# # # For
# # instruments = ["Guitar","Piano","Violin","Bass"]
# # for instrument in instruments:
# #     print(instrument)
    
# # # Range()

# # total = 0

# # for number in range (1, 101):
# #     print(number)
   

# import random
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]
# symbols = ['(', ')', ('&'), ('~'),('#'),('@'),(']'),('}'),('$'),('+'),('?'),('*'),('!')]

# # Easy Level Password Generator
# password = ""

# print("Welcome to the Password Generator App! ")
# num_of_lett = int(input("How Many Letters You Want in Your Password? \n"))
# num_of_num = int(input("How Many Numbers You Want in Your Password? \n"))
# num_of_symb = int(input("How Many Symbols You Want in Your Password? \n"))

# for char in range (0, num_of_lett):
#    password += random.choice(letters)

# for num in range (0, num_of_num):
#    password += random.choice(numbers)

# for symb in range (0, num_of_symb):
#    password += random.choice(symbols)

# print("Your Password is: " + (password))


# # Hard Level Password Generator!

import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]
symbols = ['(', ')', ('&'), ('~'),('#'),('@'),(']'),('}'),('$'),('+'),('?'),('*'),('!')]
password = ""

print("Welcome to the Password Generator App! ")
num_of_lett = int(input("How Many Letters You Want in Your Password? \n"))
num_of_num = int(input("How Many Numbers You Want in Your Password? \n"))
num_of_symb = int(input("How Many Symbols You Want in Your Password? \n"))

for char in range (num_of_lett):
   password += random.choice(letters)

for num in range (num_of_num):
   password += random.choice(numbers)

for symb in range (num_of_symb):
   password += random.choice(symbols)

   password_list = list(password)
random.shuffle(password_list)
shuffled_password = ''.join(password_list)

print("Your Shuffled Password is: " + shuffled_password)
input("\nPress Enter to exit...")

