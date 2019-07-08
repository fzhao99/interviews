def oneAwayHelp(string1, string2):
    if abs(len(string1) - len(string2)) >1 :
        return False

    ref = [0] * 128
    for char in string1:
        ref[ord(char)] += 1
    isOneAway = 0
    for char in string2:
        toCheck = ref[ord(char)]
        if toCheck == 0:
            isOneAway += 1

    if isOneAway <= 1:
        return True
    else:
        return False


def oneAway(string1, string2):
    if len(string1) < len(string2):
        return oneAwayHelp(string1, string2)
    else:
        return oneAwayHelp(string2, string1)

print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))
