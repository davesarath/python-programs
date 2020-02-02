import re
a = "text dvHsg ASD 12345 Sarath 155 4545 Sv84vd454 99 88 199 2222 As/ 1 Sv65464sv sajasvd@quest.com sdugfa euyf ugyf5 fg1"
# a = raw_input("Enter your text:")
maile = re.findall(r'\S+@\S+',a)
# nam = re.findall(r'\b[A-Z][^0-9]+',a)
nam = re.findall(r'\b[A-Z][^0-9]+[^0-9]\b',a)
# aa = ' '.join(nam)
# numbr = re.findall(r'[0-9]+',a)
numb = re.findall(r'\b[0-9][0-9]+[0-9]\b|\b[0-9][0-9]\b',a)

#numbr = re.findall(r'[0-9]{4,6}',a)

print "mail ids:", maile

print "names:",nam
# print aa
# print "numbers",numbr
print "numbers:",numb