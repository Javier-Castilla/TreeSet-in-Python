from typing import *


class Test1:
    def __init__(self):
        ...


class Test2:
    def __init__(self):
        ...

    def __eq__(self, other):
        return True

    def __lt__(self, other):
        return True


class Test3:
    def __init__(self):
        ...

    def __eq__(self, other):
        return True

    def __lt__(self, other):
        return True


class Test4:
    def __init__(self):
        ...


T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        super().__init__()
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items

    def __getitem__(self, item):
        print(item)



if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(2)
    stack.pop()
    stack.push('x')  # error: Argument 1 to "push" of "Stack" has incompatible type "str"; expected "int"
