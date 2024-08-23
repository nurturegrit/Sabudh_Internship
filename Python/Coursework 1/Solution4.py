def countDigits(num= None):
    if num is None:
        num = input("Enter a number: ")
    num = int(num)
    n = 0
    while num > 0:
        n += 1
        num //= 10
    return n


print(countDigits())
    