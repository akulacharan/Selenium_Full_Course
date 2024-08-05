# insert,  update,  delete

import mysql.connector

insert_query = "insert into Students values(106,'Kim')"
update_query = "update Students set sname='mary' where sid=106"
delete_query = "delete from Students where sid=106"
try:
    con = mysql.connector.connect(
        host="localhost",
        port=143,
        user="charan",
        password="charan",
        database="mydb")   #Connecting with database

    curs = con.cursor()  # Create cursor
    curs.execute(delete_query)  # Ececute query through cursor
    con.commit()   # Commit the transaction means save the transaction
    con.close()
except:
    print('Connection is Unsuccessful')

print('Finished')
