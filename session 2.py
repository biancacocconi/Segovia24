name = input("what is your name? ")

age = input("how old are you? ")
age = int(age)
birth_year = 2023 - age

print(f"OMG {name}, you are {age} years old so you are born in {birth_year}!")

age = int(input("what is your age? "))
age = int(age)

print(f"Your age is {age}")

try:
    age=int(input("what is your age? "))
except ValueError:
    print("I am sorry, but that is not a valid answer")
else:
    print("Your age is", age)

try:
    age1 = int(input("what is your age player 1? "))
    age2 = int(input("ehat is your age player 2? "))
    res = age1/age2
except ValueError:
        print("I am sorry, but that is not a valid answer")
else:
        print("player 1 is older than player 2 by a factor of", res)


import random
drinks = ("beer", "wine", "whiskey", "campari", "tequila", "rum", "gin tonic", "cakia")
try:
    age = int(input ("How old are you? "))
    country = input ("Where do you live? ")
except ValueError:\
    print("I am sorry, but that is not a valid number")
else:
    # Do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative, or greater than 130")
    elif age < 18:
        print ("I am sorry, too young to play this drinking game anywhere in the world")
    elif age < 21 and country == "US":
        print("I am sorry, too young to play this drinking game in the US")
    else:
        drink = random. choice(drinks)