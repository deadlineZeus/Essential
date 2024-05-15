# 'W' mode
#  overrides everything that previously used to exist
# if file does not exist, it creates one. If file exists, it overrides everything
# Write() method returns the number of character it wrote..

f = open('C:/Users/Rajdeep Ray/Documents/College Docs/Demo.txt', mode='w')

n1 = f.write('Abki baar\n')
n2 = f.write("400 paar")
print(n1, n2)
f.close()