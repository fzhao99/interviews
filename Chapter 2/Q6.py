from LinkedList import LinkedList

def is_palindrome(ll):
    ahead_runner = ll.head
    behind_runner = ll.head

    #get behind_runner to middle of ll
    while ahead_runner.next.next:
        behind_runner = behind_runner.next
        ahead_runner = ahead_runner.next.next

    if ahead_runner:
        behind_runner= behind_runner.next

    ahead_runner = ll.head

    while behind_runner:
        if behind_runner.value == ahead_runner.value:
            behind_runner = behind_runner.next
        else:
            return False

    return True
