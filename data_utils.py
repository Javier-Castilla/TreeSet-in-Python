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
        """
        Constructor of the class.
        Initializes a new instance of SimpleQueue.
        :param value: The initial value to enqueue. Default is None.
        """
        self.__first = None
        self.__last = None
        self.__current = None

        if value:
            self.enqueue(value)

    def enqueue(self, value: Any) -> None:
        """
        Enqueues a new value to the queue.
        :param value: The value to enqueue.
        """
        new_node = Node(value)

        if self.is_empty():
            self.__first = self.__last = self.__current = new_node
        else:
            self.__last.next_node = new_node
            self.__last = new_node

    def dequeue(self) -> Any:
        """
        Dequeues a value from the queue.
        :return: The dequeued value.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is already empty")

        value = self.__first.value

        if self.__first == self.__last:
            self.__first = self.__last = self.__current = None
        else:
            self.__first = self.__current = self.__first.next_node

        return value

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.
        :return: True if the queue is empty, False otherwise.
        """
        return self.__last is None

    def __iter__(self):
        """
        Returns an iterator for the queue.
        :return: An iterator for the queue.
        """
        self.__current = self.__first
        return self

    def __next__(self):
        """
        Returns the next value from the queue iterator.
        :return: The next value from the queue iterator.
        :raises StopIteration: If there are no more items to return.
        """
        if not self.__current:
            self.__current = self.__first
            raise StopIteration
        item = self.__current.value
        self.__current = self.__current.next_node
        return item

    def __str__(self):
        """
        Returns a string representation of the queue.
        :return: A string representation of the queue.
        """
        return f"{[node for node in self]}"


class SimpleStack:
    """Class that represents a stack."""

    def __init__(self, value: Any = None) -> None:
        """
        Constructor of the class.
        Initializes a new instance of SimpleStack.
        :param value: The initial value to push onto the stack. Default is None.
        """
        self.__items = list()
        self.__index = -1

        if value:
            self.push(value)

    def push(self, value: Any) -> None:
        """
        Pushes a new value onto the stack.
        :param value: The value to push.
        """
        self.__items.append(value)
        self.__index += 1

    def pull(self) -> Any:
        """
        Pulls a value from the stack.
        :return: The pulled value.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is already empty")

        self.__index -= 1
        return self.__items.pop()

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.
        :return: True if the stack is empty, False otherwise.
        """
        return len(self.__items) == 0

    def __iter__(self):
        """
        Returns an iterator for the stack.
        :return: An iterator for the stack.
        """
        return self

    def __next__(self):
        """
        Returns the next value from the stack iterator.
        :return: The next value from the stack iterator.
        :raises StopIteration: If there are no more items to return.
        """
        if self.__index < 0:
            self.__index = len(self.__items) - 1
            raise StopIteration
        item = self.__items[self.__index]
        self.__index -= 1
        return item

    def __str__(self):
        """
        Returns a string representation of the stack.
        :return: A string representation of the stack.
        """
        return f"{[node for node in self]}"


