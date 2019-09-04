def permutation(str):
    permHelper(str,"")

def permHelper(str, prefix):
    if(len(str) ==0):
        print(prefix)
    else:
        for i in range(len(str)-1):
            rem = str[0:i] + str[i+1]

            print("Rem: " + rem)
            permHelper(rem,prefix + str[i])


permutation("test")
