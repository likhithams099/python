#slicing a string
text = "Hello Amrita"

# Print first 3 chars. Positions 0..2.
begin = text[0:3]  # 0 is not necessary. It can be just text[:3]
print('First 3 chars =', begin)

# Print last 3 chars. Positions n-3, n-2, n-1
n = len(text)
end = text[n-3:n]  # n is not necessary. It can be just text[n-3:]
print('Last 3 chars =', end)

# Print a range in the middle. Positions 3..6
middle = text[3:7]
print('4 chars in between =', middle)

