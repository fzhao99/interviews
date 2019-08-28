from data_structures.LinkedList import LinkedList


def intersection(ll_1, ll_2):
    ll_1_runner = ll_1.head
    ll_2_runner = ll_2.head

    len_1 = 0
    len_2 = 0

    while ll_2_runner:
        len_2 += 1
        ll_2_runner = ll_2_runner.next

    while ll_1_runner:
        len_1 += 1
        ll_1_runner = ll_1_runner.next

    if ll_1_runner is not ll_2_runner:
        return False

    ll_2_runner = ll_2.head
    ll_1_runner = ll_1.head

    if len_1 > len_2:
        for i in range(len_1 - len_2):
            ll_1_runner = ll_1_runner.next

    if len_2 > len_1:
        for i in range(len_2-len_1):
            ll_2_runner = ll_2_runner.next

    while ll_2_runner and ll_1_runner:
        if ll_2_runner == ll_1_runner:
            return ll_2_runner
        ll_2_runner = ll_2_runner.next
        ll_1_runner = ll_1_runner.next
