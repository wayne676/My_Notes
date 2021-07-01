'''
Given an array of integers between 1 and n so all positive integers
'''


def firstDuplicateValue(array):
    a = set()
    for x in array:
        if x in a:
            return x
        else:
            a.add(x)
    return -1


def firstDuplicateValue(array):
    for i, v in enumerate(array):
        if array[abs(v)-1] < 0:
            return abs(v)
        else:
            array[abs(v)-1] *= (-1)
    return -1
