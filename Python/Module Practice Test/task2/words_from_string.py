# Generator function that yields words from a string
def word_generator(string):
    words = string.split()
    for word in words:
        yield word

# Generate all words from the string
test_string = "The quick brown fox jumps over the lazy dog"
for word in word_generator(test_string):
    print(word)
