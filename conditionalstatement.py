temperature = 32


if temperature<25:
    print("Its cold")
elif temperature>25:
    print("Its hot")
else:
      print("Normal temperature")

# A program that returns the largest number among three numbers
first = 56
second = 23
third = 78
if first>second and first>third:
    print(first, " is the largest number")
elif second > first and second> third:
    print(second, "is the largest number")
else:
    print(third, "is the largest number")

# a program that checks if a number is even or odd
no1 = 17
no2 = 14
def check_even_odd (no1):
    if no1 % 2 == 0:
        return  "The number is even"
    else:
        return "The number is odd"

result = check_even_odd(no1)
print(result)

def check_even_odd (no1):
    if no2 % 2 == 0:
        return  "The number is even"
    else:
        return "The number is odd"

result = check_even_odd(no2)
print(result)