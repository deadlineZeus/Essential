import csv

#file = input("Enter file location: ")
def check_csv(file):
    with open(file) as f:
        data = csv.reader(f, delimiter=",")    # header is an iterator object
        header = next(data)
        no_of_columns = len(header)  # no of columns

        for rec in data:
            if len(rec) != no_of_columns:
                return False
        return True




result = check_csv("C:/Users/Rajdeep Ray/Documents/College Docs/cities.csv")
if result==True:
    print("Valid CSV file")
else:
    print("Invalid CSV file")