# Combine 2 sorted list into 1

def combinedLst(array1,array2):
    
    result = []
    i, j = 0 , 0

    while(1):
        if i == len(array1):
            result.extend(array2[j:])
            break
        elif j == len(array2):
            result.extend(array1[i:])
            break
        else:
            if array1[i]<array2[j]:
                result.append(array1[i])
                i = i +1
            else:
                result.append(array2[j])
                j = j + 1

    return result


# find pair of integers from list which add up to k

def findpair(array,k):
    pairs = []
    for i in range(len(array)):
        if k - array[i] > 0:
            ele = k - array[i]
            if ele in array:
                if not ele in list(map(lambda x: x[0],pairs)):
                    pairs.append((array[i],ele))
    
    return pairs

array = [1, 2, 3, 4, 5, 6, 5, 5]

findpair(array,10)