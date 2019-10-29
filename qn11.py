import time
import sqlite3
import random

def execute():
    try:
        conn=sqlite3.connect('event.db')
        curr=conn.cursor()
        
        table="CREATE TABLE FIFA(SCORES FLOAT)"
        curr.execute(table)
        conn.commit()
        
        start=time.time()
        for i in range(100000):
            x=random.uniform(10,30)
            qry="INSERT INTO FIFA VALUES({})".format(x)
            curr.execute(qry)
        conn.commit()
        
        end=time.time()
        req_time=end-start
        print(req_time)
        
    finally:
        curr.close()
        conn.close()
        
def write():
    with open("fifa.txt","w") as f:
        start=time.time()
        for i in range(100000):
            x=random.uniform(10,30)
            stx=str(x)+"\n"
            f.write(stx)
            
        end=time.time()
        req_time=end-start
        print(req_time)
        

execute()
#time = 4.488002777099609
#time = 4.577893495559692
#time = 4.439001560211182
write()
#time = 1.5313129425048828
#time = 1.4686684608459473
#time = 1.453371524810791