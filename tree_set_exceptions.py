class ClassCastException(Exception):
    """Custom exception class for handling class cast errors."""

    def __init__(self, msg: str = None) -> None:
        """ClassCastException constructor."""
        if msg:
            super().__init__(msg)
        else:
            super().__init__()


class NoSuchElementException(Exception):
    """Custom exception class for handling no such element errors."""

    def __init__(self, msg: str = None) -> None:
        """NoSuchElementException constructor."""
        if msg:
            super().__init__(msg)
        else:
            super().__init__()


class NullPointerException(Exception):
    """Custom exception class for handling null pointer errors."""

    def __init__(self, msg: str = None) -> None:
        """NullPointerException constructor."""
        if msg:
            super().__init__(msg)
        else:
            super().__init__()