class Node:
    """
    Class that represents a node in a data structure (like a linked list or a tree).
    Each node has a value and pointers to the next and previous nodes.
    """

    def __init__(self, value: Any):
        """
        Constructor of the class.
        Initializes a new instance of Node.
        :param value: The initial value of the node.
        """
        self.value = value
        self.next_node = None
        self.previous_node = None

    @property
    def value(self) -> Any:
        """
        Getter for the value of the node.
        :return: The value of the node.
        """
        return self.__value

    @value.setter
    def value(self, value: Any) -> None:
        """
        Setter for the value of the node.
        :param value: The new value for the node.
        """
        self.__value = value

    @property
    def next_node(self) -> Any:
        """
        Getter for the next node.
        :return: The next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node: Any) -> None:
        """
        Setter for the next node.
        :param next_node: The new next node.
        """
        self.__next_node = next_node

    @property
    def previous_node(self) -> Any:
        """
        Getter for the previous node.
        :return: The previous node.
        """
        return self.__previous_node

    @previous_node.setter
    def previous_node(self, previous_node: Any) -> None:
        """
        Setter for the previous node.
        :param previous_node: The new previous node.
        """
        self.__previous_node = previous_node

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.
        :return: A string representation of the node.
        """
        return f"Node({self.value})"

    def __eq__(self, other: 'TreeNode') -> bool:
        """
        Checks if the current node is equal to the other node.
        :param other: The other node to compare with.
        :return: True if the nodes are equal, False otherwise.
        """
        if isinstance(other, TreeNode):
            return self.value == other.value
        return False

    def __lt__(self, other: 'TreeNode') -> bool:
        """
        Checks if the current node is less than the other node.
        :param other: The other node to compare with.
        :return: True if the current node is less than the other node, False otherwise.
        """
        if isinstance(other, TreeNode):
            return self.value < other.value
        return False

    def __gt__(self, other: 'TreeNode') -> bool:
        """
        Checks if the current node is greater than the other node.
        :param other: The other node to compare with.
        :return: True if the current node is greater than the other node, False otherwise.
        """
        if isinstance(other, TreeNode):
            return not self < other
        return False


class TreeNode(Node):
    """
    Class that represents a TreeNode, which is a specialized Node that also
    includes a color property. This class is used in the RedBlackTree data
    structure.
    """

    class TreeNodeUtils(Enum):
        """
        Enum class that represents the possible colors of a TreeNode in a
        RedBlackTree.
        """
        RED = 1
        BLACK = 0
        NULL = -1

    def __init__(
            self, value: Any, left: Union['TreeNode', None],
            right: Union['TreeNode', None],
            color: 'TreeNode.TreeNodeUtils' = TreeNodeUtils.RED
    ) -> None:
        """
        Constructor of the class.
        Initializes a new instance of TreeNode.
        :param value: The initial value of the node.
        :param left: The left child of the node. Default is None.
        :param right: The right child of the node. Default is None.
        :param color: The color of the node. Default is RED.
        """
        super().__init__(value)
        self.parent = None
        self.color = color
        self.left = left
        self.right = right

    @property
    def color(self) -> TreeNodeUtils:
        """
        Getter for the color of the node.
        :return: The color of the node.
        """
        return self.__color

    @color.setter
    def color(self, color: TreeNodeUtils) -> None:
        """
        Setter for the color of the node.
        :param color: The new color for the node.
        """
        assert isinstance(color,
                          TreeNode.TreeNodeUtils), "Value type should be Color"
        assert color in {TreeNode.TreeNodeUtils.RED,
                         TreeNode.TreeNodeUtils.BLACK}, \
            "Value must be 0 ('BLACK') or 1 ('RED')"

        self.__color = color

    @property
    def left(self) -> Any:
        """
        Getter for the left child of the node.
        :return: The left child of the node.
        """
        return self.__left

    @left.setter
    def left(self, node: 'TreeNode') -> None:
        """
        Setter for the left child of the node.
        :param node: The new left child for the node.
        """
        self.__left = node

    @property
    def right(self) -> Any:
        """
        Getter for the right child of the node.
        :return: The right child of the node.
        """
        return self.__right

    @right.setter
    def right(self, node: 'TreeNode') -> None:
        """
        Setter for the right child of the node.
        :param node: The new right child for the node.
        """
        self.__right = node

    def __str__(self) -> str:
        """
        Returns a string representation of the node.
        :return: A string representation of the node.
        """
        left = self.left if self.left is None else self.left.value
        right = self.right if self.right is None else self.right.value
        return f"({self.value}: {left}, {right})"

    def __repr__(self) -> str:
        """
        Returns a string representation of the node for debugging.
        :return: A string representation of the node.
        """
        return f"TreeNode({self.value}, {self.color})"


