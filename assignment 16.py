import sqlite3
conn = sqlite3.connect('TEST50979.db')
print("opened database successfully")


conn.execute('''CREATE TABLE BOOK
           (TITLEID INT  NOT NULL,
            LOCATION  CHAR(50) NOT NULL,
            GENE  REAL);''')
print("table created")


conn.execute('''CREATE TABLE PUBLISHERS
           (PUBLISHERID INT PRIMARY KEY NOT NULL,
            NAME CHAR(50) NOT NULL,
            ZIPCODEID  INT);''')
print("table created")
conn.execute("INSERT INTO BOOK(TITLEID,LOCATION,GENE)\
             VALUES(67,'TRY',0)")
conn.execute("INSERT INTO BOOK(TITLEID,LOCATION,GENE)\
           VALUES(89,'GYU',2000)")
conn.commit()
print("recorded")

cursor=conn.execute("SELECT TITLEID,LOCATION,GENE from BOOK")
for row in cursor:
    print("TITLEID =",row[0])
    print("LOCATION =",row[1])
    print("GENE =", row[2],"\n")
print("successful")
print(cursor)
conn.execute("UPDATE BOOK set GENE = 25000.00 where TITLEID=67")
conn.commit()
print("changes",conn.total_changes)

cursor=conn.execute("SELECT TITLEID,LOCATION,GENE from BOOK")
for row in cursor:
    print("TITLEID =",row[0])
    print("LOCATION =",row[1])
    print("GENE =", row[2],"\n")
print("successful")
print(cursor)


conn.execute("INSERT INTO PUBLISHERS(PUBLISHERID,NAME,ZIPCODEID)\
             VALUES(67,'TRY',0)")
conn.commit()
print("recorded")
cursor=conn.execute("SELECT PUBLISHERID,NAME,ZIPCODEID from PUBLISHERS")
for row in cursor:
    print("TITLEID =",row[0])
    print("LOCATION =",row[1])
    print("GENE =", row[2],"\n")
print("successful")
print(cursor)
conn.execute("UPDATE PUBLISHERS set NAME = 'UFUJ' where PUBLISHERID=67")
conn.commit()
print("changes",conn.total_changes)

cursor=conn.execute("SELECT PUBLISHERID,NAME,ZIPCODEID from PUBLISHERS")
for row in cursor:
    print("TITLEID =",row[0])
    print("LOCATION =",row[1])
    print("GENE =", row[2],"\n")
print("successful")
print(cursor)



conn.close()
