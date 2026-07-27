'''
This is simple banking app which will have below options
1. Check balance
2. Deposit balance
3. Withdraw balance
4. Check KYC
5. Update KYC
6. Quit
'''
balance = 0.0
kyc_documents = {}

def check_balance():
    print(f"Current Balance: {balance}")
    print("===========================")

def deposit(amount):
    global balance
    if amount <= 0:
        print(f'Deposit operation failed. You can\'t deposit amount less then or equal to 0')
        print("============================================================================")
    else:
        balance += amount
        print(f'Deposit Success!!!')
        print("===================")
        print(f'Previous balance: {balance - amount}')
        print(f'Deposit amount: {amount}')
        print(f'Updated balance: {balance}')
        print("===========================")

def withdraw(amount):
    global balance
    if balance < amount:
        print(f'Your balance({balance}) is below then the withdrawal amount({amount})')
        print("======================================================================")
    elif amount <= 0:
        print(f'You can\'t withdraw negative or 0 amount')
        print("=========================================")
    else:
        balance -= amount
        print(f'Withdrawal Success!!!')
        print("======================")
        print(f'Previous balance: {balance + amount}')
        print(f'Withdrawal amount: {amount}')
        print(f'Updated balance: {balance}')
        print("===========================")

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done, use the Update KYC option on main menu to update your KYC!!!")
        print("==========================================================================")
    else:
        print("=========================================")
        for docs in kyc_documents:
            print(f'{docs}: {kyc_documents[docs]}')
        print("=========================================")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)
    print("Kyc Updated!!!")
    print("==============")

if __name__ == "__main__":

    print("===================")
    print("Welcome to ABC Bank")
    print("===================")
    print()
    while True:
        print("1. Check your Balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
        choice = input("Enter your choice (1-4): ")
        print("==================================")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount you want to deposit: "))
            deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount you want to withdraw: "))
            withdraw(amount)
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            docs = {}
            n_documents = int(input("Enter the number of documents you want to enter: "))
            for i in range(n_documents):
                key = input("Enter the document type: ")
                value = input("Enter a document number: ")
                docs[key] = value
            update_kyc(docs)
        elif choice == '6':
            print("Quitting, have a nice day!!")
            break
        else:
            print("Invalid choice!!! Retry.")
            print("========================")

    print("Thank you for banking with us!!!")
    print("================================")
