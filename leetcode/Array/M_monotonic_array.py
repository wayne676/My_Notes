'''
[-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
-> true
non-increasing or non-decreasing
'''
def isMonotonic(array):
    n=len(array)
    if n==1or n==2:
        return True
    up=0
    down=0
    
    for i in range(1,n):
        if array[i]-array[i-1]>0:
            up=1
        elif array[i]-array[i-1]<0:
            down=1
    return False if up==1 and down==1 else True