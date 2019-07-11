def oneAway(string1, string2):
    if abs(len(string1)-len(string2)) > 1:
        return False

    refTable = [0] * 256

    for char in string1:
        refTable[ord(char)] += 1

    isOneAway = 0

    for char in string2:
        if refTable[ord(char)] != 1:
            isOneAway += 1

    if isOneAway > 1:
        return False
    else:
        return True


print(oneAway("pale", "ple"))
print(oneAway("pale", "palesestra"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))
