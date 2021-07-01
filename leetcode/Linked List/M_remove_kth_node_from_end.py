'''
you can assume that your input linked list will always have at least two nodes
'''
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

# method 1
def removeKthNodeFromEnd(head, k):
	# Write your code here.
	cur = head
	i=0
	while cur is not None:
		cur=cur.next
		i+=1
	print(i)
	if k ==i:
		head.value=head.next.value
		head.next=head.next.next
		#head=head.next
		print(head.value)
		return head
	i=i-k
	j=0
	cur=head
	while j<i-1:
		cur=cur.next
		j+=1
		print(cur.value)
	cur.next = cur.next.next
# method 2
def removeKthNodeFromEnd(head, k):
	
	counter=1
	second=first=head
	
	while counter <=k:
		second=second.next
		counter+=1
	if second is None:
		head.value=head.next.value
		head.next=head.next.next
		return
	while second.next is not None:
		second = second.next
		first=first.next
	first.next=first.next.next
	

# method 3

def removeKthNodeFromEnd(head, k):
	# Write your code here.
	array_ref = []
	node_iter = head
	while node_iter is not None:
		array_ref.append(node_iter)
		node_iter = node_iter.next
	if k == len(array_ref):
		array_ref[0].value = array_ref[1].value
		array_ref[0].next = array_ref[1].next
		return array_ref[0]
	array_ref[-k-1].next= array_ref[-k].next
	return array_ref[0]