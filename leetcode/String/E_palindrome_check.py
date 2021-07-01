'''
String is same written from forward and backward 
前后相聚中间 i小于n时循环
'''


def isPalindrome(string: str) -> bool:
    n = len(string)-1
    i = 0
    while i < n:
        if string[i] != string[n]:
            return False
        i += 1
        n -= 1
    return True
