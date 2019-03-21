import re


txt = "67"
x = re.search("(\d{1,2})" ,txt)

print(x)

if (x):
  print("YES! We have a match!")
else:
  print("No match")
