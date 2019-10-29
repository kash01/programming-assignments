import pymysql as mysql

try:
    db= mysql.connect("localhost","root","","dbms2018")
    cu=db.cursor()
    
    table="""CREATE TABLE STUDENT(ROLL_NO INT(4) PRIMARY KEY,NAME VARCHAR(20) NOT NULL,ATTENDANCE FLOAT NOT NULL,MARKS INT(3) NOT NULL)"""
    cu.execute(table)
    db.commit()
    
    print("Insert Operation\n")
    n=int(input("Enter number of entries"))
    for i in range(n):
        roll_no=int(input("Enter roll number: "))
        name=input("Enter student name: ")
        attendance=float(input("Enter attendance: "))
        marks=int(input("Enter marks: "))
        sql="""INSERT INTO STUDENT VALUES({},"{}",{},{})""".format(roll_no,name,attendance,marks)
        cu.execute(sql)
        db.commit()
    
    cu.execute("SELECT * FROM STUDENT GROUP BY ROLL_NO ASC")
    data=cu.fetchall()
    for i in data:
        print("%-6d %-10s %5.2f %-15d"%i)

    print("\nUpdate Operation\n")  
    qry="""UPDATE STUDENT SET NAME='Shivam' WHERE ROLL_NO=8440"""
    cu.execute(qry)
    db.commit
    cu.execute("SELECT * FROM STUDENT GROUP BY ROLL_NO ASC")
    data=cu.fetchall()
    for i in data:
        print("%-6d %-10s %5.2f %-15d"%i)
    
    print("\nDelete Operation\n\n")
    qry2="""DELETE FROM STUDENT WHERE ROLL_NO=8440"""
    cu.execute(qry2)
    db.commit()
    cu.execute("SELECT * FROM STUDENT GROUP BY ROLL_NO ASC")
    data=cu.fetchall()
    for i in data:
        print("%-6d %-10s %5.2f %-15d"%i)
        
finally:
    if(db.open):
       cu.close()
       db.close()