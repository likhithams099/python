text = "My_Name_is_Likhitha"

# Print first 3 chars. Positions 0..2.
begin = text[:5]  # 0 is not necessary. It can be just text[:3]
print('First 6 chars =', begin)

# Print last 3 chars. Positions n-3, n-2, n-1
n = len(text)
end = text[-7]  # n is not necessary. It can be just text[n-3:]
print('Last 7 chars =', end)

# Print a range in the middle. Positions 3..6
middle = text[5:-7]
print('8 chars in between =', middle)

