# Read values from a CSV file line-by-line and print row numbers using enumerate().
# (Use Python's csv module and enumerate())

import csv # Imports the csv module to use it's reader function

with open(r'C:\Users\singh\Documents\DataEngineeringAsIntern\DataEngineeringAsIntern\DAY1\CSVFiles\summaryFile.csv', newline='') as csvfile:
    summaryReader = csv.reader(csvfile, delimiter=',', quotechar='"')

    for index, row in enumerate(summaryReader):
        print(f"Row number {index+1} :", row)




