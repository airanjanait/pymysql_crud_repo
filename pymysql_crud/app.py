import pymysql
import sys
try:
    connection=pymysql.connect(host='localhost',user='root',password='',database='company')
except:
    print("error")                               
    sys.exit()
    
#________________creating table "flipkart" ___________________

with connection.cursor() as cur:
    sql="create table flipkart(id int(12),name varchar(12), description varchar(223),quantity int(12),brand varchar(123))"
    cur.execute(sql)
    connection.commit()
    print("create table")
    
#_______________ data insert into flipkart____________________

with connection.cursor() as cur:
    sql="insert into flipkart (id,name,description,quantity,brand) values(%s,%s,%s,%s,%s)"
    values=(2,'jeans','new brand of jeans is here',233,'zara')
    cur.execute(sql,values)
    connection.commit()
    print("data inserted")


#________________ fetching data from flipkart table___________________
    
with connection.cursor() as cur:
    sql="select * from flipkart"
    cur.execute(sql)
    a=cur.fetchall()
    for r in a:
        print(r)
        
#_______________ update data of table flipkart_______________

with connection.cursor() as cur:
    sql="update flipkart set brand='ranjana' where id=1"
    cur.execute(sql)
    connection.commit()
    connection.rollback
    print("done||||")
    
#_______________ deleting data from flipkart table______________

with connection.cursor() as cur:
    sql="delete from flipkart where id=2"
    cur.execute(sql)
    connection.commit()
    print("data deleted")




