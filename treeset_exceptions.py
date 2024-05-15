class NonComparableObjectError(Exception):
    """
    Custom exception class for handling non-comparable objects.

    This exception is raised when an attempt is made to compare objects
    that do not support comparison operations.

    Attributes:
        msg (str): The exception message. Default is None.

    Methods:
        __init__(self, msg: str = None): Initializes the exception.
    """

    def __init__(self, msg: str = None) -> None:
        """
        Initializes the NonComparableObjectError exception.

        Args:
            msg (str, optional): The exception message. Defaults to None.
        """
        if msg:
            super().__init__(msg)
        else:
            super().__init__()


class NoSuchElementError(Exception):
    """
    Custom exception class for handling non-existent elements.

    This exception is raised when an attempt is made to access an element
    that does not exist.

    Attributes:
        msg (str): The exception message. Default is None.

    Methods:
        __init__(self, msg: str = None): Initializes the exception.
    """

    def __init__(self, msg: str = None) -> None:
        """
        Initializes the NoSuchElementError exception.

        Args:
            msg (str, optional): The exception message. Defaults to None.
        """
        if msg:
            super().__init__(msg)
        else:
            super().__init__()