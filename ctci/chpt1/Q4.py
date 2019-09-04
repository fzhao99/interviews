def palindromePerm(string):
    refTable = [0] * 256

    isOdd = 0
    for char in string:
        if char.isalpha():
            refTable[ord(char)] += 1
            if refTable[ord(char)] % 2 == 1:
                isOdd +=1

            if refTable[ord(char)] % 2 == 0:
                isOdd -= 1

    if isOdd <= 1:
        return True
    else:
        return False

print(palindromePerm("hello"))
