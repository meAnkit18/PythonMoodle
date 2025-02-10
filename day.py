day_num = int(input("Enter a number (1 to 7): "))

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= day_num <= 7:
    print(f"Day of the week: {days[day_num - 1]}")
else:
    print("Invalid input! Please enter a number between 1 and 7.")
