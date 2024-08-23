n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
n3 = int(input("Enter Third Number: "))

median = None
if n3 >= n1 >= n2 or n3 <= n1 <= n2:
    median = n1
elif n3 >= n2 >= n1 or n3 <= n2 <= n1:
    median = n2
else:
    median = n3

print(f"Median is {median}")

#Using COnditional Statements is more efficient in this case than sorted function