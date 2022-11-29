import random

number = random.random() # returns a random float between 0 and 1
print(number)

low = 1
high = 100
number = random.randint(low, high)
print(number)

options = ("Rock", "Paper", "Scissors")
choice = random.choice(options)
print(choice)

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)

choice = random.choice(cards)
print(choice)

# -------------- NUMBER GUESSING GAME --------------

import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
   guess = int(input(f"Enter a number between ({low} - {high}): "))
   guesses += 1

   if guess < number:
       print(f"{guess} is too low")
   elif guess > number:
       print(f"{guess} is too high")
   else:
       print(f"{guess} is correct!")
       break

print(f"This round took you {guesses} guesses")