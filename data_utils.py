from typing import Any


class SimpleQueue:
    def __init__(self, value: Any = None) -> None:
        self.__first = None
        self.__last = None

        if value:
            self.enqueue(value)

    def enqueue(self, value: Any) -> None:
        new_node = Node(value)

        if self.is_empty():
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next_node = new_node
            self.__last = new_node

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is already empty")

        value = self.__first.value

        if self.__first == self.__last:
            self.__first = None
            self.__last = None
        else:
            self.__first = self.__first.next_node

        return value

    def is_empty(self) -> bool:
        return self.__last is None

    def __iter__(self):
        current = self.__first

        while current is not None:
            yield current
            current = current.next_node

    def __str__(self):
        return f"{[node for node in self]}"


class SimpleStack:
    def __init__(self, value: Any = None) -> None:
        self.__first = None

        if value:
            self.push(value)

    def push(self, value: Any) -> None:
        new_node = Node(value)

        if self.is_empty():
            self.__first = new_node
        else:
            new_node.next_node = self.__first
            self.__first = new_node

    def pull(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack is already empty")

        value = self.__first.value
        self.__first = self.__first.next_node

        return value

    def is_empty(self) -> bool:
        return self.__first is None

    def __iter__(self):
        current = self.__first

        while current is not None:
            yield current
            current = current.next_node

    def __str__(self):
        return f"{[node for node in self]}"


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next_node = None

    @property
    def value(self) -> Any:
        return self.__value

    @value.setter
    def value(self, value: Any) -> None:
        self.__value = value

    @property
    def next_node(self) -> Any:
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node: Any) -> None:
        self.__next_node = next_node

    def __repr__(self) -> str:
        return f"Node({self.value})"
