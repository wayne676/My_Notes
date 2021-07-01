'''
array is already sorted
"array": [-10, -5, 0, 5, 10] - >
[0, 25, 25, 100, 100]
"array": [-7, -3, 1, 9, 22, 30] ->
[1, 9, 49, 81, 484, 900]
'''


def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [0] * len(array)
    start = 0
    end = len(array) - 1
    i = len(array) - 1
    while i >= 0:
        sv = array[start] * array[start]
        ev = array[end] * array[end]
        if sv >= ev:
            sortedSquares[i] = sv
            start += 1
        else:
            sortedSquares[i] = ev
            end -= 1
        i -= 1
    return sortedSquares
