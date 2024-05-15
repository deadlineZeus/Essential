# if a variable holds collection of strings, then we can write each element in a file
# using writeline() method

f = open('C:/Users/Rajdeep Ray/Documents/College Docs/WriteLines.txt', mode='w')
collection = ['Rajdeep', 'Anubhab', 'Lokesh', 'Sagarika', 'Bijay']

f.writelines(collection)   # will write one each tem after another

f.close()
