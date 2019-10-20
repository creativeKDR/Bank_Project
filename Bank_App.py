################################ By Creative KDR ##############################################

# pip install mysql
# pip install mysql.connector

import mysql.connector
con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='bank_det')
cur = con.cursor()

class Bank_sys():

    print("Welcome XYZ Bank System......")
    print("Please choose the following Options:......")
    print("1. Account Details")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Change pin")
    print("5. Balance Details")

    ch=int(input("Enter The Option:"))

    def Option(self,a):
        if(a == 1):
            k = int(input("Enter Account Number:"))
            U_pin=int(input("Enter the Pin:"))
            cur.execute("select * from bank_details")
            result = cur.fetchall()
            for row in result:
                Acc_no=row[0]
                pin=row[3]
                if(k==Acc_no and pin==U_pin):
                    print(row)



        elif(a == 2):
            k = int(input("Enter Account Number:"))
            U_pin = int(input("Enter the Pin:"))
            withdraw=int(input("Enter the amount to withdraw:"))
            cur.execute("select * from bank_details")
            result = cur.fetchall()
            for row in result:
                no=row[0]
                mpin=row[3]
                mbal=row[5]
                if (k == no and mpin == U_pin):
                    cum=mbal-withdraw
                    cur.execute("""update bank_details set balance=%s where Acc_no=%s""",(mbal-withdraw,k))
                    con.commit()
                    print("You have Withdraw the amount:",withdraw,",After Your Balance Details:")
                    mbal=cum
                    print(mbal)

        elif (a == 3):
            k = int(input("Enter Account Number:"))
            U_pin = int(input("Enter the Pin:"))
            deposit = int(input("Enter the amount to Deposit:"))
            cur.execute("select * from bank_details")
            result = cur.fetchall()
            for row in result:
                no = row[0]
                mpin = row[3]
                mbal = row[5]
                if (k == no and mpin == U_pin):
                    cum = mbal + deposit
                    cur.execute("""update bank_details set balance=%s where Acc_no=%s""", (mbal + deposit, k))
                    con.commit()
                    print("You have Deposit the amount:", deposit, ",After Your Balance Details:")
                    mbal = cum
                    print(mbal)

        elif (a == 4):
            k = int(input("Enter Account Number:"))
            U_pin = int(input("Enter the Pin:"))
            cur.execute("select * from bank_details")
            result = cur.fetchall()
            for row in result:
                no = row[0]
                mpin = row[3]
                if (k == no and mpin == U_pin):
                    new_pin = int(input("Enter the New Pin:"))
                    cur.execute("""update bank_details set pin=%s where Acc_no=%s""", (new_pin, k))
                    con.commit()
                    print("Your pin has been Succesfully changed")

        elif (a == 5):
            u_acc = int(input("Enter Account Number:"))
            u_pin = int(input("Enter the Pin:"))
            cur.execute("select * from bank_details")
            result = cur.fetchall()
            for row in result:
                acc_no=row[0]
                acc_n=row[1]
                pin = row[3]
                bal=row[5]
                if(acc_no==u_acc and pin==u_pin):
                    print(acc_no,acc_n,bal)

con.commit()
c=Bank_sys()
c.Option(Bank_sys.ch)