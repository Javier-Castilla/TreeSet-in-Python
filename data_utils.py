"""
data_utils module.

This module provides four different minor data structures classes.
    1. SimpleQueue
    2. SimpleStack
    3. Node
    4. TreeNode
"""

from enum import Enum
from typing import *


class SimpleQueue:
    """
    Class that represents a queue.
    """

    def __init__(self, value: Any = None) -> None:
        """
        Constructor of the class. Initializes a new instance of SimpleQueue.

        :param value: the initial value to enqueue, default is None
        :type value: Any
        """
        self.__first = None
        self.__last = None
        self.__current = None
        self.__size = 0

        if value:
            if isinstance(value, Collection):
                for item in value:
                    self.enqueue(item)
            else:
                self.enqueue(value)

    def enqueue(self, value: Any) -> None:
        """
        Enqueues a new value to the queue.

        :param value: the value to enqueue
        :type value: Any
        """
        new_node = Node(value)

        if self.is_empty():
            self.__first = self.__last = self.__current = new_node
        else:
            self.__last.next_node = new_node
            self.__last = new_node

        self.__size += 1

    def dequeue(self) -> Any:
        """
        Dequeues a value from the queue.

        :return: the dequeued value
        :rtype: Any
        :raises IndexError: if the queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is already empty")

        value = self.__first.value

        if self.__first == self.__last:
            self.__first = self.__last = self.__current = None
        else:
            self.__first = self.__current = self.__first.next_node

        self.__size -= 1
        return value

    def peek(self) -> Any:
        """
        Returns the value at the top of the queue without removing it.

        :return: the value at the top of the queue
        :rtype: Any
        :raises IndexError: if the queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.__first.value

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        :return: True if the queue is empty, False otherwise
        :rtype: bool
        """
        return len(self) == 0

    def __len__(self) -> int:
        """
        Returns the length of the queue.

        :return: the length of the queue
        :rtype: int
        """
        return sum(1 for _ in self)

    def __iter__(self) -> Iterator[Any]:
        """
        Returns an iterator for the queue.

        :return: an iterator for the queue
        :rtype: Iterator[Any]
        """
        self.__current = self.__first
        return self

    def __next__(self) -> Any:
        """
        Returns the next value from the queue iterator.

        :return: the next value from the queue iterator
        :rtype: Any
        :raises StopIteration: if there are no more items to return
        """
        if not self.__current:
            self.__current = self.__first
            raise StopIteration
        item = self.__current.value
        self.__current = self.__current.next_node
        return item

    def __str__(self) -> str:
        """
        Returns a string representation of the queue.

        :return: a string representation of the queue
        :rtype: str
        """
        return f"SimpleQueue({[node for node in self]})"


class SimpleStack:
    """
    Class that represents a stack.
    """

    def __init__(self, value: Any = None) -> None:
        """
        Constructor of the class.
        Initializes a new instance of SimpleStack.

        :param value: the initial value to push onto the stack, default is None
        :type value: Any
        """
        self.__items = list()
        self.__index = -1
        self.__next_index = -1

        if value:
            if isinstance(value, Collection):
                for item in value:
                    self.push(item)
            else:
                self.push(value)

    def push(self, value: Any) -> None:
        """
        Pushes a new value onto the stack.

        :param value: the value to push
        :type value: Any
        """
        self.__items.append(value)
        self.__index += 1
        self.__next_index = self.__index

    def pull(self) -> Any:
        """
        Pulls a value from the stack.

        :return: the pulled value.
        :rtype: Any
        :raises IndexError: if the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is already empty")

        self.__index -= 1
        self.__next_index = self.__index
        return self.__items.pop()

    def peek(self) -> Any:
        """
        Returns the value at the top of the stack without removing it.

        :return: the value at the top of the stack
        :rtype: Any
        :raises IndexError: if the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.__items[self.__index]

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        :return: True if the stack is empty, False otherwise
        :rtype: bool
        """
        return len(self.__items) == 0

    def __len__(self) -> int:
        """
        Returns the length of the stack.

        :return: the length of the stack
        :rtype: int
        """
        return len(self.__items)

    def __iter__(self) -> Iterator[Any]:
        """
        Returns an iterator for the stack.

        :return: an iterator for the stack
        :rtype: Iterator[Any]
        """
        return self

    def __next__(self) -> Any:
        """
        Returns the next value from the stack iterator.

        :return: the next value from the stack iterator
        :rtype: Any
        :raises StopIteration: if there are no more items to return
        """
        if self.__next_index < 0:
            self.__next_index = len(self.__items) - 1
            raise StopIteration
        item = self.__items[self.__next_index]
        self.__next_index -= 1
        return item

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        :return: a string representation of the stack
        :rtype: str
        """
        return f"SimpleStack({[item for item in self]})"


class Node:
    """
    Class that represents a node in a data structure (like a linked list or a tree).
    Each node has a value and pointers to the next and previous nodes.
    """

    def __init__(self, value: Any) -> None:
        """
        Constructor of the class.
        Initializes a new instance of Node.

        :param value: the initial value of the node
        :type value: Any
        """
        self.value = value
        self.next_node = None
        self.previous_node = None

    @property
    def value(self) -> Any:
        """
        Getter for the value of the node.

        :return: the value of the node
        :rtype: Any
        """
        return self.__value

    @value.setter
    def value(self, value: Any) -> None:
        """
        Setter for the value of the node.
        :param value: the new value for the node
        :type value: Any
        """
        self.__value = value

    @property
    def next_node(self) -> Any:
        """
        Getter for the next node.

        :return: the next node
        :rtype: Any
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node: Any) -> None:
        """
        Setter for the next node.

        :param next_node: the new next node
        :type next_node: Any
        """
        self.__next_node = next_node

    @property
    def previous_node(self) -> Any:
        """
        Getter for the previous node.

        :return: the previous node
        :rtype: Any
        """
        return self.__previous_node

    @previous_node.setter
    def previous_node(self, previous_node: Any) -> None:
        """
        Setter for the previous node.

        :param previous_node: the new previous node
        :type previous_node: Any
        """
        self.__previous_node = previous_node

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.

        :return: a string representation of the node
        :rtype: str
        """
        return f"Node({self.value})"

    def __eq__(self, other: 'TreeNode') -> bool:
        """
        Checks if the current node is equal to the other node.

        :param other: the other node to compare with
        :type other: TreeNode
        :return: True if the nodes are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, TreeNode):
            return self.value == other.value
        return False

    def __lt__(self, other: 'TreeNode') -> bool:
        """
        Checks if the current node is less than the other node.

        :param other: the other node to compare with
        :type other: TreeNode
        :return: True if the current node is less than the other node, False otherwise
        :rtype: bool
        """
        if isinstance(other, TreeNode):
            return self.value < other.value
        return False

    def __gt__(self, other: 'TreeNode') -> bool:
        """
        Checks if the current node is greater than the other node.

        :param other: the other node to compare with
        :type other: TreeNode
        :return: True if the current node is greater than the other node, False otherwise
        :rtype: bool
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

        :param value: the initial value of the node
        :type value: Any
        :param left: the left child of the node, default is None
        :type left: Union['TreeNode', None]
        :param right: the right child of the node, default is None
        :type right: Union['TreeNode', None]
        :param color: the color of the node, default is RED
        :type color: 'TreeNode.TreeNodeUtils'
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

        :return: the color of the node
        :rtype: TreeNode.TreeNodeUtils
        """
        return self.__color

    @color.setter
    def color(self, color: TreeNodeUtils) -> None:
        """
        Setter for the color of the node.

        :param color: the new color for the node
        :type color: TreeNode.TreeNodeUtils
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

        :return: the left child of the node
        :rtype: Any
        """
        return self.__left

    @left.setter
    def left(self, node: 'TreeNode') -> None:
        """
        Setter for the left child of the node.

        :param node: the new left child for the node
        :type node: 'TreeNode'
        """
        self.__left = node

    @property
    def right(self) -> Any:
        """
        Getter for the right child of the node.

        :return: the right child of the node
        :rtype: Any
        """
        return self.__right

    @right.setter
    def right(self, node: 'TreeNode') -> None:
        """
        Setter for the right child of the node.

        :param node: the new right child for the node
        :type node: 'TreeNode'
        """
        self.__right = node

    def __str__(self) -> str:
        """
        Returns a string representation of the node.

        :return: a string representation of the node
        :rtype: str
        """
        left = self.left if self.left is None else self.left.value
        right = self.right if self.right is None else self.right.value
        return f"({self.value}: {left}, {right})"

    def __repr__(self) -> str:
        """
        Returns a string representation of the node for debugging.

        :return: a string representation of the node
        :rtype: str
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
        :rtype: bool
        """
        return self.__size == 0

    def add(self, value: Any) -> bool:
        """
        Inserts a new value into the RedBlackTree.

        :param value: the value to insert
        :type value: Any
        :return: False if the value already exists in the tree, True otherwise
        :rtype: bool
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

    def remove(self, value) -> bool:
        """
        Deletes a value from the RedBlackTree.

        :param value: the value to delete
        :type value: Any
        :return: False if the value does not exist in the tree, True otherwise
        :rtype: bool
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

    def clear(self) -> None:
        """
        Clears the RedBlackTree.
        """
        self.__root = self._NULL
        self.__size = 0

    def size(self) -> int:
        """
        Returns the size of the RedBlackTree.

        :return: the size of the RedBlackTree
        :rtype: int
        """
        return self.__size

    def __fix_after_insertion(self, node: TreeNode) -> None:
        """
        Fixes the RedBlackTree after an insertion operation.

        :param node: the node that was inserted
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

        :param node: the node to perform the rotation on
        :type node: TreeNode
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

        :param node: The node to perform the rotation on
        :type node: TreeNode
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

    def __fix_after_deletion(self, node) -> None:
        """
        Fixes the RedBlackTree after a deletion operation.

        :param node: the node that was deleted
        :type node: TreeNode
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

    def __replace(self, node: TreeNode, other: TreeNode) -> None:
        """
        Replaces a node with another node.

        :param node: the node to be replaced
        :type node: TreeNode
        :param other: the node to replace with
        :type other: TreeNode
        """
        if not node.parent:
            self.__root = other
        elif node == node.parent.left:
            node.parent.left = other
        else:
            node.parent.right = other
        other.parent = node.parent

    def __symmetrical_successor(self, node) -> TreeNode:
        """
        Finds the symmetrical successor of a node.

        :param node: the node to find the symmetrical successor of
        :type node: TreeNode
        :return: the symmetrical successor of the node
        :rtype: TreeNode
        """
        while node.left is not self._NULL:
            node = node.left
        return node

    def __contains(self, value) -> TreeNode:
        """
        Checks if the given value is contained in the current RedBlackTree and
        returns the TreeNode where it is contained or a leaf.

        :param value: the value to check
        :type value: Any
        :return: TreeNode having the searched value or a leaf
        :rtype: TreeNode
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

        :param inorder: if True the route will be in-order else reversed
        :type inorder: bool
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

        :param other: other instance to compare with
        :type other: Any
        :return: True if instances are equal else False
        :rtype: bool
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
        :return: an iterator over the RedBlackTree instance
        :return: Any
        """
        for node in self.__inorder(True):
            yield node.value

    def __reversed__(self) -> Any:
        """
        Method to iterate reversely over the RedBlackTree instance.

        :return: an iterator over the RedBlackTree instance
        :rtype: Any
        """
        for node in self.__inorder(False):
            yield node.value

    def __str__(self) -> str:
        """
        Returns a string representation of the current RedBlackTree.

        :return: RedBlackTree string representation
        :rtype: str
        """
        return f"{[value for value in self]}"

    def __contains__(self, value) -> bool:
        """
        Check if the given value is contained in the RedBlackTree or not.
        This method is called when using built-in operator 'in'.

        :param value: the value to check
        :type value: Any
        :return: True if it is contained else False
        :rtype: bool
        """
        return self.__contains(value).value == value

    def __len__(self) -> int:
        """
        Provides the length of the current RedBlackTree. It is used with the
        built-in method len().

        :return: the length of the RedBlackTree
        :rtype: int
        """
        return self.__size


if __name__ == "__main__":
    t = RedBlackTree()

    for i in range(10):
        t.add(i)

    print(t)
