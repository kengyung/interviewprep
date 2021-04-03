# Given a target integer and an array of numbers, return if there exists a combination the sums to the target integer (i.e: true/false)
# challenge: return instead, the indices of two numbers that sum to that amount
# returns True or False if there are two integers that sum to the target amount and -1 if the array is less than 2 integers
def doesTwoSumExist(target, alist):
    if len(alist) > 1:  # Checks if alist is at least 2 numbers
        i = 0
        while i < len(alist):
            testNum1 = alist[i]
            testNum2 = target - testNum1
            if testNum2 in alist:
                return True
            else:
                i += 1
        return False
    else:
        return -1


# returns the indicies of the two numbers if it exists, False otherwise and -1 if the array is <2 numbers
def doesTwoSumExistIndicies(target, alist):
    if len(alist) > 1:  # Checks if alist is at least 2 numbers
        i = 0
        while i < len(alist):
            testNum1 = alist[i]
            testNum2 = target - testNum1
            if testNum2 in alist:
                for j in alist:
                    if alist[j] == testNum2:
                        return i, j
            else:
                i += 1
        return False
    else:
        return -1


#alist = dict([(0,0),(1,1),(2,2),(3,3),(4,4),(5,16)])
alist = [0, 1, 2, 3, 4]
#print (alist[6])
print(doesTwoSumExist(12, alist))
#print(doesTwoSumExistIndicies(6, alist))
