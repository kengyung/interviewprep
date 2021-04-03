#Given a target integer and an array of numbers, return if there exists a combination the sums to the target integer (i.e: true/false)
#challenge: return instead, the indices of two numbers that sum to that amount 
def doesTwoSumExist(target, alist):
    if len(alist) > 1: #Checks if alist is at least 2 numbers
        i = 0
        while i < len(alist): 
            testNum1 = alist[i]
            testNum2 = target - testNum1
            if testNum2 in alist:
                return True
            else:
                i+= 1
        return False
    else:
        return -1



alist = dict([(0,0),(1,1),(2,2),(3,3),(4,4),(5,16)])

#print (alist[6])
print(doesTwoSumExist(12,alist))