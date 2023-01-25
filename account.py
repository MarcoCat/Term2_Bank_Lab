from customer import Customer


class Account:
    """
    Account class represents a bank account.

    Attributes:
        owner (Customer): The account owner.
        amount (float): The account balance.

    Methods:
        deposit(amount:float) -> None: Deposits the given amount in the account.
        withdraw(amount:float) -> None: Withdraws the given amount from the account.
        transfer(account:Account, amount:float) -> None: Transfers the given amount to the specified account.
        compute_interest() -> float: Computes the interest on the account balance.
    """

    def __init__(self, owner, amount=0.0):
        """
        Initializes the Account object.

        Parameters:
            owner (Customer): The account owner.
            amount (float): The account balance. Default is 0.0
        """
        if not isinstance(owner, Customer):
            raise AttributeError("Invalid account, owner is a Customer class")
        self.owner = owner
        self.amount = amount

    def deposit(self, amount):
        """
        Deposits the given amount in the account.

        Parameters:
            amount (float): The amount to be deposited.

        Raises:
            AttributeError: If the amount is invalid.
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise AttributeError("Invalid amount for the deposit.")
        self.amount += amount

    def withdraw(self, amount):
        """
        Withdraws the given amount from the account.

        Parameters:
            amount (float): The amount to be withdrawn.

        Raises:
            AttributeError: If the amount is invalid.
        """
        if not isinstance(amount, (int, float)):
            raise AttributeError("Invalid amount for the withdrawal.")
        self.amount -= amount

    def transfer(self, account, amount):
        """
        Transfers the given amount to the specified account.

        Parameters:
            account (Account): The account to which the amount is transferred.
            amount (float): The amount to be transferred.

        Raises:
            TypeError: If the account is invalid.
            AttributeError: If the amount is invalid.
        """
        if not isinstance(account, Account):
            raise TypeError("Invalid account for the transfer.")

        if not isinstance(amount, (int, float)):
            raise AttributeError("Invalid amount for the transfer.")

        if amount > self.amount:
            raise AttributeError("Insufficient funds.")

        self.amount -= amount
        account.amount += amount

    def compute_interest(self):
        """
        Computes the interest on the account balance.

        Returns:
            float: The new account balance after calculating interest and penalty.
        """
        if self.amount < 0:
            self.amount = self.amount * (100 + self.interest) / 100
            self.amount -= 10
        return self.amount


class CreditAccount(Account):
    """
    CreditAccount class represents a credit account.

    Attributes:
        owner (Customer): The account owner.
        amount (float): The account balance.
        interest (float): The interest rate.

    Methods:
        deposit(amount:float) -> None: Deposits the given amount in the account.
        withdraw(amount:float) -> None: Withdraws the given amount from the account.
        transfer(account:Account, amount:float) -> None: Transfers the given amount to the specified account.
        compute_interest() -> float: Computes the interest on the account balance.
    """

    def __init__(self, owner, interest):
        """
        Initializes the CreditAccount object.

        Parameters:
            owner (Customer): The account owner.
            interest (float): The interest rate.
        """
        super().__init__(owner)
        self.interest = interest

    def compute_interest(self):
        """
        Computes the interest on the account balance.

        Returns:
            float: The new account balance after calculating interest and penalty.
        """
        super().compute_interest()


class SavingsAccount(Account):
    """
    SavingsAccount class represents a savings account.

    Attributes:
        owner (Customer): The account owner.
        amount (float): The account balance.

    Methods:
        deposit(amount:float) -> None: Deposits the given amount in the account.
        withdraw(amount:float) -> None: Withdraws the given amount from the account.
        transfer(account:Account, amount:float) -> None: Transfers the given amount to the specified account.
        compute_interest() -> float: Computes the interest on the account balance.
    """

    def __init__(self, owner):
        """
        Initializes the SavingsAccount object.

        Parameters:
            owner (Customer): The account owner.
        """
        super().__init__(owner)

    @property
    def amount(self):
        """
        Property for the account balance.

        Returns:
            float: Account balance.
        """
        return self._amount if self._amount > 0 else 0

    @amount.setter
    def amount(self, value):
        """
        Sets the account balance.

        Parameters:
            value (float): The new balance.

        Raises:
            UserWarning: If the value is invalid.
        """
        if value < 0:
            raise UserWarning("Invalid amount for the account.")
        self._amount = value
