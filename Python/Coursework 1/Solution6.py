def reverse_num(num=None):
    if num is None:
        num = input("Input a Number: ")
    result = ''
    for digit in num:
        result = digit + result
    print(result)
    return int(result)

reverse_num()