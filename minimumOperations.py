def countMinSwaps(arr):
    pairs = [(val, i) for i, val in enumerate(arr)]
    pairs.sort()

    swaps = 0 
    for i in range(len(pairs)):
        if i != pairs[i][1]:
            swaps += 1
    
    return 0 if not swaps else swaps - 1


countMinSwaps([4,6,5,7])