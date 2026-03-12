from database import cursor, db

def create_account():
    acc_no = input("Enter Account Number: ")

    cursor.execute("SELECT * FROM accounts WHERE acc_no=%s",(acc_no,))
    if cursor.fetchone():
        print("Account already exists")
        return

    name = input("Enter Name: ")
    balance = int(input("Enter Initial Balance: "))

    cursor.execute("INSERT INTO accounts VALUES(%s,%s,%s)",(acc_no,name,balance))
    db.commit()

    print("Account created successfully")


def deposit():

    acc_no = input("Enter Account Number: ")
    amount = int(input("Enter Amount: "))

    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE acc_no=%s",(amount,acc_no))
    cursor.execute("INSERT INTO transactions(acc_no,type,amount) VALUES(%s,'DEPOSIT',%s)",(acc_no,amount))

    db.commit()

    print("Money deposited")


def withdraw():

    acc_no = input("Enter Account Number: ")

    cursor.execute("SELECT balance FROM accounts WHERE acc_no=%s",(acc_no,))
    data = cursor.fetchone()

    if not data:
        print("Account not found")
        return

    balance = data[0]
    amount = int(input("Enter amount: "))

    if amount > balance:
        print("Insufficient balance")
        return

    cursor.execute("UPDATE accounts SET balance=balance-%s WHERE acc_no=%s",(amount,acc_no))
    cursor.execute("INSERT INTO transactions(acc_no,type,amount) VALUES(%s,'WITHDRAW',%s)",(acc_no,amount))

    db.commit()

    print("Withdrawal successful")


def search_account():

    acc_no = input("Enter account number: ")

    cursor.execute("SELECT * FROM accounts WHERE acc_no=%s",(acc_no,))
    data = cursor.fetchone()

    if data:
        print("Account:",data)
    else:
        print("Account not found")


def check_balance():

    acc_no = input("Enter Account Number: ")

    cursor.execute("SELECT name,balance FROM accounts WHERE acc_no=%s",(acc_no,))
    data = cursor.fetchone()

    if data:
        print("\nAccount Holder:", data[0])
        print("Current Balance:", data[1], "\n")
    else:
        print("Account not found")


def display_accounts():

    cursor.execute("SELECT * FROM accounts")
    data = cursor.fetchall()

    if not data:
        print("No accounts found")
        return

    print("\n----- All Bank Accounts -----")

    for acc in data:
        print("Account No:", acc[0], "| Name:", acc[1], "| Balance:", acc[2])

    print()

def delete_account():

    acc_no = input("Enter account number: ")

    cursor.execute("DELETE FROM accounts WHERE acc_no=%s",(acc_no,))
    db.commit()

    print("Account deleted")


def transaction_history():

    acc_no = input("Enter account number: ")

    cursor.execute("SELECT * FROM transactions WHERE acc_no=%s",(acc_no,))
    data = cursor.fetchall()

    for row in data:
        print(row)