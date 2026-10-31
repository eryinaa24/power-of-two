number=int(input("Enter a number: "))
while number<0 or number>300:
    print("Invalid number. Please enter a number between 0 to 300.")
    number=int(input("Enter a number: "))

total=2**number
number_of_digit=len(str(total))
print(f"{total}")
print(f"{number_of_digit}")
