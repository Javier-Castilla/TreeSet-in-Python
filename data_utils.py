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
from treeset_exceptions import *


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


E = TypeVar('E')

class RedBlackTree:

    @staticmethod
    def __check_comparable(function):
        def wrapper(self, *args):
            item = args[0]
            value_type = type(item) if not isinstance(item, type) else item
            if value_type.__eq__ is object.__eq__ \
                    or (value_type.__lt__ is object.__lt__
                        and value_type.__gt__ is object.__gt__):
                raise NonComparableObjectError(
                    f"class {value_type} cannot be compared")

            return function(self, *args)

        return wrapper

    def __complete_comparator(self, value_type: Type):
        if value_type.__lt__ is object.__lt__ and value_type.__gt__ is not object.__gt__:
            def __lt__(self, other):
                if isinstance(other, type(self)):
                    if self == other:
                        return True
                    return not self.__gt__(other)
                return False

            setattr(value_type, '__lt__', __lt__)
        elif value_type.__gt__ is object.__gt__ and value_type.__lt__ is not object.__lt__:
            def __gt__(self, other):
                if isinstance(other, type(self)):
                    if self == other:
                        return True
                    return not self.__lt__(other)
                return False

            setattr(value_type, '__gt__', __gt__)

        return value_type

    @staticmethod
    def __type_validation(function):
        """Decorator used to validate item type when adding or deleting it from a TreeSet.
        This decorator should not be used with other object instance but a TreeSet.

        :param function: function used of the TreeSet
        :return: function return statement
        """

        def wrapper(self, item):
            if not isinstance(item, self.__class_type):
                raise TypeError(f"Value type must be '{self.__class_type}: {type(item)}'")

            return function(self, item)

        return wrapper

    @__check_comparable
    def __init__(self, tree_type: Type):
        self.__tree_type = self.__complete_comparator(tree_type)
        self.__root = None
        self.__size = 0

    @__type_validation
    def add(self, value: E) -> bool:
        """Inserts the given value into the TreeSet if value is not contained.

        :param value: Value to insert into the TreeSet
        :type value: E
        :return: True if the value have been added to the TreeSet else False
        :rtype: bool
        :raises AssertionError: If the given value's type does not match generic
        type
        """
        if (parent := self.__contains(value)) and parent.value == value:
            return False

        new_node = TreeNode(value)

        if not parent:
            self.__root = new_node
        elif new_node < parent:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.parent = parent

        self.__size += 1
        self.__fix_insertion(new_node)
        return True

    def remove(self, value: E) -> bool:
        if self.is_empty() or (current := self.__contains(value)).value != value:
            return False

        successor, position = self.__successor(current)
        if successor and position == 1:
            ...

    @staticmethod
    def __successor(node: TreeNode) -> Union[TreeNode, None]:
        if not node:
            return (None, None)
        elif node.right:
            current = node.right
            while current.left:
                current = current.left

            return (current, 1)
        else:
            return (node.left, -1)

    def __contains(self, value: E) -> TreeNode:
        """Checks if the given value is contained into the current TreeSet and
        returns the TreeNode where it is contained or a leaf.

        :param value: value to check
        :return: TreeNode having the searched value or a leaf
        :rtype: TreeNode
        """
        if self.is_empty():
            return self.__root

        parent = None
        current = self.__root

        while current:
            if current.value == value:
                return current

            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return parent

if __name__ == "__main__":
    stack = SimpleQueue()
    stack.enqueue(n1 := TreeNode(1))
    stack.enqueue(n2 := TreeNode(2))
    stack.enqueue(n3 := TreeNode(3))

    for item in stack:
        print(repr(item))
