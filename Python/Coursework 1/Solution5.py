def series_sum(n=None):
    if n is None:
        n = int(input("Enter a numer for 2's series:  "))
    sum = 0
    for i in range(1, n+1):
        num = int('2' * i)
        sum += num
    print(f"The sum of 2's series upto {n} Numbers is {sum}")
    return sum

series_sum()