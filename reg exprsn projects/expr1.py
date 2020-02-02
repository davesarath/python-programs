import re

str = "The rain in Spain aran"

#Return a match at every NON white-space character:

x = re.findall(" r\S+", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())
k=x

print(k)