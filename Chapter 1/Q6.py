def comp(string):

    ans = []

    counter = 0
    for c in range(len(string)):
        if c != 0 and string[c] != string[c-1]:
            ans.append(string[c-1] + str(counter))
            counter = 0
        counter += 1

    ans.append(string[-1] + str(counter) )

    return min(string, "".join(ans), key=len)

print(comp("aabbcccccccccccccccdd"))
