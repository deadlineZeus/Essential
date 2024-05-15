f1 = open('C:/Users/Rajdeep Ray/Documents/College Docs/RCB_Scenario.txt', mode='r')
f2 = open('C:/Users/Rajdeep Ray/Documents/College Docs/Paste2.txt', mode='w')


data = f1.readlines()
for i in data:
    print(i, end= '')
    f2.write(i)

f1.close()
f2.close()


