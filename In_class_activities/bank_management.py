account = {}

def create_account():
    print("Create a new account")
    account_number = input("Enter account number: ")

    if account_number in account:
        print ("Account alrdeay exists.")
        return
    name = input("Enter account holder name:")
    phone = input("Enter phone number:")
    initial_deposit = float(input("Enter initial deposit amount:"))

    if initial_deposit < 0:
        print("Initial deposit cannot be negative.")
        return
    account[account_number]= {
        "name": name,
        "phone": phone,
        "balance": initial_deposit,
        "transactions": []
    }

    account[account_number]["transactions"].append(f"Account created with initial deposit of {initial_deposit}")
    print("Account created successfully!")
    print(f"Account Number: {account_number}")


    def view_accounts():
        print("!Account Details!")
        account_number = inputt("Enter account number to view details: ")

        if account_number in account:
            print(f"Account number not found!")
            return
        
        account_details = account[account_number]
        print("Account Number:", account_number)
        print("Account Holder:", account_details["name"])
        print("Phone Number:", account_details["phone"])
        print("Balance:", account_details["balance"])

def deposit_money():
    print("!Deposit Money!")
    account_number = input("Enter account number:")

    if account_number not in account:
        print("Account number not found!")
        return
    amount = float(input("Enter an amount to deposit- "))

    if amount <=0:
        print("Deposit amount must be greater than zero!!")
        return
    
    account[account_number]["balance"] += amount
    account[account_number]["transactions"].append(f"Deposited {amount}")

    print(f"Deposited {amount} successfully! New Balance: {account[account_number]["balance"]}")
    


def main():
    while True:
        print("Welcome to the Bank Management System")
        print("1. Create Account")
        print("2. View all accounts")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")   
        print("6. Transfer Money")
        print("7. Transaction History")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            withdraw_money()
        elif choice == "5":
            check_balance()
        elif choice == "6":
            transfer_money()
        elif choice == "7":
            transaction_history()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()





