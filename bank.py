from account import Account, CreditAccount, SavingsAccount


class Bank:
    """
    Bank class represents a bank.

    Attributes:
        name (str): The name of the bank.
        _accounts (list): The list of all accounts in the bank.

    Methods:
        create_account(category:str, owner:Customer, interest_rate:float) -> Account/CreditAccount/SavingsAccount:
        Creates a new account in the specified category with the given owner and interest rate.
        find_accounts_by_name(name:str) -> list: Finds all the accounts with the given name.
        find_accounts_by_ssn(ssn:str) -> list: Finds all the accounts with the given ssn.
        balance -> float: Property to get the total balance of all accounts in the bank.
    """

    def __init__(self, name):
        """
        Initializes the Bank object.

        Parameters:
            name (str): The name of the bank.
        """
        self.name = name
        self._accounts = []

    def create_account(self, category, owner, interest_rate=0):
        """
        Creates a new account in the specified category with the given owner and interest rate.

        Parameters:
            category (str): The category of the account. Can be 'account', 'credit', or 'savings'.
            owner (Customer): The owner of the account.
            interest_rate (float): The interest rate for the account. Default is 0.

        Returns:
            Account/CreditAccount/SavingsAccount: The newly created account object.

        Raises:
            AttributeError: If the category is invalid.
        """
        if category == "account":
            new_account = Account(owner)
        elif category == "credit":
            new_account = CreditAccount(owner, interest_rate)
        elif category == "savings":
            new_account = SavingsAccount(owner)
        else:
            raise AttributeError("Invalid category for the account.")
        self._accounts.append(new_account)
        return new_account

    def find_accounts_by_name(self, name):
        """
        Finds all the accounts with the given name.

        Parameters:
            name (str): The name of the account owner.

        Returns:
            list: A list of accounts with the given name.
        """
        return [
            account
            for account in self._accounts
            if name.upper() in account.owner.name.upper()
        ]

    def find_accounts_by_ssn(self, ssn):
        """
        Finds all the accounts with the given ssn.

        Parameters:
            ssn (str): The SSN of the account owner.

        Returns:
            list: A list of accounts with the given SSN.
        """
        return [account for account in self._accounts if account.owner.ssn == ssn]

    @property
    def balance(self):
        """
        Property to get the total balance of all accounts in the bank.

        Returns:
            float: The total balance of all accounts in the bank.
        """
        return sum([account.amount for account in self._accounts])
