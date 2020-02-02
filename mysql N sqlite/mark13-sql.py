import mysql.connector
con= mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="hellbat")
cur=con.cursor()

try:
    s="create table stut(name varchar(10),roll int(2),department varchar(10))"
    cur.execute(s)
except(mysql.connector.errors.ProgrammingError):
    print("already table exist")


# nam=str(input("name:"))
# ag=input("age:")
# drt=str(input("department:"))

# s="insert into student values(?,?,?)",input("name:"),input("roll numbr:"),input("dartmnt:")
#
# s="insert into stut(name,roll,department) values('dsl',12,'ec')"
# cur.execute(s)


s="select * from stut"
cur.execute(s)
a=cur.fetchall()
for i in a:
    print("name:",i[0])
    print("Roll number:",i[1])
    print("department:",i[2])
    # print("year:",i[3],"\n")

# s="delete from stut where name='dsl'"
# cur.execute(s)

print("hahaha\n")
s="select * from stut"
cur.execute(s)
a=cur.fetchall()
for i in a:
    print("name:",i[0])
    print("Roll number:",i[1])
    print("department:",i[2])
    # print("year:",i[3],"\n")

# s="alter table stut add year int"
# cur.execute(s)
# s="update stut set year=2018 where name='dsl'"
# cur.execute(s)

# s="alter table stut drop year"
# cur.execute(s)

s="select * from stut"
cur.execute(s)
a=cur.fetchall()
for i in a:
    print("name:",i[0])
    print("Roll number:",i[1])
    print("department:",i[2])
    print("year:",i[3],"\n")

con.commit()
con.close()

