f = open('C:/Users/Rajdeep Ray/Documents/College Docs/promise.txt', mode='r')

no_of_lines = 0
no_of_words = 0
no_of_characters = 0

for line in f:
    no_of_lines += 1
    line = line.strip('\n')
    no_of_characters += len(line)
    word_list = line.split()
    no_of_words = no_of_words + len(word_list)

print('No od lines: ', no_of_lines)
print('No of words: ', no_of_words)
print('No of characters: ', no_of_characters)
