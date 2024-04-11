"""
TreeSet module.

This module provides a TreeSet class for storing and managing a set of elements
in a red-black tree data structure.
"""

from random import randint
from data_utils import *

E = TypeVar('E')


class TreeSet:
    """Class that represents a set based on a tree. The elements are ordered
    using its natural ordering.

    Since this implementation uses a Red-Black Tree, it provides guaranteed
    log(n) time cost for the basic operations.

    TreeSet string representation will be provided inorder.
    """

    RED = TreeNode.Color.RED
    BLACK = TreeNode.Color.BLACK

    def __init__(self, class_type: Union[E, Sequence[E]]) -> None:
        """
        Initialize an empty TreeSet if type is given or constructs one with the
        elements contained into the given sequence.

        :param class_type: The generic type of the class or a sequence with
        element to construct the TreeSet
        :type class_type: Union[E, Sequence[E]]
        """
        self.__root = self.__first = self.__last = None
        self.__size = 0

        if isinstance(class_type, Sequence):
            if len(set(map(type, class_type))) != 1:
                raise TypeError("Sequence elements type must be the same")

            self.class_type = type(class_type[0])

            for item in class_type:
                self.add(item)
        else:
            self.class_type = class_type

    def add(self, value: E) -> bool:
        """Inserts the given value into the TreeSet if value is not contained.

        :param value: Value to insert into the TreeSet
        :type value: E
        :return: True if the value have been added to the TreeSet else False
        :rtype: bool
        :raises AssertionError: If the given value's type does not match generic
        type
        """
        assert isinstance(value, self.class_type), \
            f"Value type must be '{self.class_type}'"

        new_node = TreeNode(value, TreeSet.RED)

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

    def add_all(self, sequence: Sequence[E]) -> bool:
        """Inserts the given values into the TreeSet. If some value is
        already contained, it will not be inserted.

        :param sequence: Values to insert into the TreeSet
        :type sequence: Sequence[E]
        :return: True if the value has been added to the TreeSet else False
        :rtype: bool
        :raises AssertionError: If the given value's type does not match generic
        type
        """
        old_size = len(self)
        for item in sequence:
            self.add(item)

        return len(self) != old_size

    def remove(self, value: E) -> bool:
        """Deletes the given value from the TreeSet if contained.

        :param value: Value to delete
        :type value: E
        :return: True if value could be deleted else False
        :rtype: bool
        """
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

    def clear(self) -> None:
        """Clears the TreeSet from all its inserted elements."""
        self.__root = None

    def clone(self) -> 'TreeSet':
        """Clones the current TreeSet and returns that clone.

        :return: A shallow copy of the current TreeSet instance
        :rtype: TreeSet
        """
        return TreeSet([node for node in self])

    def is_empty(self) -> bool:
        """Checks if the current TreeSet is empty or not.

        :return: True if TreeSet is empty else False
        :rtype: bool
        """
        return len(self) == 0

    def contains(self, value: E) -> bool:
        """Checks if a given value is contained into the current TreeSet
        instance.

        :param value: To check if it is contained
        :type value: E
        :return: True if value is contained else False
        :rtype: bool
        """
        return value in self

    def first(self) -> E:
        """Returns the lowest element contained in the current TreeSet instance.

        :return: Lowest contained element
        :rtype: E
        """
        for node in self.__inorder(False):
            return node.value

    def last(self) -> E:
        """Return the greatest element contained in the current TreeSet instance.

        :return: Greatest contained element
        :rtype: E
        """
        for node in self.__inorder(True):
            return node.value

    def iterator(self) -> Iterator[E]:
        """Provides an iterator of the current TreeSet instance elements.

        :return: TreeSet elements iterator
        :rtype: Iterator[E]
        """
        return iter(self)

    def descending_iterator(self) -> Iterator[E]:
        """Provides a descending iterator of the current TreeSet instance
        elements.

        :return: TreeSet elements descending iterator
        :rtype: Iterator[E]
        """
        return iter(reversed(self))

    def lower(self, value: E) -> Union[E, None]:
        """Returns the contiguous lower element of the given value from the
        TreeSet.

        :param value: Value to compare
        :return: Greatest element lower than the given value. If it was not
            possible, None will be returned.
        :rtype: Union[E, None]
        """
        return self.__get_contiguous(value, False)

    def higher(self, value: E) -> Union[E, None]:
        """Returns the contiguous greater element of the given value from the
        TreeSet.

        :param value: Value to compare
        :return: Lowest element greater than the given value. If it was not
            possible, None will be returned.
        :rtype: Union[E, None]
        """
        return self.__get_contiguous(value, True)

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
        while node != self.__root and node.parent.color == TreeSet.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle and uncle.color == TreeSet.RED:
                    node.parent.color = TreeSet.BLACK
                    uncle.color = TreeSet.BLACK
                    node.parent.parent.color = TreeSet.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__left_rotation(node)

                    node.parent.color = TreeSet.BLACK
                    node.parent.parent.color = TreeSet.RED
                    self.__right_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle and uncle.color == TreeSet.RED:
                    node.parent.color = TreeSet.BLACK
                    uncle.color = TreeSet.BLACK
                    node.parent.parent.color = TreeSet.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__right_rotation(node)

                    node.parent.color = TreeSet.BLACK
                    node.parent.parent.color = TreeSet.RED
                    self.__left_rotation(node.parent.parent)

        self.__root.color = TreeSet.BLACK

    def __fix_removal(self, node: TreeNode) -> None:
        while node != self.__root and (not node or node.color == TreeSet.BLACK):
            if not node.parent:
                # Si el padre de node es None, salimos del bucle
                break

            if node == node.parent.left:
                sibling = node.parent.right
                if not sibling:
                    # Si no hay hermano, salimos del bucle
                    break

                if sibling and sibling.color == TreeSet.RED:
                    sibling.color = TreeSet.BLACK
                    node.parent.color = TreeSet.RED
                    self.__left_rotation(node.parent)
                    sibling = node.parent.right

                if not sibling:
                    break

                if ((
                        not sibling.right or sibling.right.color == TreeSet.BLACK) and
                        (
                                not sibling.left or sibling.left.color == TreeSet.BLACK)):
                    sibling.color = TreeSet.RED
                    node = node.parent
                else:
                    if not sibling.right or sibling.right.color == TreeSet.BLACK:
                        sibling.left.color = TreeSet.BLACK if sibling.left else None
                        sibling.color = TreeSet.RED
                        self.__right_rotation(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = TreeSet.BLACK
                    sibling.right.color = TreeSet.BLACK if sibling.right else None
                    self.__left_rotation(node.parent)
                    node = self.__root
            else:
                sibling = node.parent.left
                if not sibling:
                    # Si no hay hermano, salimos del bucle
                    break

                if sibling and sibling.color == TreeSet.RED:
                    sibling.color = TreeSet.BLACK
                    node.parent.color = TreeSet.RED
                    self.__right_rotation(node.parent)
                    sibling = node.parent.left

                if not sibling:
                    break

                if ((
                        not sibling.right or sibling.right.color == TreeSet.BLACK) and
                        (
                                not sibling.left or sibling.left.color == TreeSet.BLACK)):
                    sibling.color = TreeSet.RED
                    node = node.parent
                else:
                    if not sibling.left or sibling.left.color == TreeSet.BLACK:
                        sibling.right.color = TreeSet.BLACK if sibling.right else None
                        sibling.color = TreeSet.RED
                        self.__left_rotation(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = TreeSet.BLACK
                    sibling.left.color = TreeSet.BLACK if sibling.left else None
                    self.__right_rotation(node.parent)
                    node = self.__root

        if node:
            node.color = TreeSet.BLACK

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
        return f"{[value for value in self]}"

    def __contains__(self, value) -> bool:
        return self.__contains(value).value == value

    def __eq__(self, other) -> bool:
        if isinstance(other, TreeSet):
            for node in self:
                if node.value not in other:
                    return False

            return True
        else:
            return False
    def pollFirst(self):
        if self.is_empty():
            return None
        else:
            first_value = next(self.iterator())
            self.remove(first_value)
            return first_value

if __name__ == "__main__":
    # items = [randint(1, 100) for _ in range(10)]
    items = [8, 93, 18, 5, 32, 82, 78, 5, 6, 13, 20, 35, 92, 86, 95]
    t = TreeSet(items)
    print(t)
    print(t.clone())
    print("Eliminar el primer elemento")
    while not t.is_empty():
        print("Árbol antes de eliminar el primer elemento:", t)
        print("Elemento eliminado:", t.pollFirst())
