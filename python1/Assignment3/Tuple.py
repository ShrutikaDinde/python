Elements = ('Python','Shravani','Mango','Banana','India')
print(Elements)
print(Elements[1])
print(Elements[2])
#Iterate through a Tuple
print('\n')
for Element in Elements:
    print(Element)

print('Length of Tuple:')
print(len(Elements))

print('\n')
print('Slicing')
T = (1,2,3,4,5,6)
print(T[2:4])

print('Multiplication')
print(T*3)

print('Concatination')
T1 =(3,2,1,4)
T2 =('A','B','C')
T3 =T1+T2
print(T3)

print('Minimum')
print(min(T1))
print('Maximum')
print(max(T1))

print('Sum')
print(sum(T1))

print('Sort')
print(sorted(T1))
print('\n')
Tuple = ('SHRAVANI')
print(Tuple)

#Removing element
print('Remove first element')
print(Tuple[1:])

#REverse the string
print('Reversed string')
print(Tuple[::-1])
