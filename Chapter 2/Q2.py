from data_structures.LinkedList import LinkedList

def kth_to_last(ll, k ):
    end_tracker = ll.head
    elem_tracker = ll.head

    for i in range(k):
        if end_tracker.next:
            end_tracker = end_tracker.next
        else:
            return None

    while end_tracker:
        end_tracker = end_tracker.next
        elem_tracker = elem_tracker.next

    return elem_tracker.value

ll = LinkedList()
ll.generate(10, 0 ,99)
print(ll)
print(kth_to_last(ll, 3))
