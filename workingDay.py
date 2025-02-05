A= int(input("Number of Days work by A : "))
B= int(input("Number of Days work by B : "))
C= int(input("Number of Days work by C : "))

ans = A*B*C//(A*B+B*C+C*A)
print(f"Number of days that all the person take to complete the work : {ans}")