import re

str = "sadsa@ggg.com alls mainly aix  aixxx aixx aixxxx in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:
reg="[a-z0-9]+@[a-z]+\.[a-z]+"
x = re.findall(reg, str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
