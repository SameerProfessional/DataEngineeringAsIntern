# Basic File Handling Questions

## Reading a CSV File
- **Task**: Modify the given code to read a CSV file named `data.csv` located in your Desktop folder. What changes would you make?

## Understanding `enumerate()`
- **Question**: What is the purpose of using `enumerate(summaryReader)` instead of a simple `for row in summaryReader` loop?

## Changing the Delimiter
- **Scenario**: If your CSV file uses semicolons (`;`) instead of commas to separate values, how would you modify the `csv.reader` function to correctly read the file?

## Handling Quoted Text
- **Question**: What happens if a CSV file contains commas within quotation marks (e.g., `"Hello, World"`)? How does the `quotechar='"'` argument handle this?

## Skipping the Header Row
- **Task**: Suppose your CSV file contains a header row. How can you modify the code to skip the first row when printing the content?

## Writing to a CSV File
- **Task**: Extend the given code to not only read but also write the data into a new file called `output.csv` using the `csv.writer` module.

## Error Handling
- **Question**: How can you modify the code to catch and handle errors if the CSV file doesn’t exist or can’t be opened?

## Reading Large Files
- **Task**: How can you modify the code to read a large CSV file in chunks instead of loading the entire file into memory at once?

## Appending to a CSV File
- **Task**: Extend the code to append new rows to an existing CSV file instead of overwriting it.

## Using `DictReader` and `DictWriter`
- **Question**: How can you use `csv.DictReader` and `csv.DictWriter` to work with CSV files as dictionaries instead of lists?

## Handling Different Encodings
- **Question**: What changes would you make to handle CSV files with different encodings, such as UTF-8 or ISO-8859-1?

## Sorting CSV Data
- **Task**: Write a code snippet to sort the rows of a CSV file based on a specific column before writing it to a new file.

## Filtering Rows
- **Task**: How can you filter rows based on a condition (e.g., rows where a specific column value is greater than 100) while reading a CSV file?