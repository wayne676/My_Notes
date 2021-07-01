'''
"abaxyzzyxf" -> "xyzzyx"
遍历 字符串
分别检测当前 index 的左右两侧 和 右侧(abba形式)

'''
def longestPalindromicSubstring(string):
    r=''
    for i,v in enumerate(string):
        candidate = longestPalindromic(i, string)
        r = candidate if len(candidate)>len(r) else r
    return r
def longestPalindromic(i, string):
    odd =''
    left=i-1
    right=i+1
    while left>=0 and right<len(string):
        if string[left]!=string[right]:
            break
        left-=1
        right+=1
	odd = string[left+1:right]
	print(odd)
    even=''
    left =i
    right=i+1
    while left>=0 and right<len(string):
        if string[left]!=string[right]:
            break
        left-=1
        right+=1
	even = string[left+1:right]
    return odd if len(odd)>len(even) else even