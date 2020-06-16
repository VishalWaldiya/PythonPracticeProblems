array = [54,21,45,77,32,45]

n = last = len(array) -1

print("Array before sorting {}".format(array))
for i in range(0,n):
    print("Iteration {} \n".format(i+1))
    print("Currently array is like  {}".format(array))
    print("Last : {}".format(last))
    first_ele = array.pop(0)
    print("printing after pop array {}".format(array))
    array.insert(last,first_ele)
    print("after inserting array    {}".format(array))
    last = last -1
    print("********************************************\n\n")

print("Array after sorting {}".format(array))
