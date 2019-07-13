from LinkedList import LinkedList

def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    refTable = {current.value}

    while current.next:
        if current.next.value in refTable:
            current.next = current.next.next
        else:
            refTable.add(current.next.value)
            current = current.next

    return ll

def remove_dups_follow_up(ll):
    if ll.head is None:
        return

    current = ll.head

    while current:
        runner = current

        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll


ll = LinkedList()
ll.generate(30,0,9)
print(ll)
print(remove_dups(ll))


ll = LinkedList()
ll.generate(30,0,9)
print(ll)
print(remove_dups_follow_up(ll))
