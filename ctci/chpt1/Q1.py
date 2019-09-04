def isUnique(string):
    tally = [0] * 256

    for char in string:
        if tally[ord(char)] !=0:
            return False
        else:
             tally[ord(char)] +=1

    return True


print(isUnique("test"))
print(isUnique("cat"))
print(isUnique("unique"))
print(isUnique("abcdefghijklmnopqrstuvwxyz"))
