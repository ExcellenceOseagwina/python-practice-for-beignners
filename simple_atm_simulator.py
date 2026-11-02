account_balance = 50000  # Starting balance for the ATM account
transaction_message = None

# Display the available ATM options.
print("""
==============================
    WELCOME TO PYTHON ATM
==============================
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit
==============================
""")

# Collect the account holder's name and selected menu option.
account_firstname = input("Enter firstname: ") 
account_lastname = input("Enter lastname: ")
account_username = f"{account_firstname} {account_lastname}"
choice = int(input("Enter choice (1-4): "))

# Prepare a response for the selected transaction.

# Prepare the account balance inquiry response.
if choice == 1:
    transaction_message = f'''
========================================================
                WELCOME TO PYTHON ATM
=========================================================

Account Name: {account_username} 
Account Balance: ₦{account_balance}

=========================================================
'''

# Handle a withdrawal request.
elif choice == 2:
    transaction_message = f'''
========================================================
                WELCOME TO PYTHON ATM
========================================================

2. Withdraw Money ✅...............

=========================================================
'''
    print(transaction_message)
    withdraw_money = int(input("Enter the amount you want to withdraw: "))

    if withdraw_money <= account_balance and withdraw_money > 0:
        transaction = account_balance - withdraw_money
        transaction_message = f'''
========================================================
                WELCOME TO PYTHON ATM
=========================================================
Account Name: {account_username} 
Amount Withdrawn: ₦{withdraw_money} 
Current Account Balance: ₦{transaction}
        
        Thank you for banking with us🤝.
=========================================================
'''
# Report an error when the withdrawal exceeds the available balance.
    else:
         transaction_message = f'''
========================================================
              WELCOME TO PYTHON ATM
=========================================================
Dear {account_username}, your transaction could not be completed due to insufficient funds. 
Try again or deposit money.
Attempted Amount For Withdrawal: {withdraw_money} 
Current Account Balance: ₦{account_balance}
                
                Thank you for banking with us🤝.
=========================================================
 
'''
# Handle a deposit request.
elif choice == 3:
    transaction_message = f'''
========================================================
                WELCOME TO PYTHON ATM
========================================================

3. Deposit Money ✅.............

=========================================================
'''
    deposit_money = int(input("Enter amount to be deposited: "))
    if deposit_money > 0:
            deposit_balance = deposit_money + account_balance
            transaction_message = f'''
========================================================
                WELCOME TO PYTHON ATM
=========================================================
Name: {account_username}
Amount Deposited: {deposit_money}
You deposited ₦{deposit_money}
Current Account Balance: ₦{deposit_balance}
                        
                Thank you for banking with us🤝.
=========================================================
'''

# Report an error when the deposit amount is zero or negative.
    else:
        transaction_message =  f'''
========================================================
                WELCOME TO PYTHON ATM
=========================================================
        Error⚠️, You tried depositing ₦{deposit_money}.
        Your current account balance is ₦{account_balance}
        Thank you for banking with us🤝.
=========================================================
'''

# Prepare the message for exiting the ATM.
elif choice == 4:
    transaction_message =   f'''
========================================================
                        WELCOME TO PYTHON ATM
=========================================================

Thank you {account_username}, for banking with us🤝.
=========================================================
'''

# Handle a menu choice outside the available options.
else:
    transaction_message =   f'''
========================================================
                WELCOME TO PYTHON ATM
=========================================================
Dear {account_firstname}, Invalid selection. Try 1-4.
        
        Thank you for banking with us🤝.
=========================================================
'''

# Display the response for the selected transaction.
print(transaction_message)