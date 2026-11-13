import json
from pathlib import Path


INITIAL_BALANCE = 50000
ACCOUNT_FILE = Path(__file__).with_name("atm_account.json")


def load_balance():
    try:
        with ACCOUNT_FILE.open(encoding="utf-8") as account_file:
            account_data = json.load(account_file)
    except FileNotFoundError:
        return INITIAL_BALANCE
    except json.JSONDecodeError as error:
        raise SystemExit(f"Could not read the saved account balance: {error}") from error

    if not isinstance(account_data, dict):
        raise SystemExit("The saved account balance file has an invalid format.")

    account_balance = account_data.get("account_balance")
    if (
        isinstance(account_balance, bool)
        or not isinstance(account_balance, int)
        or account_balance < 0
    ):
        raise SystemExit("The saved account balance must be a non-negative whole number.")

    return account_balance


def save_balance(account_balance):
    with ACCOUNT_FILE.open("w", encoding="utf-8") as account_file:
        json.dump({"account_balance": account_balance}, account_file)


def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


account_balance = load_balance()
account_firstname = input("Enter firstname: ")
account_lastname = input("Enter lastname: ")
account_username = f"{account_firstname} {account_lastname}"

while True:
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
    choice = read_integer("Enter choice (1-4): ")

    if choice == 1:
        print(f"""
========================================================
                WELCOME TO PYTHON ATM
========================================================

Account Name: {account_username}
Account Balance: ₦{account_balance}

========================================================
""")
    elif choice == 2:
        withdraw_money = read_integer("Enter the amount you want to withdraw: ")

        if withdraw_money <= 0:
            print(f"Enter a withdrawal amount greater than zero. Balance: ₦{account_balance}")
        elif withdraw_money > account_balance:
            print(
                f"Insufficient funds. Attempted withdrawal: ₦{withdraw_money}. "
                f"Balance: ₦{account_balance}"
            )
        else:
            new_balance = account_balance - withdraw_money
            save_balance(new_balance)
            account_balance = new_balance
            print(f"""
========================================================
                WELCOME TO PYTHON ATM
========================================================
Account Name: {account_username}
Amount Withdrawn: ₦{withdraw_money}
Current Account Balance: ₦{account_balance}

        Thank you for banking with us🤝.
========================================================
""")
    elif choice == 3:
        deposit_money = read_integer("Enter amount to be deposited: ")

        if deposit_money <= 0:
            print(f"Enter a deposit amount greater than zero. Balance: ₦{account_balance}")
        else:
            new_balance = account_balance + deposit_money
            save_balance(new_balance)
            account_balance = new_balance
            print(f"""
========================================================
                WELCOME TO PYTHON ATM
========================================================
Name: {account_username}
Amount Deposited: ₦{deposit_money}
Current Account Balance: ₦{account_balance}

                Thank you for banking with us🤝.
========================================================
""")
    elif choice == 4:
        print(f"Thank you {account_username}, for banking with us🤝.")
        break
    else:
        print("Invalid selection. Try 1-4.")
