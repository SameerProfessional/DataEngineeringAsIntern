# - Read a CSV file named data.csv located in your Desktop folder. What changes would you make?

import csv

# Writing to a CSV file (append mode)
with open(r'C:\Users\singh\Desktop\Data.csv', mode='w', newline='') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=',',quotechar='"')
    csvWriter.writerow(["Conclusion:The CSV module's reader and writer objects along with the DictReader and DictWriter classes provide Python developers with flexible and powerful tools for handling CSV data efficiently, whether in a list or dictionary format"]) 
    # writerow() takes a list or tuple, not a string.
    # Passing a long string to writerow() causes each character to be treated as a separate column. 
    csvWriter.writerow(["This makes it easy to integrate CSV file processing into a wide range of applications, contributing to data interchange and analysis tasks."])

with open(r'C:\Users\singh\Desktop\Data.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvReader:
        print(row)
    
