str = 'Sameer'

print(str[0:2])  # Output: Sa
print(str[2:4])  # Output: me
print(str[:-1]) # Output: Samee

# The slice notation str[start:end] extracts a substring from the string str, starting at index start and ending at index end - 1.
# Slice syntax :- str[start:end:step]
# The step parameter is optional and specifies the increment between each index in the slice. If not provided, it defaults to 1.

# Example:
print(str[0:5:2])  # Output: Sme
print(str[::2])  # Output: Sme
print(str[::-1])  # Output: reemaS (Reverses the string)
print(str[1:5:2])  # Output: ae
print(str[1:5])
print(str[1::-1])  # Output: aS (Reverses the string from index 1 to 0)
print(str[1:5:-1])  # Output: '' (Empty string, because the start index is greater than the end index with a negative step)

# start: The index where slicing begins.
# end: The index before which slicing stops (not included).
# step: The direction & interval (positive for left-to-right, negative for right-to-left).

# Issue:
# Slicing moves backward due to -1, but start (1) is before end (5) in normal order.
# Python expects start > end for negative steps to work, but here it's start < end, which is invalid.
# Result: Since Python can't process this direction mismatch, it returns an empty string ('').

print(str[5:0:-1]) # Output: reemaS (Reverses the string from index 5 to 1)
print(str[5:0:-2]) # Output: rea (Reverses the string from index 5 to 1 with a step of -2)


# 🔹 Quick Rule to Remember
# ✅ For Positive Step (step > 0) → start < end
# ✅ For Negative Step (step < 0) → start > end

# If start < end and step < 0, Python returns an empty string.

