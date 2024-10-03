def countConsistentStrings(allowed, words):
    # convert allowed chars to set
    allowed_set = set(allowed)
    consistent = 0
    for word in words:
        # For each word, check if every character is in the allowed set
        is_consistent = True
        for char in word:
            if char not in allowed_set:
                is_consistent = False
                break  # If a character is not allowed, no need to check further
        
        if is_consistent:
            consistent += 1
    
    return consistent
