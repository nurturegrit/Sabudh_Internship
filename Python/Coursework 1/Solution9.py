def factorial(num):
    if num:
        result = 1
        for i in range(2,num + 1):
            result *= i
        return result
    else:
        return 0
    
print(factorial(int(input("Enter a Number to get its Factorial:  "))))