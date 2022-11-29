import math

print(math.e)
print(math.pi)
x = 9
result = math.sqrt(x)
print(result)
x += 0.2
result = math.ceil(x)
print(result)
result = math.floor(x)
print(result)

# ------------------------------------------------
# EXERCISE 1 CIRCLE RADIUS & AREA
# ------------------------------------------------
radius = float(input("Enter the radius: "))
result = 2 * math.pi * radius
print(f"The circumference is: {round(result, 2)}cm")
result = math.pi * radius ** 2
print(f"The area is: {round(result, 2)}cm^2")

# ------------------------------------------------
# EXERCISE 2 HYPOTEENUSE CALCULATOR
# ------------------------------------------------
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
result = math.sqrt(side_a ** 2 + side_b ** 2)
print(f"The length of the hypotenuse is: {round(result, 2)}cm")