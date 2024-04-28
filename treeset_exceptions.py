class NonComparableObjectError(Exception):
    def __init__(self, msg: str = None) -> None:
        if msg:
            super().__init__(msg)
        else:
            super().__init__()


class NoSuchElementError(Exception):
    def __init__(self, msg: str = None) -> None:
        if msg:
            super().__init__(msg)
        else:
            super().__init__()
