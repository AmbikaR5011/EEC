#Random Password Generator
import random
print("Welcome yo random password generator")
random_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
no_of_pass=int(input("Please enter the number of password to be generated:"))
len_of_pass=int(input("Please enter the length of the password needed:"))
print("Here are your random passwords:")
for x in range(no_of_pass):
    password=""
    for chars in range(len_of_pass):
        password = password+random.choice(random_chars)
    print(password)