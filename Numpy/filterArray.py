import numpy as np
# arr = np.array([1, 2, 3, 7 , 8])
# filter =[True,False]

# newarr = arr[filter]
# print(newarr)
x = np.random.randint(1,100,size=10)
arr = np.array(x)
# print(arr)

#defining filter

filter_ar=[]

for x in arr:
    if x>45:
        filter_ar.append(True)
    else:
        filter_ar.append(False)

# print(filter_ar)

# print(arr[filter_ar])


#Filtering Even Number

def Even(array):
    fil=[]
    for x in array:
        if x%2==0:
            fil.append(True)
        else:
            fil.append(False)
    
    return array[fil]

# x = Even(arr)
# print(arr)
# print(x)

#Direct Filter
print(arr)

filter = arr%2==0
print(filter)
print(arr[filter])