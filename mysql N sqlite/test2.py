import mysql.connector
con= mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="testdb")
cur=con.cursor()

try:
    cur.execute("CREATE DATABASE testdb")
except:
    print("db exist")
try:
    s="create table stud(name varchar(20),dartmnt varchar(2),year int(4))"
    cur.execute(s)
except:
    print("table exist")

s="select * from stud"
cur.execute(s)
a=cur.fetchall()
print(a)

# nam=str(input("name:"))
# drt=str(input("dartmnt:"))
# yr=int(input("year:"))
# s="insert into stud(name,dartmnt,year) values('nam',drt,yr)"
#
s="insert into stud values(%s,%s,%d)",str(input("name:")),str(input("dartmnt:")),int(input("year:"))
#
#
print(s)
cur.execute(s)


s="select * from studnt"
cur.execute(s)
a=cur.fetchall()
print(a)
