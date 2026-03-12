from bank_operations import *

def login():

    username = input("Enter username: ")
    password = input("Enter password: ")

    from database import cursor

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))

    if cursor.fetchone():
        return True
    else:
        return False


print("===== BANK MANAGEMENT SYSTEM =====")

if login():

    while True:

        print("""
1 Create Account
2 Deposit Money
3 Withdraw Money
4 Search Account
5 Check Balance
6 Display All Accounts              
7 Delete Account
8 Transaction History
9 Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            search_account()

        elif choice == "5":
            check_balance()
        
        elif choice == "6":
            display_accounts()

        elif choice == "7":
            delete_account()

        elif choice == "8":
            transaction_history()

        elif choice == "9":
            break

        else:
            print("Invalid choice")

else:
    print("Invalid login")