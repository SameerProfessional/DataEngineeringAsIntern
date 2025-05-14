#  Read a large CSV file and stop at the 100th row, printing its contents

import csv

with open('/c/Users/singh/Desktop/File.csv', mode='w', newline='') as csvfile:
    text = input("Enter the string: ")
    csvReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(csvReader):
        if i == 100:  # Stop at the 100th row (index 99)
            print(row)
            break
        