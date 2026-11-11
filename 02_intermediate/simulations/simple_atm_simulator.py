# LESSON: Choose a menu option and check the amount
# This is the starting balance. The program shows a new balance for a
# transaction, but it does not save that new balance for another run.
account_balance = 50000  # Starting balance for the ATM account
transaction_message = None

# The menu is text written across several lines. print() shows it on screen.
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

# input() gives us text for the names. int() changes the menu choice to a whole
# number so it can be checked below. Enter a number for this example.
account_firstname = input("Enter firstname: ") 
account_lastname = input("Enter lastname: ")
account_username = f"{account_firstname} {account_lastname}"
choice = int(input("Enter choice (1-4): "))

# None means no message has been chosen yet. A menu choice will set the message.

# if/elif/else chooses what to do for the menu number. The f-string puts the
# name and balance into the message.
if choice == 1:
    transaction_message = f'''
========================================================
                WELCOME TO PYTHON ATM
=========================================================

Account Name: {account_username} 
Account Balance: ₦{account_balance}

=========================================================
'''

# Ask how much to withdraw. The amount must be above zero and no more than the
# balance in the account.
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
        # Subtract the withdrawal to find the new balance. Save it in another
        # variable so the starting balance stays the same.
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
# Ask how much to deposit. If the amount is above zero, add it to the balance;
# otherwise, show an error message.
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

# Choice 4 prepares a goodbye message. The print() at the end shows it.
elif choice == 4:
    transaction_message =   f'''
========================================================
                        WELCOME TO PYTHON ATM
=========================================================

Thank you {account_username}, for banking with us🤝.
=========================================================
'''

# This else handles a menu number that is not 1, 2, 3, or 4.
else:
    transaction_message =   f'''
========================================================
                WELCOME TO PYTHON ATM
=========================================================
Dear {account_firstname}, Invalid selection. Try 1-4.
        
        Thank you for banking with us🤝.
=========================================================
'''

# Show the message chosen for the menu option.
print(transaction_message)
