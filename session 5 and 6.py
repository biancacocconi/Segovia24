try:
    age1 = int(input("What is your age player 1? "))
    age2 = int(input("What is your age player 2? "))
    res = age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("I am sorry, but you cannot divide by 0")
except:
    print("I am sorry, but something went wrong")
else:
    print('Player 1 is older than player 2 by a factor of ', res)
finally:
    print("Thank you for playing")

# I want to print the multiplication table from 1 to 10.
for i in range(1, 11):
    for j in range(i, 11):
        print(i, "x", j, "=", i*j)
    print()

import random
drinks = ["beer", "wine", "whiskey", "campari", "rum", "gin tonic", "rakia", "vodka", "martini", "sangria"]
try:
    age = int(input("How old are you? "))
    country = input("Where do you live? ")
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    # Do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative or greater than 130")
    elif age < 18:
        print("I am sorry, but you are too young to play this drinking game anywhere in the world.")
    elif age < 21 and country == "US":
        print("I am sorry, but you are too young to play this drinking game in the US.")
    else:
        drink = random.choice(drinks)
        print("Drink some", drink, ". Thank you for playing, you are", age, "years old so you can play this game in", country)

import random
lives = 3

while lives:
    print("You have", lives, "lives left")
    dice_roll = random.randint(1,6)
    if dice_roll == 6:
        print("You rolled a 6, you win!")
        break

    print("You rolled a", dice_roll, "try again")
    lives -= 1

else:
    print("You lost all your lives, game over.")

result = 0
for i in range(0,10):
    result += i
print("The sum of the first 9 numbers is", result)

result = 0
text = "1234567890"
for i in text:
    result += int(i)
print("The sum of the first 9 numbers is", result)

print(list(range(10)))
print(list(range(1, 11)))
print(list(range(0, 30, 5)))
print(list(range(0, 10, 3)))
print(list(range(0, -10, -1)))
print(list(range(0)))
print(list(range(1, 0)))

try:
    num = input("Give me a number:")
    num = int(num)
    print("The square of the number read is:", num*num)
except:
    print("Please give me a proper number.")

# Try/Except Syntax and Functionality
try:
    num = input("Give me a number:")
    num = int(num)
    num2 = input("Give me another number:")
    num2 = int(num2)
    result = num/num2

except ValueError:
    print("Please give me a proper number.")
except ZeroDivisionError:
    print("The second number cannot be zero.")
except:
    print("Some other exception I did not see coming.")
else:
    print("The division result is", result)

n = 1
result = 0

while n < 10:
    result += n
    n += 1
print("The sum of the first 9 numbers is", result)



# Infinite While Statements
while True:
    num = input("Give me a number (type quit to exit):")
    num2 = input("Give me another number(type quit to exit):")
    if num == "quit" or num2 == "quit":
        break
    num = int(num)
    num2 = int(num2)
    if num2 == 0:
        print("Cannot divide by zero")
        continue
    print("The division result of", num, "and", num2, "is", num/num2)
