# insert,  update,  delete

import mysql.connector


try:
    con = mysql.connector.connect(
        host="localhost",
        port=143,
        user="charan",
        password="charan",
        database="mydb")   #Connecting with database

    curs = con.cursor()  # Create cursor
    curs.execute("select * from Students")  # Ececute query through cursor

    for row in curs:
        print(row[0],row[1])

    con.commit()   # Commit the transaction means save the transaction
    con.close()    # Close the connection
except:
    print('Connection is Unsuccessful')

print('Finished')
