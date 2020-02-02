import os 
print(os.name)

import os
print(os.getcwd())
# To print absolute path on your system
print(os.path.abspath('.'))

# To print files and directories in the current directory
# on your system
print(os.listdir('.'))

fd = "GFG.txt"
file = open(fd, 'w')
text = file.write(" ")
print(text)
file.close()

fd = "stud.txt"
file = open(fd, 'r')
text = file.read()
print(text)
file.close()


# file rename
fd = "GFG.txt"
# os.rename(fd,'New.txt')
os.uname()
print(os.uname())


