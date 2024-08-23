def pair_sum_k(array, k):
    pairs = []
    counter = {}
    for num in array:
        counter[num] = counter.get(num, 0) + 1
    found = set()
    for key in counter.keys():
        if key in found:
            continue
        elif k - key == key:
            found.add(key)
            pairs.extend([key, key] for i in range((counter[key] * (counter[key] - 1))//2))
        elif k - key in counter.keys():
            found.add(k - key)
            pairs.extend([[key, k - key] for  i in range(counter[key] * counter[k - key])])
    return pairs


# test case
print(pair_sum_k([1, 5, 7, -1, 3, 3], 6))
print(pair_sum_k([1, 5, 7, -1, 5], 6))