class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    cur = head
    cur_next = None
    while cur is not None:
        temp = cur.next
        cur.next = cur_next
        cur_next = cur
        cur = temp
    return cur_next