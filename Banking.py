# Banking Management

print("********************************")
print("Banking Management")
print("********************************")

import re
class account():
    def __init__(self, name, email, cnic):
        self.name = name
        self.email = email
        self.cnic = cnic

# print("Name Validation for new Accounts")

name = str (input(("Enter your name : ")))
if (name.isalpha() and len(name) > 2 and len(name) <= 17):
    print("Valid name")
else:
    print("Invalid Name")
print(name)

# print("Email Validation for new Accounts")

def is_valid_email(email):
    return re.match(email_pattern, email) 
email = input(("Enter your email : "))
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if(is_valid_email(email)):
    print("Valid Email")
else:
    print("Email is not valid : Try Again")
  
# print("CNIC Validation for new Accounts")

def is_valid_cnic(cnic):
    cnic_pattern = r'^\d{5}-\d{7}-\d{1}$'
    return re.match(cnic_pattern, cnic)

cnic = str (input("Enter your cnic : "))
if((is_valid_cnic(cnic))):
    print("Valid cnic")
else:
    print("Invalid cnic")
    
class account_no():
    def __init__(self, account_no):
        self.account_no = account_no
        account_no = int (input("Enter your Account number : ")) 
        print(account_no)
        def validate_account_number(account_no):
            pattern = r'^\d{16}$'
            if re.match(pattern , account_no):
                print("Valid Account Number : ")
            else:
                print("Not Valid : ")     
account_no = str (input("Enter your Account number : "))
  
    
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        amount = int (input("Enter your deposit amount : "))
        print (amount)
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.balance
    
account = BankAccount("12345678910123456", "Hasssan", 500)
account.deposit(0)  
print(f"Current balance: ${account.get_balance()}")  

