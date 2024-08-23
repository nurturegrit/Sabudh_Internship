def roman_to_num(romans):
    roman_dict = {'M': 1000, 'CM': 900, 'D': 500,
                 'CD': 400, 'C': 100, 'XC': 90, 'L': 50,
                 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
                 'IV': 4, 'I': 1}
    search = ''
    ans = 0
    i = 0
    while not ans or search or i < len(romans):
        if len(search) < 2 and i < len(romans):
            search += romans[i]
            i += 1
        else:
            if search in roman_dict:
                ans += roman_dict[search]
                search = ''
            else:
                ans += roman_dict[search[0]]
                search = search[-1]
    return ans

print(roman_to_num('MMMCMXCIX'))