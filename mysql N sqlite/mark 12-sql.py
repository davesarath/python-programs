import sqlite3
con =sqlite3.connect("manbat.db")
# con.execute("drop student")
try:
    con.execute("create table stu(name char,roll int(2),department char)")
except(sqlite3.OperationalError):
    print("already table exist")

# con.execute("create table stu(name char,roll int(2),department char)")

con.execute("insert into student values(?,?,?)",(input("name:"),input("roll numbr:"),input("dartmnt:")))
con.commit()
curse = con.execute("select * from student")
for i in curse:
    print("name:",i[0])
    print("roll number:",i[1])
    print("deprtmnt:",i[2])


con.close()

