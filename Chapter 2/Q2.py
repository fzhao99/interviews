from LinkedList import LinkedList


def k_to_last(k, ll):
    p2 = ll.head

    for p2Counter in range(k):
        if p2.next == None:
            return None
        p2= p2.next

    p1 = ll.head

    while p2:
        p1 = p1.next
        p2 = p2.next

    return p1

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))
