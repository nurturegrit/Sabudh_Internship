# Problem 1:
# Given an integer array nums,
# return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0

def zero_sum_triplets(array):
    triplets = []
    for i in range(len(array)):
        found = set()
        for j in range(i+1, len(array)):
            compliment = - (array[i] + array[j])
            if compliment in found:
                continue
            for k in range(j+1, len(array)):
                if array[k] == compliment:
                    triplets.append([array[i], array[j], array[k]])
                    found.add(compliment)
                    break
    return triplets

print(zero_sum_triplets([0]*3))
print(zero_sum_triplets([0,1,1]))
print(zero_sum_triplets([-1,0,1,2,-1,-4]))