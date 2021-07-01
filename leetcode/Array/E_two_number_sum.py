'''
{
  "array": [3, 5, -4, 8, 11, 1, -1, 6],
  "targetSum": 10
}

return [-1,11]
you can assume at most one pair of numbers summing up to the target number
'''

# o(n)
def twoNumberSum(array, targetSum):
    # Write your code here.
    r = []
    helpHashT = {}


    for x in array:
        if targetSum - x not in helpHashT:
            helpHashT[x] = 0
        else:
            r += [x, targetSum - x]
            del helpHashT[targetSum - x]
    return r

def twoNumberSum(array, targetSum):
    array.sort()

    left=0
    right = len(array)-1
    while left < right:
        l,r = array[left], array[right]
        lr_sum = l+r
        if  lr_sum== targetSum:
         	return [l,r]
            
        elif lr_sum>targetSum:
            right-=1
        elif lr_sum<targetSum:
            left+=1
	return[]