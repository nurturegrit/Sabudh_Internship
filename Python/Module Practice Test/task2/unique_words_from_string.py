# Generator function for unique words in a list
def unique_word_generator(word_list):
    seen = set()
    for word in word_list:
        word_lower = word.lower()  # To make uniqueness case-insensitive
        if word_lower not in seen:
            seen.add(word_lower)
            yield word

# Generate unique words from the list
word_list = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
for word in unique_word_generator(word_list):
    print(word)