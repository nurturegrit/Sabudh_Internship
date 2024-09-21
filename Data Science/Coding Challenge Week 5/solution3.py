def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        # Add to stack
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()
    return ''.join(stack)


print(remove_adjacent_duplicates('aaaaab'))