def isPerm(string1, string2):
    if len(string1) != len(string2):
        return False

    references = [0] * 256

    for char in string1:
        references[ord(char)]  += 1

    for char in string2:
        references[ord(char)] -= 1

        if references[ord(char)] < 0:
            return False

    return True


print(isPerm("test1","test"))
print(isPerm("test1","test2"))
print(isPerm("cat", "tac"))
print(isPerm("caterwaul", "aacetlurw"))
