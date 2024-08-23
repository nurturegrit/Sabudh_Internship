def printOddIndex(arr= None):
    output = []
    if arr is None:
        arr = [int(num) for num in input("Enter a List of Numbers seperated by comma").split(",")]
    for i in range(1, len(arr), 2):
        print(arr[i])
        output.append(arr[i])
    return output

printOddIndex()