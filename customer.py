class Customer:
    """
    A simple class that represents a customer at the bank.
    """

    def __init__(self, name, ssn):
        """
        Initializes a new instance of the `Customer` class.

        Args:
            name (str): The name of the customer. Must be at least 2 characters long.
            ssn (str): The social security number of the customer. Must be a string of numbers.

        Raises:
            AttributeError: If either the `name` or `ssn` is invalid.
        """
        if type(name) is not str or len(name) < 2:
            raise AttributeError("Invalid name for the account.")

        if type(ssn) is not str or not ssn.isnumeric():
            raise AttributeError("Invalid SSN for the account.")

        self.name = name
        self.ssn = ssn
