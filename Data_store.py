################################ By Creative KDR ##############################################

import mysql.connector
con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='bank_det') # change the database name as per your database
cur = con.cursor()

# For creating tables in data base
cur.execute("create table bank_details (Acc_no int, Acc_name varchar(20), Acc_type varchar(10), pin int,""addr varchar(15))")

# Once your table is created then you can comment above line code and then run below line code.

# For inserting values in data base
cur.execute("insert into bank_details values(0101,'XYZ','Current',2020,'Thane')")

# Once your table is created then you can comment above line code and then run below line code.

# If you want to add and update the table you can run following code or command

# For Adding New Collumn in Table
cur.execute("alter table bank_details ADD Balance float ")
# For Updating Values in Table Database
cur.execute("update bank_details set balance = 42500 where Acc_no = 2345")


#Use the query for the making database
con.commit()