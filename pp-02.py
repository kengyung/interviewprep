# determine is a string has all unique characters. Assumption char is not case sensitive (i.e.: T = t)

def checkUniqChars(inputString):  # assumes we can use hashmap
    if len(inputString) == 0:
        return False

    inputStringConv = inputString.lower()
    hm = {}

    for i in range(len(inputStringConv)-1):
        if hm.get(inputStringConv[i]) == None:
            hm[inputStringConv[i]] = i
        else:
            return False

    return True


def checkUniqChars2(inputString):
    if len(inputString) > 128:
        return False


testString = "TestString"
testString2 = "Tesring"
testString3 = ""

print(checkUniqChars(testString3))
checkUniqChars2(testString)
