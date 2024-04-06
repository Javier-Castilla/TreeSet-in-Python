from typing import *

from TreeNode import TreeNode


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


E = TypeVar('E')


class RedBlackTree:
    RED = TreeNode.Color.RED
    BLACK = TreeNode.Color.BLACK

    def __init__(self, elements: Sequence[E] = None) -> None:
        """
        Initialize an empty RedBlackTree if type is given or constructs one with the
        elements contained into the given sequence.
        """
        self.__root = self.__first = self.__last = None
        self.__size = 0

        if elements:
            for item in elements:
                self.add(item)

    def add(self, value: E) -> bool:
        """Inserts the given value into the RedBlackTree if value is not contained.

        :param: Value to insert into the RedBlackTree
        :return: True if the value have been added to the RedBlackTree else False
        :rtype: bool
        :raises AssertionError: If the given value's type does not match generic
        type
        """
        new_node = TreeNode(value, RedBlackTree.RED)

        if (parent := self.__contains(value)) != new_node:
            if not parent:
                self.__root = new_node
            elif new_node < parent:
                parent.left = new_node
            else:
                parent.right = new_node

            if parent:
                new_node.parent = parent

            if len(self) == 0:
                self.__first = self.__last = new_node
            else:

                self.__last.next_node = new_node
                new_node.previous_node = self.__last

        else:
            return False

        self.__size += 1
        self.__fix_insertion(new_node)
        return True

    def remove(self, value: E) -> bool:
        if self.is_empty() or (root := self.__contains(value)).value != value:
            return False

        successor = None
        if not root.left and not root.right:
            if len(self) == 1:
                self.__root = None
            else:
                if root < root.parent:
                    root.parent.left = None
                else:
                    root.parent.right = None
        else:
            successor = None
            current = root.right
            while current:
                successor = current
                current = current.left

            if successor:
                root.value = successor.value

                if successor.parent == root:
                    root.right = successor.right
                else:
                    successor.parent.left = successor.right

                if child := successor.right:
                    child.parent = successor.parent
            else:
                successor = root.left
                if root.parent:
                    root.parent.left = successor
                    successor.parent = root.parent
                else:
                    self.__root = successor

            if len(self) == 1:
                self.__first = self.__last = None
            else:
                if prev := root.previous_node:
                    prev.next_node = root.next_node
                if next := root.next_node:
                    next.previous_node = root.previous_node

        self.__size -= 1
        self.__fix_removal(successor if successor else root)
        return True

    def __contains(self, value: E) -> TreeNode:
        if not len(self):
            return self.__root

        parent = None
        root = self.__root

        while root:
            if root.value == value:
                return root

            parent = root
            root = root.left if value < root.value else root.right

        return parent

    def __fix_insertion(self, node: TreeNode) -> None:
        while node != self.__root and node.parent.color == RedBlackTree.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle and uncle.color == RedBlackTree.RED:
                    node.parent.color = RedBlackTree.BLACK
                    uncle.color = RedBlackTree.BLACK
                    node.parent.parent.color = RedBlackTree.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__left_rotation(node)

                    node.parent.color = RedBlackTree.BLACK
                    node.parent.parent.color = RedBlackTree.RED
                    self.__right_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle and uncle.color == RedBlackTree.RED:
                    node.parent.color = RedBlackTree.BLACK
                    uncle.color = RedBlackTree.BLACK
                    node.parent.parent.color = RedBlackTree.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__right_rotation(node)

                    node.parent.color = RedBlackTree.BLACK
                    node.parent.parent.color = RedBlackTree.RED
                    self.__left_rotation(node.parent.parent)

        self.__root.color = RedBlackTree.BLACK

    def __fix_removal(self, node: TreeNode) -> None:
        while node != self.__root and (not node or node.color == RedBlackTree.BLACK):
            if not node.parent:
                break

            if node == node.parent.left:
                sibling = node.parent.right
                if not sibling:

                    break

                if sibling and sibling.color == RedBlackTree.RED:
                    sibling.color = RedBlackTree.BLACK
                    node.parent.color = RedBlackTree.RED
                    self.__left_rotation(node.parent)
                    sibling = node.parent.right

                if ((not sibling.right or sibling.right.color == RedBlackTree.BLACK) and
                        (not sibling.left or sibling.left.color == RedBlackTree.BLACK)):
                    sibling.color = RedBlackTree.RED
                    node = node.parent
                else:
                    if not sibling.right or sibling.right.color == RedBlackTree.BLACK:
                        sibling.left.color = RedBlackTree.BLACK if sibling.left else None
                        sibling.color = RedBlackTree.RED
                        self.__right_rotation(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = RedBlackTree.BLACK
                    sibling.right.color = RedBlackTree.BLACK if sibling.right else None
                    self.__left_rotation(node.parent)
                    node = self.__root
            else:
                sibling = node.parent.left
                if not sibling:
                    break

                if sibling and sibling.color == RedBlackTree.RED:
                    sibling.color = RedBlackTree.BLACK
                    node.parent.color = RedBlackTree.RED
                    self.__right_rotation(node.parent)
                    sibling = node.parent.left

                if ((not sibling.right or sibling.right.color == RedBlackTree.BLACK) and
                        (not sibling.left or sibling.left.color == RedBlackTree.BLACK)):
                    sibling.color = RedBlackTree.RED
                    node = node.parent
                else:
                    if not sibling.left or sibling.left.color == RedBlackTree.BLACK:
                        sibling.right.color = RedBlackTree.BLACK if sibling.right else None
                        sibling.color = RedBlackTree.RED
                        self.__left_rotation(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = RedBlackTree.BLACK
                    sibling.left.color = RedBlackTree.BLACK if sibling.left else None
                    self.__right_rotation(node.parent)
                    node = self.__root

        if node:
            node.color = RedBlackTree.BLACK

    def __left_rotation(self, node: TreeNode) -> None:
        other = node.right
        node.right = other.left

        if other.left:
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

        if other.right:
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

    def first(self) -> E:
        for node in self.__inorder(False):
            return node.value

    def last(self) -> E:
        for node in self.__inorder(True):
            return node.value

    def __get_contiguous(self, value: E, higher: bool) -> Union[E, None]:
        if (value != (self.first() if not higher else self.last())
                and (root := self.__contains(value)).value == value):
            parent = None
            current = root.left if not higher else root.right
            while current:
                parent = current
                current = current.right if not higher else current.left

            if parent:
                current = parent
            else:
                current = root.parent
                while current and (
                        (current.value >= root.value) if not higher
                        else (current.value <= root.value)
                ):
                    current = current.parent

            return current.value if current.value != root.value else None
        else:
            return None

    def __insertion_order(self):
        current = self.__first
        while current:
            yield current
            current = current.next_node

    def __len__(self) -> int:
        return self.__size

    def __iter__(self) -> E:
        for node in self.__inorder(False):
            yield node.value

    def __reversed__(self) -> E:
        for node in self.__inorder(True):
            yield node.value

    def __inorder(self, reversed: bool) -> E:
        stack = SimpleStack()
        current = self.__root

        while True:
            if current:
                stack.push(current)
                current = current.left if not reversed else current.right
            elif not stack.is_empty():
                current = stack.pull()
                yield current
                current = current.right if not reversed else current.left
            else:
                break

    def __str__(self) -> str:
        return f"{[str(value) for value in self]}"

    def __contains__(self, value) -> bool:
        return self.__contains(value).value == value

    def __eq__(self, other) -> bool:
        if isinstance(other, RedBlackTree):
            for node in self.__insertion_order():
                if node.value not in other:
                    return False

            return True
        else:
            return False