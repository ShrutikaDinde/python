#write
f1=open("File.txt",'w')
f1.write("Hello,Python")

#read
f1=open("File.txt",'r')
print(f1.read())

#append
f1=open("File.txt",'a')
f1.write("\nMy Name is Shravani")
f1=open("File.txt",'r')
print(f1.read())

#binary read
print('\n')
f1=open("File.txt",'rb')
binary_read=f1.read()
print(binary_read)


f1=open("File.txt",'rt')
content=f1.read()
print(content)

#read 10 bytes
with open("File.txt",'r')as file:
    content=file.read(10)
    print("\nRead 10 bytes")
    print(content)

'''#write some data into file
with open("File.txt",'w')as file:
    file.write("Heyy Guys")'''

#Appending to the file
with open("File.txt",'a')as file:
    file.write("\n I am from Kolhapur\n")
    print("Data is appended to the file")

#read a sigle line
with open("File.txt",'r')as file:
    line=file.readline()
    print("\nread Single line")
    print(line)    

#read all lines
with open("File.txt",'r')as file:
    lines=file.readlines()
    print("\nread all line")
    print(lines)    

#read the file line by line
print("\nRead file line by line")
with open("File.txt",'r')as file:
    for line in file:
      print("line =",line)
      

#seek function
with open("File.txt",'r')as file:
    file.seek(5)
    content=file.read()
    print(content)

#tell() Function
with open("File.txt",'r')as file:
    print(file.tell())
    file.read(10)
    print(file.tell())