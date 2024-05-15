f = open('C:/Users/Rajdeep Ray/Documents/College Docs/promise.txt', mode='r')

print(f.tell())    # tell() returns the current position of the file pointer curser which is 0 as of now

s1 = f.read(8)
print(s1)
print(f.tell())    # now the curser has crossed 8 characters, so the current position is 8

s2 = f.read(9)     #  now the curser has crossed 9 characters, so the current position is 8 + 9 = 17
print(s2)
print(f.tell())

print('####################################################')
f.seek(0)
s3 = f.read(20)
print(s3)     # should start reading from the begining and print first 20 characters
print(f.tell())
print('####################################################')
f.seek(3)     # again the curser is rearragned to position 3
s4 = f.read(10)    # reads character from 3-13
print(s4)
print(f.tell())

f.close()
