import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
    #first we want to get the user to tell us the length of the password they're comfortable with or we can randomize password
    num_of_char = random.randint(10, 25)
    #num_of_char = int(input("Enter password length: "))

    #then we want to get the possible characters (the characters list written out earlier), and randomly select the amount of characters, 
    password = []
    for i in range(num_of_char):
        password.append(random.choice(characters))

    # then send out a randomized version of that list.
    random.shuffle(password)
    
    print("".join(password))
    
    #side tangent idea: maybe even store password in a file

generate_random_password()