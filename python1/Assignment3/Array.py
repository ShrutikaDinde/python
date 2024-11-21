array = [2,4,3,7,'A','B','Z']
print('Array')
print(array)

#SLICING
A = [2.3,1,7,5.5,9]
print('1st element:',A[0])
print('1st element:',A[2])
print('1st element:',A[1])
print('1st element:',A[4])
print(A[2:4])
print(A[:])

print('Length')
print(len(A))
#Changing element of array
print('Changing element')
A[1] = 8
print(A)

#Adding element
print('Print')
A.append(4)
print(A)
print('Extend')
A.extend([0,2])
print(A)

#Count
print('Count')
print(A.count(3))

#Index
print('Index')
print(A.index(2.3))

#Inserting
print('Insertion of element')
A.insert(2,6)
print(A)

#Removing
print('Remove element')
A.remove(5.5)
print(A)

#Reverse
print('Reversed Array')
print(A[::-1])

#POP
print('POP element')
A.pop(2)
print(A)

#Sort
print('Sorted array')
print(sorted(A))
