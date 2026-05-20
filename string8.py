# check all char are same
text = input()
n = len(text)
result = 'All chars are same'
for i in range(n-1) :  # Why n-1? Can you guess?
  if text[i] != text[i+1] :
    result = 'All chars not same'
    break
print(result)