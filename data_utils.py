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
    class TreeNodeUtils(Enum):
        RED = 1
        BLACK = 0
        NULL = -1

    def __init__(
            self, value: Any, left: Union['TreeNode', None],
            right: Union['TreeNode', None],
            color: 'TreeNode.TreeNodeUtils' = TreeNodeUtils.RED
    ) -> None:
        super().__init__(value)
        self.parent = None
        self.color = color
        self.left = left
        self.right = right

    @property
    def color(self) -> TreeNodeUtils:
        return self.__color

    @color.setter
    def color(self, color: TreeNodeUtils) -> None:
        assert isinstance(color, TreeNode.TreeNodeUtils), "Value type should be Color"
        assert color in {TreeNode.TreeNodeUtils.RED, TreeNode.TreeNodeUtils.BLACK}, \
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

class RedBlackTree:
    __RED = TreeNode.TreeNodeUtils.RED
    __BLACK = TreeNode.TreeNodeUtils.BLACK
    __NULL = TreeNode(TreeNode.TreeNodeUtils.NULL, None, None, TreeNode.TreeNodeUtils.BLACK)

    def __init__(self) -> None:
        self.__root = self.__NULL
        self.__size = 0

    def is_empty(self) -> bool:
        """Checks if the current TreeSet is empty or not.

        :return: True if TreeSet is empty else False
        :rtype: bool
        """
        return self.__size == 0
    
    def insert(self, value: Any) -> bool:
        if (parent := self.__contains(value)) is not self.__NULL and parent.value == value:
            return False

        node = TreeNode(value, self.__NULL, self.__NULL, self.__RED)
        parent = None if parent is self.__NULL else parent

        node.parent = parent
        if parent is None:
            self.__root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = self.__BLACK
        elif node.parent.parent is not None:
            self.__fix_after_insertion(node)

        self.__size += 1
        return True
    
    def delete(self, value):
        if (node := self.__contains(value)) is self.__NULL or node.value != value:
            return False

        successor = node
        successor_color = successor.color
        if node.left is self.__NULL:
            replacement = node.right
            self.__replace(node, node.right)
        elif node.right is self.__NULL:
            replacement = node.left
            self.__replace(node, node.left)
        else:
            successor = self.__symmetrical_successor(node.right)
            successor_color = successor.color
            replacement = successor.right

            if successor.parent == node:
                replacement.parent = successor
            else:
                self.__replace(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            self.__replace(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color

        if successor_color == self.__BLACK:
            self.__fix_after_deletion(replacement)

        self.__size -= 1
        return True

    def __fix_after_insertion(self, node: TreeNode):
        while node.parent.color == self.__RED:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == self.__RED:
                    uncle.color = self.__BLACK
                    node.parent.color = self.__BLACK
                    node.parent.parent.color = self.__RED
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self.__right_rotation(node)
                    node.parent.color = self.__BLACK
                    node.parent.parent.color = self.__RED
                    self.__left_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.color == self.__RED:
                    uncle.color = self.__BLACK
                    node.parent.color = self.__BLACK
                    node.parent.parent.color = self.__RED
                    node = node.parent.parent
                else:
                    if node is node.parent.right:
                        node = node.parent
                        self.__left_rotation(node)
                    node.parent.color = self.__BLACK
                    node.parent.parent.color = self.__RED
                    self.__right_rotation(node.parent.parent)
            if node == self.__root:
                break

        self.__root.color = self.__BLACK

    def __left_rotation(self, node: TreeNode) -> None:
        other = node.right
        node.right = other.left
        if other.left is not self.__NULL:
            other.left.parent = node

        other.parent = node.parent
        if node.parent is None:
            self.__root = other
        elif node == node.parent.left:
            node.parent.left = other
        else:
            node.parent.right = other
        other.left = node
        node.parent = other

    def __right_rotation(self, node: TreeNode) -> None:
        other = node.left
        node.left = other.right
        if other.right is not self.__NULL:
            other.right.parent = node

        other.parent = node.parent
        if node.parent is None:
            self.__root = other
        elif node == node.parent.right:
            node.parent.right = other
        else:
            node.parent.left = other
        other.right = node
        node.parent = other

    def __fix_after_deletion(self, node):
        while node != self.__root and node.color == self.__BLACK:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == self.__RED:
                    sibling.color = self.__BLACK
                    node.parent.color = self.__RED
                    self.__left_rotation(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == self.__BLACK \
                        and sibling.right.color == self.__BLACK:
                    sibling.color = self.__RED
                    node = node.parent
                else:
                    if sibling.right.color == self.__BLACK:
                        sibling.left.color = self.__BLACK
                        sibling.color = self.__RED
                        self.__right_rotation(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = self.__BLACK
                    sibling.right.color = self.__BLACK
                    self.__left_rotation(node.parent)
                    node = self.__root
            else:
                sibling = node.parent.left
                if sibling.color == self.__RED:
                    sibling.color = self.__BLACK
                    node.parent.color = self.__RED
                    self.__right_rotation(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == self.__BLACK \
                        and sibling.right.color == self.__BLACK:
                    sibling.color = self.__RED
                    node = node.parent
                else:
                    if sibling.left.color == self.__BLACK:
                        sibling.right.color = self.__BLACK
                        sibling.color = self.__RED
                        self.__left_rotation(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = self.__BLACK
                    sibling.left.color = self.__BLACK
                    self.__right_rotation(node.parent)
                    node = self.__root

        node.color = self.__BLACK

    def __replace(self, node: TreeNode, other: TreeNode):
        if not node.parent:
            self.__root = other
        elif node == node.parent.left:
            node.parent.left = other
        else:
            node.parent.right = other
        other.parent = node.parent

    def __symmetrical_successor(self, node):
        while node.left is not self.__NULL:
            node = node.left
        return node
    
    def __contains(self, value) -> TreeNode:
        """Checks if the given value is contained into the current TreeSet and
        returns the TreeNode where it is contained or a leaf.

        :param value: value to check
        :return: TreeNode having the searched value or a leaf
        :rtype: TreeNode
        """
        parent = self.__NULL
        current = self.__root

        while current is not self.__NULL:
            if current.value == value:
                return current

            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return parent

    def __inorder(self, inorder: bool) -> Any:
        """Generator that traverses the TreeSet in-order or reversed.

        :param inorder: if True the route will be in-order else reversed
        """
        stack = SimpleStack()
        current = self.__root

        while True:
            if current is not self.__NULL:
                stack.push(current)
                current = current.left if inorder else current.right
            elif not stack.is_empty():
                current = stack.pull()
                yield current
                current = current.right if inorder else current.left
            else:
                break

    def __eq__(self, other) -> bool:
        """Check equality between the current instance and a given object.
        This method is called when using built-in operator '=='.

        :param other: other instance to compare with
        :return: True if instances are equal else False
        :rtype: bool
        """
        if isinstance(other, RedBlackTree):
            for value in self:
                if value not in other:
                    return False

            return True
        else:
            return False

    def __iter__(self) -> Any:
        """Method to iterate over the TreeSet instance."""
        for node in self.__inorder(True):
            yield node.value

    def __str__(self) -> str:
        """String representation of the current TreeSet.

        :return: TreeSet string representation
        :rtype: str
        """
        return f"{[value for value in self]}"

if __name__ == "__main__":
    t = RedBlackTree()

    for i in range(10):
        t.insert(i)

    print(t)
