# READINE function
f1 = open('C:/Users/Rajdeep Ray/Documents/College Docs/promise.txt', mode='r')
x1 = f1.readline()    # readline method reads line by line
x2 = f1.readline()    # 1st readline reads 1st line, 2ns readline method reads 2nd line
x3 = f1.readline(8)   # if we specify a number, it reads only those many characters
print(x1)  # should contain entire 1st line
print(x2)  # should contain entire 2nd line
print(x3)  # should contain initial 8 characters of 3rd line
f1.close()

print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
# READLINES function
f2 = open('C:/Users/Rajdeep Ray/Documents/College Docs/promise.txt', mode='r')
y1 = f2.readlines()   # returns a list of each lines
print(y1)
print(y1[1])