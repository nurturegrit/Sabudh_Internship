def solution():
    vowels = consonants = 0
    s = input("Input a word: ").lower()
    for char in s:
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    print(f"Vowels : {vowels}\nConsonants : {consonants}")

solution()