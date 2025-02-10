num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
    if num % 6 == 0:
        print(f"{num} is also divisible by 6")
    else:
        print(f"{num} is not divisible by 6")
else:
    print(f"{num} is Odd")
    if num % 5 == 0:
        print(f"{num} is also divisible by 5")
    else:
        print(f"{num} is not divisible by 5")
