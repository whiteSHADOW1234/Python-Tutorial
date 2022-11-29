# format specifiers = {:flags} format a value based on what flags are inserted

price1 = 3159456.14159456789
price2 = -987789456.65456
price3 = 4.34
print(f"price1 is: ${price1:}")
print(f"price2 is: ${price2:}")
print(f"price3 is: ${price3:}")

# .(number)f = round to that many decimal places
print(f"price1 is: ${price1:.3f}")
print(f"price2 is: ${price2:.3f}")
print(f"price3 is: ${price3:.1f}")
# :(number) = allocate at least that many spaces
print(f"price1 is: ${price1:10.3f}")
print(f"price2 is: ${price2:10.3f}")
print(f"price3 is: ${price3:10.3f}")
# :0(number) = allocate and zero pad at least that many spaces
print(f"price1 is: ${price1:010.3f}")
print(f"price2 is: ${price2:010.3f}")
print(f"price3 is: ${price3:010.3f}")
# :< = left justify
print(f"price1 is: ${price1:<10.3f}")
print(f"price2 is: ${price2:<10.3f}")
print(f"price3 is: ${price3:<10.3f}")
# :> = right justify
print(f"price1 is: ${price1:>20.3f}")
print(f"price2 is: ${price2:>20.3f}")
print(f"price3 is: ${price3:>20.3f}")
# :^ = center align
print(f"price1 is: ${price1:^20.3f}")
print(f"price2 is: ${price2:^20.3f}")
print(f"price3 is: ${price3:^20.3f}")
# :+ = use a plus sign to indicate positive value
print(f"price1 is: ${price1:+10.3f}")
print(f"price2 is: ${price2:+10.3f}")
print(f"price3 is: ${price3:+10.3f}")
# := = place sign to leftmost position
print(f"price1 is: ${price1:=20.3f}")
print(f"price2 is: ${price2:=20.3f}")
print(f"price3 is: ${price3:=20.3f}")
# :  = insert a space before positive numbers
print(f"price1 is: ${price1: 10.3f}")
print(f"price2 is: ${price2: 10.3f}")
print(f"price3 is: ${price3: 10.3f}")
# :, = comma separator
print(f"price1 is: ${price1:,}")
print(f"price2 is: ${price2:,}")
print(f"price3 is: ${price3:,}")
# :% = percentage format
print(f"price1 is: {price1:%}")
print(f"price2 is: {price2:%}")
print(f"price3 is: {price3:%}")