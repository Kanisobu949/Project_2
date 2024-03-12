import math

code = str(input("Enter customer code (R, C, or I): "))

if code == "R" or code == "C" or code == "I":
    begin = int(input("Enter beginning numbers (between 0 and 999999999): "))
    if not begin in range(0,999999999):
        print("Invalid input (Beginning is out of range)")
        exit()
    end = int(input("Enter end numbers (between 0 and 999999999): "))
    if not end in range(0,999999999):
        print("Invalid input (End is out of range)")
        exit()
else:
    print("Invalid input (customer code)")
    exit()

if end < begin:
    tot = end - begin + 1000000000
else:
    tot = end - begin

total_gal = tot / 10

if code == "R":
    total = (total_gal*0.0005) + 5
elif code == "C":
    if total_gal <= 4000000:
        total = 1000
    else:
        total = (total_gal*0.00025)+1000
elif code == "I":
    if total_gal < 4000000:
        total = 1000
    elif total_gal >= 4000000 and total < 10000000:
        total = 2000
    else:
        total = (total_gal*0.00025) + 2000

print(f'Your code is {code}')
print(f'Your beginning numbers are {begin:09}')
print(f'Your ending numbers are {end:09}')
print(f'The amount of gallons you used was {total_gal:.1f} gallons')
print(f"Your total is {total:.2f} dollars")