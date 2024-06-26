class Checkbook:
    def __init__(self):
        """
        Initialize a new Checkbook object with zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit funds into the checkbook.

        Parameters:
        - amount (float): The amount to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw funds from the checkbook if sufficient balance is available.

        Parameters:
        - amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Get the current balance in the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook object.

    Allows the user to deposit, withdraw, check balance, or exit the program.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    raise ValueError("Deposit amount must be positive.")
                cb.deposit(amount)
            except ValueError as e:
                print("Error:", e)
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    raise ValueError("Withdrawal amount must be positive.")
                cb.withdraw(amount)
            except ValueError as e:
                print("Error:", e)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

