def divisibleBy5(arr= None):
    if arr is None:
        arr = [int(num) for num in input("Enter a list of Numbers Seperated by Commas: ").split(",")]
    result = []
    for num in arr:
        if num > 500:
            break
        if num > 150:
            continue
        if num%5 == 0:
            result.append(num)
    print(result)
    return result

divisibleBy5()