class Checkbook:
    """
    A simple checkbook class to track deposits, withdrawals, and the current balance.
    """

    def __init__(self):
        """
        Initialize the checkbook with a starting balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook balance.

        Parameters:
            amount (float): The amount to be deposited. Must be non-negative.

        Returns:
            None
        """
        if amount < 0:
            print("Cannot deposit a negative amount.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook balance.

        Parameters:
            amount (float): The amount to be withdrawn. Must be <= current balance and non-negative.

        Returns:
            None
        """
        if amount < 0:
            print("Cannot withdraw a negative amount.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawl.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main loop to interact with the user for deposit, withdrawal, balance inquiry, or exit.

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action == 'deposit':
            try:
                amount_input = input("Enter the amount to deposit: $").strip()
                if not amount_input:
                    raise ValueError
                amount = float(amount_input)
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid, non-negative number.")

        elif action == 'withdraw':
            try:
                amount_input = input("Enter the amount to withdraw: $").strip()
                if not amount_input:
                    raise ValueError
                amount = float(amount_input)
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid, non-negative number.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

