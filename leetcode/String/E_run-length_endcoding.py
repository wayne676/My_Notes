'''
"AAAAAAAAAAAAABBCCCCDD"->"9A4A2B4C2D"
当前和之前不同 以及 counter == 9的时候 操作一下
'''
def runLengthEncoding(string):
    n=len(string)
    i=0
    counter=0
    prev=string[0]
    r=''
    while i<n:
        if string[i]!=prev or counter==9:
            r+=(str(counter)+prev)
            prev=string[i]
            counter=1
        else:
            counter+=1
        i+=1
    r=r+str(counter)+prev
    return r