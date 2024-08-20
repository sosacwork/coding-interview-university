def get_powerset(s):
    """given a set find powerset 
    [1,2] -> [], [1], [2], [1,2]

    no duplicates
    """
    res = []
    backtrack([], 0, res, s)
    return res

def backtrack(subset, i, res, s):
    if i > len(s):
        return
    res.append(subset)
    for index, e in enumerate(s):
        if index < i:
            continue
        subset.append(e)
        new_subset = []
        new_subset.extend(subset)
        backtrack(new_subset, index+1, res, s)
        subset.pop()

if __name__ == "__main__":
    s = [1,2,3]
    powerset = get_powerset(s)
    print(f"Result:{powerset}")
    
    s = []
    powerset = get_powerset(s)
    print(f"Result:{powerset}")
    
    s = [1]
    powerset = get_powerset(s)
    print(f"Result:{powerset}")
    # O(2^n)
    
"""Given a M x N matrix, find number of paths moving from top left to bottom right.
Note that you can only move one step at a time and each step can be either 1 or 2 distance units.

1 2 3  
4 5 6  -> 5 ways

0 1 2 
1 2 5
"""
