from LinkedList import LinkedList

def removeDups(ll):

    if ll.head is None:
        return

    runner = ll.head
    refTable = set([runner.value]) #Initialize with the head value@
    while runner.next: #we're checking .next for the end of the list, not the actual node!
        if runner.value.next in refTable:
            runner.next = runner.next.next

        else:
            refTable.add(runner.next.value)
            runner = runner.next

    return ll


#follow up

def removeDupsFollowUp(ll):
    if ll.head is None:
        return

    current = ll.head

    while current.next:
        runner = current.next

        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next

            else:
                runner = runner.next

        current = current.next

    return ll
