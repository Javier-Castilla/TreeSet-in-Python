"""
data_utils module.

This module provides four different minor data structures classes.
    1. SimpleQueue
    2. SimpleStack
    3. Node
    4. TreeNode
"""

from enum import Enum
from functools import total_ordering
from typing import *


class SimpleQueue:
    """Class that represents a queue."""

    def __init__(self, value: Any = None) -> None:
        """Constructor of the class."""
        self.__first = None
        self.__last = None
        self.__current = None

        if value:
            self.enqueue(value)

    def enqueue(self, value: Any) -> None:
        new_node = Node(value)

        if self.is_empty():
            self.__first = self.__last = self.__current = new_node
        else:
            self.__last.next_node = new_node
            self.__last = new_node

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is already empty")

        value = self.__first.value

        if self.__first == self.__last:
            self.__first = self.__last = self.__current = None
        else:
            self.__first = self.__current = self.__first.next_node

        return value

    def is_empty(self) -> bool:
        return self.__last is None

    def __iter__(self):
        self.__current = self.__first
        return self

    def __next__(self):
        if not self.__current:
            self.__current = self.__first
            raise StopIteration
        item = self.__current.value
        self.__current = self.__current.next_node
        return item

    def __str__(self):
        return f"{[node for node in self]}"


class SimpleStack:
    def __init__(self, value: Any = None) -> None:
        self.__items = list()
        self.__index = -1

        if value:
            self.push(value)

    def push(self, value: Any) -> None:
        self.__items.append(value)
        self.__index += 1

    def pull(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack is already empty")

        self.__index -= 1
        return self.__items.pop()

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < 0:
            self.__index = len(self.__items) - 1
            raise StopIteration
        item = self.__items[self.__index]
        self.__index -= 1
        return item

    def __str__(self):
        return f"{[node for node in self]}"


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next_node = None
        self.previous_node = None

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

    @property
    def previous_node(self) -> Any:
        return self.__previous_node

    @previous_node.setter
    def previous_node(self, previous_node: Any) -> None:
        self.__previous_node = previous_node

    def __repr__(self) -> str:
        return f"Node({self.value})"

    def __eq__(self, other: 'TreeNode') -> bool:
        if isinstance(other, TreeNode):
            return self.value == other.value
        return False

    def __lt__(self, other: 'TreeNode') -> bool:
        if isinstance(other, TreeNode):
            return self.value < other.value
        return False

    def __gt__(self, other: 'TreeNode') -> bool:
        if isinstance(other, TreeNode):
            return not self < other
        return False


class TreeNode(Node):
    class Color(Enum):
        RED = 1
        BLACK = 0

    def __init__(self, value: Any, color: 'TreeNode.Color' = Color.RED) -> None:
        super().__init__(value)
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, color: Color) -> None:
        assert isinstance(color, TreeNode.Color), "Value type should be Color"
        assert color in {TreeNode.Color.RED, TreeNode.Color.BLACK}, \
            "Value must be 0 ('BLACK') or 1 ('RED')"

        self.__color = color

    @property
    def left(self) -> Any:
        return self.__left

    @left.setter
    def left(self, node: 'TreeNode') -> None:
        self.__left = node

    @property
    def right(self) -> Any:
        return self.__right

    @right.setter
    def right(self, node: 'TreeNode') -> None:
        self.__right = node

    def __str__(self) -> str:
        left = self.left if self.left is None else self.left.value
        right = self.right if self.right is None else self.right.value
        return f"({self.value}: {left}, {right})"

    def __repr__(self) -> str:
        return f"TreeNode({self.value}, {self.color})"

if __name__ == "__main__":
    stack = SimpleQueue()
    stack.enqueue(n1 := TreeNode(1))
    stack.enqueue(n2 := TreeNode(2))
    stack.enqueue(n3 := TreeNode(3))

    for item in stack:
        print(repr(item))