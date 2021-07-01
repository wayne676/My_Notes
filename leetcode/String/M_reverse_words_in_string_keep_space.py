'''
翻转单词 保留空格  'ab  c' -> 'c  ab'
把空格当 空串 压入列表 再用 空格 join 灵感来自 split 和 join
'''

def reverseWordsInString(string):
    r = []
    i = len(string)-1

    temp = ''
    while i >= 0:
        v = string[i]
        if v != ' ':
            temp = v+temp
        else:
            r.append(temp)
            temp = ''
        i -= 1
    r.append(temp)
    return ' '.join(r)
