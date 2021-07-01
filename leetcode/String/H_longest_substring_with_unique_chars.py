'''
"clementisacap" -> "mentisac"
当 last['e']=2 遇到第二个e 因为unique所以 要从 第三个位置从新算 start=3
也有例外就是遇到第二个 c 的时候 因为start已经大于last['c']=0 所以没必要退回到 0 位置
'''
# o(n) time 多一点点 space
def longestSubstringWithoutDuplication(string):
    # Write your code here.
    lastSeenAt={}
    start=0
    r=''
    for i,v in enumerate(string):
        if v in lastSeenAt:
            start=max(lastSeenAt[v]+1,start)
        r=max(r,string[start:i+1],key=lambda x: len(x))
        lastSeenAt[v]=i
	return r

# o(n*n) 少一点空间
def longestSubstringWithoutDuplication(string):
    # Write your code here.
    longest = ''
    n=len(string)
    for i,v in enumerate(string):
        j=i
        while j <n:
            if string[j] in string[i:j]:
                break
            j+=1
        longest=max(longest,string[i:j],key=lambda x: len(x))
	return longest