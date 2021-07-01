
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is None:
            return False
        elif slow == fast:
            break
    slow = head
    while slow != fast:
        slow=slow.next
        fast = fast.next
    return slow
    