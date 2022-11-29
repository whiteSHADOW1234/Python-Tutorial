unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))
degree_sign = u'\N{DEGREE SIGN}'
if unit == "C" or unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} {degree_sign}F")
elif unit == "F" or unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp} {degree_sign}C")
else:
    print(f"{unit} is an invalid unit of measurement")