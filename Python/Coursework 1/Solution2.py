def solution():
    s = input("Enter a String: ")
    result = ''
    for char in s:
        if char not in result:
            result += char
    return result

print(solution())