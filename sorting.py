# %%

def bubbleSort(alist):
    temp = 0
    
    for i in range(0, len(alist)-1 ,1):
        sortedList = True #Optimizing for exiting out early if sortedList is detected
        for j in range(0, len(alist)-1,1):
            if alist[j] < alist[j+1]:
                None
            else:
                sortedList = False #Optimizing for exiting out early if sortedList is detected

                temp = alist[j+1]
                alist[j+1] = alist[j]
                alist[j] = temp
        
        if sortedList: #Optimizing for exiting out early if sortedList is detected
            return alist

    return alist

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2

        L = alist[:mid]
        R = alist[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                alist[k] = L[i]
                i+= 1
            else:
                alist[k] = R[j]
                j+=1
            k+=1
        
        while i < len(L):
            alist[k] = L[i]
            i+=1
            k+=1

        while j< len(R):
            alist[k] = R[j]
            j+=1
            k+=1
        
        return alist

def selectionSort(alist):

    for i in range(0, len(alist)-1, 1):
        location = 0
        currentBiggest = alist[0] 
        for j in range(1, len(alist)-1-i, 1):
            #get the location of the biggest int
            if alist[j] > currentBiggest:
                location = j
                currentBiggest = alist[j]
        
        # if (i == len(alist)-2):
        #     print(i)
        if alist[len(alist)-1-i] < alist[location]:    
            alist[location] = alist[len(alist)-1-i]
            alist[len(alist)-1-i] = currentBiggest
    #insert it into the final location
    return alist

def insertionSort(alist):
    for i in range(1, len(alist),1):
        position = i

        # print("Run #: ",i)
        # print (alist[position])
        # print (alist[position-1])

        # if i == 7:
        #     print(i)

        while alist[position] < alist[position - 1] and position > 0:
            temp = alist[position]
            alist[position] = alist[position-1]
            alist[position - 1] = temp

            position = position - 1

    return alist





def quickSort(alist):
    low = 0
    high = len(alist)-1

    if low < high:
        pi = partition(alist)

        quickSort(alist[:pi])
        quickSort(alist[pi:])


alist = [54,26,93,17,77,31,44,55,20]
#alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]
#alist = [54,26,93]
#print (bubbleSort(alist))
#print (selectionSort(alist))
#print (insertionSort(alist))

print(mergeSort(alist))
# %%
