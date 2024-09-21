# Generator function for sublists of length n
def sublist_generator(lst, n):
    for i in range(len(lst) - n + 1):
        yield lst[i:i+n]

# Generate all sublists of length 3 from the list
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for sublist in sublist_generator(test_list, 3):
    print(sublist)
