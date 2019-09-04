import sys
sys.path.append("..")

from data_structures.LinkedList import LinkedList

def partition(ll, val):
    before_list = LinkedList()
    after_list = LinkedList()

    current = ll.head
    while current:
        if current.value < val:
            before_list.add(current.value)
        else:
            after_list.add(current.value)

    if before_list.tail is None:
        return after_list
    else:
        before_list.add(Node(None))
        before_list.tail.next = after_list.head
        return before_list

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(partition(ll, ll.head.value))
