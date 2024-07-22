import mysql connector.connect

conn = mysql connector.connect(host='localhost',
                               user='root',
                               password='')
cur=conn.cursor()
cur.execute("create database employee")
conn.commit()
conn.close()


conn = mysql connector.connect(host='localhost',
                               user='root',
                               password='',
                               database='employee')
cur=conn.cursor()
q1 = "CREATE TABLE emp(id INTEGER PRIMARY KEY,name TEXT NOT NULL,age INTEGER  ,position TEXT)"
cur.execute(q1)
conn.commit()
conn.close()



conn = mysql connector.connect(host='localhost',
                               user='root',
                               password='',
                               database='employee')
cur=conn.cursor()
q1 =  "INSERT INTO emp VALUES(1,'raj',12,'ceo');"
q1 =  "INSERT INTO emp VALUES(1,'raj',12,'ceo');"
q1 =  "INSERT INTO emp VALUES(1,'raj',12,'ceo');"
q1 =  "INSERT INTO emp VALUES(1,'raj',12,'ceo');"
q1 =  "INSERT INTO emp VALUES(1,'raj',12,'ceo');"
cur.execute(q1)
cur.execute(q2)
cur.execute(q3)
cur.execute(q4)
cur.execute(q5)


conn = mysql connector.connect(host='localhost',
                               user='root',
                               password='',
                               database='employee')
cur=conn.cursor()
id =  int(input("Enter id u want to delete : "))
q1 = "delete from emp where id={}".format(id)
cur.execute(q1)
conn.commit()
conn.close()


conn = mysql connector.connect(host='localhost',
                               user='root',
                               password='',
                               database='employee')
cur=conn.cursor()
id =  int(input("Enter id u want to update : "))
name = input("Enter name : ")
age =  int(input("Enter age : "))
position = input("Enter position : ")
q1 = "UPDATE emp set name='{}',age={},position='{}' where id={}".format(name,age,position,id)
cur.execute(q1)
conn.commit()
conn.close()
















