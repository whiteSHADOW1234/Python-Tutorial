# Here are the Unicode characters I use for drawing the dice.
# Youtube has strange spacing, so the ASCII art looks warped in the description. 
# It should still work if you copy and paste it into PyCharm.

# 0 ¢z ¢w ¢{ | ¢| ¢}

import random

dice_art = {
    1: ("__________ ",
        "|         |",
        "|    0    |",
        "|         |",
        "|_________|"),
    2: ("__________ ",
        "|  0      |",
        "|         |",
        "|      0  |",
        "|_________|"),
    3: ("__________ ",
        "|  0      |",
        "|    0    |",
        "|      0  |",
        "|_________|"),
    4: ("__________ ",
        "|  0   0  |",
        "|         |",
        "|  0   0  |",
        "|_________|"),
    5: ("__________ ",
        "|  0   0  |",
        "|    0    |",
        "|  0   0  |",
        "|_________|"),
    6: ("__________ ",
        "|  0   0  |",
        "|  0   0  |",
        "|  0   0  |",
        "|_________|")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# PRINT VERTICALLY
for die in range(num_of_dice):
   for line in dice_art.get(dice[die]):
       print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")