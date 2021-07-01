'''
linkedListOne = 2->4->7->1
// 1742
linkedlistTwo = 9->4->5
// 549
Note: your function must create and return a new Linked List, and you are now allowed to modify
either of the input Linked Lists
'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# method 1 use string
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    
    one = ''
    while linkedListOne is not None:
        
        one=str(linkedListOne.value)+one
        linkedListOne=linkedListOne.next
    two = ''
    while linkedListTwo is not None:
        two=str(linkedListTwo.value)+two
        linkedListTwo=linkedListTwo.next
    
    he = str(int(one)+int(two))
    
    cursup=None
    for i in range(0,len(he)):
        
        cur=LinkedList(int(he[i]))
        cur.next=cursup
        cursup=cur
    return cur


# method 2
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    a = linkedListOne
    b = linkedListTwo
    n = cur = LinkedList(0)
    carry = 0
    while a is not None or b is not None:
        av = a.value if a is not None else 0
        bv = b.value if b is not None else 0
        
        value =  (av+bv)%10
        cur.next = LinkedList(value+carry)
        carry = (av+bv)//10
        
        cur=cur.next
        a=a.next if a is not None else None
        b=b.next if b is not None else None
    if carry !=0:
        cur.next = LinkedList(carry)
        
    return n.next