'''
nodes are sorted
'''
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None
		
def removeDuplicatesFromLinkedList(linkedList):
	# Write your code here.
	cru = linkedList
	while cru is not None and cru.next is not None:
		print(cru.value)
		if cru.next.value == cru.value:
			cru.next = cru.next.next
		else:
			cru = cru.next
	return linkedList