def successful(potions, spells, success):
    ans = []
    for spell in spells:
        n = 0
        for potion in potions:
            if spell*potion >= success:
                n += 1
        ans.append(n)
    return ans

p = [1,2,3,4,5]
s = [5,1,3]
print(successful(p, s, 7))
s = [3,1,2]
p = [8,5,8]
print(successful(p, s, 16))
