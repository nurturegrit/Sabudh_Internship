def get_roman_numeral(num):
    def convert_to_roman(num):
        if num >= 1000:
            n = num // 1000
            remainder = num % 1000
            return 'M' * n, remainder
        elif num >= 100:
            n = num // 100
            remainder = num % 100
            if n == 9:
                return 'CM', remainder
            elif n >= 5:
                return 'D' + ('C' * (n - 5)), remainder
            elif n == 4:
                return 'CD', remainder
            else:
                return 'C' * n, remainder
        elif num >= 10:
            n = num // 10
            remainder = n % 10
            if n == 9:
                return 'XC', remainder
            elif n >= 5:
                return 'L' + ((n - 5) * 'X'), remainder
            elif n == 4:
                return 'XL', remainder
            else:
                return 'X' * n, remainder
        else:
            if num == 9:
                return 'IX', 0
            elif num >= 5:
                return 'V' + ((num - 5) * 'I'), 0
            elif num == 4:
                return 'IV', 0
            else:
                return 'I' * num, 0

    ans = ''
    while num != 0:
        roman_numeral, num = convert_to_roman(num)
        ans += roman_numeral
    return ans

print(get_roman_numeral(3999))