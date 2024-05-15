import csv
# Way-1:  in the form of List
# with open("C:/Users/Rajdeep Ray/Documents/College Docs/Titanic.csv", 'r') as f:
#     titanic_data = csv.reader(f, delimiter=',')
#     print(titanic_data )
#
#     for rec in titanic_data:
#         print(rec)   # prints every line as a list

# Way-2:  in the form of Dictionary

with open("C:/Users/Rajdeep Ray/Documents/College Docs/Titanic.csv", 'r') as f:
    csv.register_dialect('normal_dialect', delimiter=",", quotechar='"')
    titanic_data = csv.DictReader(f, delimiter=',')
    print(titanic_data )

    for rec in titanic_data:
        print(rec)   # prints every line as a Dictionary