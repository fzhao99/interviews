from data_structures.LinkedList import LinkedList


def delete_mid(n):
    next = n.next
    if next is None:
        return False

    else:
        n.value = next.value
        n.next = next.next
        return True
