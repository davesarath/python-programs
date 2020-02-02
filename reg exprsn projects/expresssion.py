import re
a = "text dvsg ASD Sarath sdugfa euyf ugyf5 fg1"
ab=re.findall('[A-Z][a-zA-Z]*',a)
print(ab)
