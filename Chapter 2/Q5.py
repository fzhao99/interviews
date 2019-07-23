from LinkedList import LinkedList,Node

def sum_lists(d1,d2):
    answer = LinkedList()
    d1_runner = d1.head
    d2_runner = d2.head
    tens_from_prev = False
    while d1_runner and d2_runner:
        digit_sum = d1_runner.value + d2_runner.value
        if tens_from_prev:
            answer.add(Node(digit_sum % 10 + 1))
        else:
            answer.add(Node(digit_sum % 10))

        if digit_sum >= 10:
            tens_from_prev = True
        else:
            tens_from_prev = False

        d1_runner = d1_runner.next
        d2_runner = d2_runner.next

    if d1_runner is None and d2_runner is None:
        if tens_from_prev:
            answer.add(Node(1))
            return answer
        else:
            return answer
    elif d1_runner is None:
        while d2_runner:
            if tens_from_prev:
                answer.add(Node(d2_runner.value + 1))
            else:
                answer.add(Node(d2_runner.value))

            if d2_runner.value+1 >= 10:
                tens_from_prev = True
            else:
                tens_from_prev = False

            d2_runner = d2_runner.next
        return answer
    elif d2_runner is None:
        while d1_runner:
            if tens_from_prev:
                answer.add(Node(d1_runner.value + 1))
            else:
                answer.add(Node(d1_runner.value))

            if d1_runner.value+1 >= 10:
                tens_from_prev = True
            else:
                tens_from_prev = False
            d1_runner = d1_runner.next
        return answer


# provided answer

def sum_list_prov(ll_a,ll_b):
    ll_a_run, ll_b_run = ll_a.head, ll_b.head
    carry = 0
    ans = LinkedList()
    while ll_a_run or ll_b_run:
        result = carry
        if ll_a_run:
            result += ll_a_run.value
        if ll_b_run:
            result += ll_b_run.value
        ans.add(result % 10)
        carry = result // 10

        ll_a_run = ll_a_run.next
        ll_b_run = ll_b_run.next

    if carry:
        ans.add(1)
    return ans


#follow up

def sum_list_fol(ll_a,ll_b):
    if len(ll_a) < len(ll_b):
        for i in range(len(ll_b) - len(ll_a)):
            ll_a.add_to_beginning(0)
    else:
        for i in range(len(ll_a) - len(ll_b)):
            ll_b.add_to_beginning(0)

    ll_a_run, ll_b_run = ll_a.head, ll_b.head
    result = 0
    while ll_a_run and ll_b_run:
        result = result * 10 + ll_a_run.value + ll_b_run.value

        ll_a_run = ll_a_run.next
        ll_b_run = ll_b_run.next

    ll = LinkedList()
    for i in str(result):
        ll.add(int(i))

    return ll



ll1 = LinkedList()
ll1.generate(7, 0, 9)
print(ll1)
ll2 = LinkedList()
ll2.generate(5, 0, 9)
print(ll2)
print(sum_list_fol(ll2, ll1))
