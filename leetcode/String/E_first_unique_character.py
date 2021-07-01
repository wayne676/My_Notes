def firstNonRepeatingCharacter(string):
    dict = {}
    for c in string:
        dict[c] = dict.get(c, 0)+1
    for i, v in enumerate(string):
        if dict[v] == 1:
            return i
    return -1
