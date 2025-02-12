print("ITEMS")
print("Mango : 20$")
print("Bread : 05$")
print("Egg   : 10$")
print("Maggi : 12$")
print("Bucket: 22$")
print("Mugg  : 05$")
print("Choko : 07$")
Mango = 20
Bread = 5
Egg = 10
Maggi = 12
Bucket = 22
Mugg = 5
Choko = 7

a = input("Enter 1st item what you wnat: ")
q1 = int(input("Enter Quantity: "))
b = input("Enter 2st item what you wnat: ")
q2 = int(input("Enter Quantity: "))
c = input("Enter 2st item what you wnat: ")
q3 = int(input("Enter Quantity: "))
t = 0
if a == "Mango":
   t = t+(Mango*q1)
if a == "Bread":
   t = t+(Bread*q1)
if a == "Egg":
   t = t+(Egg*q1)
if a == "Maggi":
   t = t+(Maggi*q1)
if a == "Bucket":
   t = t+(Bucket*q1)
if a == "Mugg":
   t = t+(Mugg*q1)
if a == "Choko":
   t = t+(Choko*q1)


if b == "Mango":
   t = t+(Mango*q2)
if b == "Bread":
   t = t+(Bread*q2)
if b == "Egg":
   t = t+(Egg*q1)
if b == "Maggi":
   t = t+(Maggi*q2)
if b == "Bucket":
   t = t+(Bucket*q2)
if b == "Mugg":
   t = t+(Mugg*q2)
if b == "Choko":
   t = t+(Choko*q2)

if c == "Mango":
   t = t+(Mango*q3)
if c == "Bread":
   t = t+(Bread*q3)
if c == "Egg":
   t = t+(Egg*q1)
if c == "Maggi":
   t = t+(Maggi*q3)
if c == "Bucket":
   t = t+(Bucket*q3)
if c == "Mugg":
   t = t+(Mugg*q3)
if c == "Choko":
   t = t+(Choko*q3)

if a == b or a ==c or a==b or b == c:
   print("Don't Enter Same Item Again!!")
else:
    print("Total amount", end = " : ")
    print(t)
if t > 50:
    d = (t*10)/100
    print("You get Discout of 10%", end=" : ")
    print(f"{d}$")
else:
    print("You are not eligible for Discount!!!")

    print("Payable amout : ", end="")
    print(f"{t-d}$")