class RedBlackTree:
    """
    Class that represents a Red-Black Tree, a self-balancing binary search
    tree. Each node of the binary tree has an extra bit for denoting the
    color of the node, either red or black.
    """

    _RED = TreeNode.TreeNodeUtils.RED
    _BLACK = TreeNode.TreeNodeUtils.BLACK
    _NULL = TreeNode(TreeNode.TreeNodeUtils.NULL, None, None,
                     TreeNode.TreeNodeUtils.BLACK)

    def __init__(self) -> None:
        """
        Constructor of the class.
        Initializes a new instance of RedBlackTree.
        """
        self.__root = self._NULL
        self.__size = 0
        self.iterations = 0
        self.count = False

    def is_empty(self) -> bool:
        """
        Checks if the current RedBlackTree is empty or not.
        :return: True if RedBlackTree is empty else False
        """
        return self.__size == 0

    def add(self, value: Any) -> bool:
        """
        Inserts a new value into the RedBlackTree.
        :param value: The value to insert.
        :return: False if the value already exists in the tree, True otherwise.
        """
        if (parent := self.__contains(
                value)) is not self._NULL and parent.value == value:
            return False

        node = TreeNode(value, self._NULL, self._NULL, self._RED)
        parent = None if parent is self._NULL else parent

        node.parent = parent
        if parent is None:
            self.__root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = self._BLACK
        elif node.parent.parent is not None:
            self.__fix_after_insertion(node)

        self.__size += 1
        return True

    def remove(self, value):
        """
        Deletes a value from the RedBlackTree.
        :param value: The value to delete.
        :return: False if the value does not exist in the tree, True otherwise.
        """
        if (
        node := self.__contains(value)) is self._NULL or node.value != value:
            return False

        successor = node
        successor_color = successor.color
        if node.left is self._NULL:
            replacement = node.right
            self.__replace(node, node.right)
        elif node.right is self._NULL:
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

        if successor_color == self._BLACK:
            self.__fix_after_deletion(replacement)

        self.__size -= 1
        return True

    def size(self) -> int:
        """
        Returns the size of the RedBlackTree.
        :return: The size of the RedBlackTree.
        """
        return self.__size

    def __fix_after_insertion(self, node: TreeNode):
        """
        Fixes the RedBlackTree after an insertion operation.
        :param node: The node that was inserted.
        """
        while node.parent.color == self._RED:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == self._RED:
                    uncle.color = self._BLACK
                    node.parent.color = self._BLACK
                    node.parent.parent.color = self._RED
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self.__right_rotation(node)
                    node.parent.color = self._BLACK
                    node.parent.parent.color = self._RED
                    self.__left_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.color == self._RED:
                    uncle.color = self._BLACK
                    node.parent.color = self._BLACK
                    node.parent.parent.color = self._RED
                    node = node.parent.parent
                else:
                    if node is node.parent.right:
                        node = node.parent
                        self.__left_rotation(node)
                    node.parent.color = self._BLACK
                    node.parent.parent.color = self._RED
                    self.__right_rotation(node.parent.parent)
            if node == self.__root:
                break

        self.__root.color = self._BLACK

    def __left_rotation(self, node: TreeNode) -> None:
        """
        Performs a left rotation on a node.
        :param node: The node to perform the rotation on.
        """
        other = node.right
        node.right = other.left
        if other.left is not self._NULL:
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
        """
        Performs a right rotation on a node.
        :param node: The node to perform the rotation on.
        """
        other = node.left
        node.left = other.right
        if other.right is not self._NULL:
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
        """
        Fixes the RedBlackTree after a deletion operation.
        :param node: The node that was deleted.
        """
        while node is not self.__root and node.color == self._BLACK:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == self._RED:
                    sibling.color = self._BLACK
                    node.parent.color = self._RED
                    self.__left_rotation(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == self._BLACK \
                        and sibling.right.color == self._BLACK:
                    sibling.color = self._RED
                    node = node.parent
                else:
                    if sibling.right.color == self._BLACK:
                        sibling.left.color = self._BLACK
                        sibling.color = self._RED
                        self.__right_rotation(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = self._BLACK
                    sibling.right.color = self._BLACK
                    self.__left_rotation(node.parent)
                    node = self.__root
            else:
                sibling = node.parent.left
                if sibling.color == self._RED:
                    sibling.color = self._BLACK
                    node.parent.color = self._RED
                    self.__right_rotation(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == self._BLACK \
                        and sibling.right.color == self._BLACK:
                    sibling.color = self._RED
                    node = node.parent
                else:
                    if sibling.left.color == self._BLACK:
                        sibling.right.color = self._BLACK
                        sibling.color = self._RED
                        self.__left_rotation(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = self._BLACK
                    sibling.left.color = self._BLACK
                    self.__right_rotation(node.parent)
                    node = self.__root

        node.color = self._BLACK

    def __replace(self, node: TreeNode, other: TreeNode):
        """
        Replaces a node with another node.
        :param node: The node to be replaced.
        :param other: The node to replace with.
        """
        if not node.parent:
            self.__root = other
        elif node == node.parent.left:
            node.parent.left = other
        else:
            node.parent.right = other
        other.parent = node.parent

    def __symmetrical_successor(self, node):
        """
        Finds the symmetrical successor of a node.
        :param node: The node to find the symmetrical successor of.
        :return: The symmetrical successor of the node.
        """
        while node.left is not self._NULL:
            node = node.left
        return node

    def __contains(self, value) -> TreeNode:
        """
        Checks if the given value is contained in the current RedBlackTree and
        returns the TreeNode where it is contained or a leaf.
        :param value: The value to check.
        :return: TreeNode having the searched value or a leaf.
        """
        parent = self._NULL
        current = self.__root

        while current is not self._NULL:
            if self.count:
                self.iterations += 1
            if current.value == value:
                return current

            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return parent

    def __inorder(self, inorder: bool) -> Any:
        """
        Generator that traverses the RedBlackTree in-order or reversed.
        :param inorder: if True the route will be in-order else reversed.
        """
        stack = SimpleStack()
        current = self.__root

        while True:
            if current is not self._NULL:
                stack.push(current)
                current = current.left if inorder else current.right
            elif not stack.is_empty():
                current = stack.pull()
                yield current
                current = current.right if inorder else current.left
            else:
                break

    def __eq__(self, other) -> bool:
        """
        Check equality between the current instance and a given object.
        This method is called when using built-in operator '=='.
        :param other: other instance to compare with.
        :return: True if instances are equal else False.
        """
        if isinstance(other, RedBlackTree):
            if self.size() != other.size():
                return False

            for value in self:
                if value not in other:
                    return False

            return True
        else:
            return False

    def __iter__(self) -> Any:
        """
        Method to iterate over the RedBlackTree instance.
        """
        for node in self.__inorder(True):
            yield node.value

    def __reversed__(self) -> Any:
        """
        Method to iterate reversely over the RedBlackTree instance.
        """
        for node in self.__inorder(False):
            yield node.value

    def __str__(self) -> str:
        """
        Returns a string representation of the current RedBlackTree.
        :return: RedBlackTree string representation.
        """
        return f"{[value for value in self]}"

    def __contains__(self, value) -> bool:
        """
        Check if the given value is contained in the RedBlackTree or not.
        This method is called when using built-in operator 'in'.
        :param value: The value to check.
        :return: True if it is contained else False.
        """
        return self.__contains(value).value == value

    def __len__(self) -> int:
        """
        Provides the length of the current RedBlackTree. It is used with the
        built-in method len().
        :return: The length of the RedBlackTree.
        """
        return self.__size

    def depth(self, node=None):
        """
        Calculate the maximum depth of the tree.
        :param node: The node to start the depth calculation from. Defaults to the root of the tree.
        :return: The maximum depth of the tree.
        """
        if node is None:
            node = self.__root

        if node is self._NULL:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)

        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    t = RedBlackTree()

    for i in range(10):
        t.add(i)

    print(t)
