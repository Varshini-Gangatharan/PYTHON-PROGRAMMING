import sqlite3
from getpass import getpass

# Connect to the SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('atm_database.db')
cursor = conn.cursor()

# Create a table to store account information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_number INTEGER PRIMARY KEY,
        pin INTEGER,
        balance REAL
    )
''')

# Sample data (you can add more accounts as needed)
sample_data = [
    (123456, 1234, 1000.0),
    (789012, 5678, 500.0),
    # Add more accounts if needed
]
sample_data = [
    ('192210720', '6153', 15000),
    ('192219077', '2802', 5000),
    ('192212402', '0204', 10000),
    ('123456789', '4589', 20000)
]

# Insert sample data into the accounts table
cursor.executemany('INSERT INTO accounts VALUES (?, ?, ?)', sample_data)

# Commit the changes and close the connection
conn.commit()
conn.close()


def authenticate_user():
    # Function to authenticate the user using account number and PIN
    account_number = int(input("Enter your account number: "))
    pin = int(getpass("Enter your PIN: "))  # Using getpass to hide the PIN input

    conn = sqlite3.connect('atm_database.db')
    cursor = conn.cursor()

    # Check if the account exists and the PIN is correct
    cursor.execute('SELECT * FROM accounts WHERE account_number = ? AND pin = ?', (account_number, pin))
    account = cursor.fetchone()

    conn.close()
    return account


def display_balance(balance):
    print(f'Your current balance: ${balance:.2f}')


def deposit(account):
    # Function to handle the deposit process
    amount = float(input("Enter the deposit amount: "))

    conn = sqlite3.connect('atm_database.db')
    cursor = conn.cursor()

    # Update the account balance
    new_balance = account[2] + amount
    cursor.execute('UPDATE accounts SET balance = ? WHERE account_number = ?', (new_balance, account[0]))

    conn.commit()
    conn.close()

    display_balance(new_balance)


def withdraw(account):
    # Function to handle the withdrawal process
    amount = float(input("Enter the withdrawal amount: "))

    conn = sqlite3.connect('atm_database.db')
    cursor = conn.cursor()

    # Check if the account has sufficient balance
    if account[2] >= amount:
        # Update the account balance
        new_balance = account[2] - amount
        cursor.execute('UPDATE accounts SET balance = ? WHERE account_number = ?', (new_balance, account[0]))
        conn.commit()
        conn.close()
        display_balance(new_balance)
    else:
        conn.close()
        print("Insufficient funds. Withdrawal canceled.")


def main():
    print("Welcome to the ATM")

    # Authentication
    account = authenticate_user()

    if account:
        print("Authentication successful")

        while True:
            # Main menu
            print("\n1. Display Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                display_balance(account[2])
            elif choice == 2:
                deposit(account)
            elif choice == 3:
                withdraw(account)
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
