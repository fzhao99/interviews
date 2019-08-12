from LinkedList import LinkedList

def is_loop(ll):
    slow=fast = ll.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        #collission point
        if slow is fast:
            break


    # if the fast is none, then no loop exists
    if fast is None or fast.next is None:
        return None

    fast = ll.head

    while slow is not fast:
        fast = fast.next
        slow = slow.next

    return fast
