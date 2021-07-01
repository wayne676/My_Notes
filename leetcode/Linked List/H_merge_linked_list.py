'''
链表的算法题 有时可以使用dummyhead 来简化一些逻辑
并且 使用 
temp = cur.next
...
...
cur = temp
这种方法可以改变链表结点的结构 reverse linkedlist 也用到了这个
'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
	
	dummyhead = LinkedList(0)
	dummyhead.next = headOne
	cur = dummyhead
	while cur.next and headTwo:
		if cur.next.value<headTwo.value:
			cur=cur.next
		else:
			temp = headTwo.next
			headTwo.next = cur.next
			cur.next = headTwo
			headTwo = temp
	if cur.next is None:
		cur.next = headTwo
	return dummyhead.next