f1 = open('C:/Users/Rajdeep Ray/Documents/College Docs/promise.txt', mode='r')
x1 = f1.read()
print(x1)
f1.close()

print("################################################################################")

f2 = open('C:/Users/Rajdeep Ray/Documents/College Docs/promise.txt', mode='rb')
x2 = f2.read()  # if we do not give any arguement to read() method, it reads the whole file as string
print(x2)
f2.close()

print("################################################################################")

f3 = open('C:/Users/Rajdeep Ray/Documents/College Docs/promise.txt', mode='r')
x3 = f3.read(20) # read method takes an optional agruement to specify no of characters we want to read
print(x3)        # (Hi there \r\nI am a soft)

x4 = f3.read(10) # read method takes an optional agruement to specify no of characters we want to read
print(x4)   # reads the next 10 characters starting from where we left last time (ware engin)

f3.close()