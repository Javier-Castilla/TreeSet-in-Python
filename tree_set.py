"""
tree_set module.

This module provides a TreeSet class for storing and managing a set of elements
in a red-black tree data structure. It also provides its base class, a
RedBlackTree class, which is a self-balancing binary search tree. The TreeSet
class extends the RedBlackTree class and provides additional methods for
managing the set of elements.
"""
from typing import *
from data_utils import TreeNode, SimpleStack
from tests.tests_classes import *
from tree_set_exceptions import *
import random

E = TypeVar('E')


class RedBlackTree:
    """
    Class that represents a Red-Black Tree, a self-balancing binary search
    tree. It provides guaranteed *O(log n)* time cost for the basic operations.
    If needed to use a self-balancing tree with more operations, it is
    recommended to use the :class:`TreeSet` class.
    """

    __attributes = {
        "_RedBlackTree__root", "_RedBlackTree__size",
        "_RedBlackTree__object_type"
    }

    _RED = TreeNode.TreeNodeUtils.RED
    _BLACK = TreeNode.TreeNodeUtils.BLACK
    _NULL = TreeNode(TreeNode.TreeNodeUtils.NULL, None, None,
                     TreeNode.TreeNodeUtils.BLACK)

    def _type_validation(function):
        """
        Decorator method used to validate item type when using a TreeSet.

        :param function: used function of the TreeSet
        :return: given function return statement
        :raises TypeError: if the item type does not match the TreeSet type
        """

        def wrapper(self, item):
            """
            Wrapper function used to validate the item type.

            :param self: the instance of the current TreeSet
            :type self: TreeSet
            :param item:  item to validate
            :type item: E
            :return: the given function return statement
            :rtype: Any
            :raises TypeError: if the item type does not match the TreeSet type
            """
            if not isinstance(item, self.object_type):
                raise TypeError(
                    f"Value type must be '{self.object_type}: {type(item)}'")

            return function(self, item)

        return wrapper

    def _null_validation(function):
        """
        Decorator used to validate if the given value is None or not.

        :param function: used function of the TreeSet
        :return: given function return statement
        :raises NullPointerException: if the item is None
        """

        def wrapper(self, value):
            """
            Wrapper function used to validate if the given value is None or not.

            :param self: the instance of the current TreeSet
            :type self: TreeSet
            :param value: value to validate
            :type value: E
            :return: the given function return statement
            :rtype: Any
            :raises NullPointerException: if the item is None
            """
            if value is None:
                raise NullPointerException("Value cannot be None")
            return function(self, value)

        return wrapper

    def _check_comparable(function):
        """
        Private decorator used to check comparability of the type specified when
        creating the TreeSet.

        :param function: used functions of the TreeSet
        :return: given function return statement
        :raise ClassCastException: if the given value is not comparable
        """

        def wrapper(self, *args):
            """
            Wrapper function used to check the comparability of the given value.

            :param self: the instance of the current TreeSet
            :param args: arguments given dynamically
            :return: the given function return statement
            :rtype: Any
            :raise ClassCastException: if the given value is not comparable
            """

            def throw_exception():
                """
                Private method used to throw a ClassCastException exception.

                :raises ClassCastException: always
                """
                raise ClassCastException(
                    f"class {value_type} cannot be compared")

            item = args[0]
            value_type = type(item)
            if value_type.__eq__ is object.__eq__ \
                    or (value_type.__lt__ is object.__lt__
                        and value_type.__gt__ is object.__gt__):
                throw_exception()
            elif not isinstance(item, type):
                try:
                    if (item < item) is None or (item > item) is None:
                        throw_exception()
                except TypeError:
                    throw_exception()

            return function(self, *args)

        return wrapper

    @classmethod
    def __complete_comparator(cls, value_type: Type):
        """
        Private method used to complete specified type comparator.
        If the given class has only one of the two lateral
        comparators, the other will be added to the class with
        the help of the one already implemented.

        :param value_type: the type to complete its comparator
        :type value_type: type
        :return: the given value type
        :rtype: Type
        """
        c_type = value_type.__base__ if value_type.__base__ is not object \
            else value_type

        if value_type.__lt__ is object.__lt__ \
                and value_type.__gt__ is not object.__gt__:
            setattr(value_type, f"_{value_type}__comparator_class", c_type)

            def __lt__(s, other):
                if s == other:
                    return False
                else:
                    return not s.__gt__(other)

            setattr(value_type, '__lt__', __lt__)
        elif value_type.__gt__ is object.__gt__ \
                and value_type.__lt__ is not object.__lt__:
            setattr(value_type, f"_{value_type}__comparator_class", c_type)

            def __gt__(s, other):
                if s == other:
                    return False
                else:
                    return not s.__lt__(other)

            setattr(value_type, '__gt__', __gt__)

        return value_type

    def __init__(self, generic_type: Type) -> None:
        """
        Constructor of the class.
        Initializes a new instance of RedBlackTree.
        """
        self.__root = self._NULL
        self.__size = 0
        self.__object_type = self.__complete_comparator(generic_type)

    @property
    def object_type(self) -> Type:
        """
        Getter method to retrieve the TreeSet object type.

        :return: the TreeSet object type
        :rtype: Type
        """
        return self.__object_type

    @_null_validation
    @_type_validation
    @_check_comparable
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

    @_null_validation
    @_type_validation
    @_check_comparable
    def remove(self, value) -> bool:
        """
        Deletes a value from the RedBlackTree.

        :param value: the value to delete
        :type value: Any
        :return: False if the value does not exist in the tree, True otherwise
        :rtype: bool
        """
        if (
                node := self.__contains(
                    value)) is self._NULL or node.value != value:
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

        :return: the size of the RedBlackTree
        :rtype: int
        """
        return self.__size

    def is_empty(self) -> bool:
        """
        Checks if the current RedBlackTree is empty or not.

        :return: True if RedBlackTree is empty else False
        :rtype: bool
        """
        return self.__size == 0

    def clear(self) -> None:
        """
        Clears the RedBlackTree.
        """
        self.__root = self._NULL
        self.__size = 0

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

    def __nodes_color_arrays(self):
        """
        Returns the colors of the nodes in the RedBlackTree.

        :return: the colors of the nodes in the RedBlackTree
        :rtype: List[str]
        """
        colors = []
        for node in self.__inorder(True):
            colors.append(node.color)

        return colors

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

    @_null_validation
    @_type_validation
    @_check_comparable
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

    def __setattr__(self, key, value) -> None:
        """
        Method called when trying to set a value to an attribute that does not
        exist. Once the class is created, new attributes cannot be added.

        :param key: name of the attribute
        :type key: Any
        :param value: value to assign to the attribute
        :raises AttributeError: if trying to add a new attribute dynamically
        """
        if key not in self.__attributes:
            raise AttributeError(
                f"Cannot add more attributes to this instance {key}")
        super().__setattr__(key, value)


class TreeSet(RedBlackTree):
    """
    Class that represents a set based on a tree. The elements are ordered
    using its natural ordering.

    Since this implementation uses a Red-Black Tree, it provides guaranteed
    *O(log n)* time cost for the basic operations.

    TreeSet string representation will be provided inorder.
    """

    def __init__(self, generic_type: Type,
                 sequence: Collection[E] = None) -> None:
        """
        Initialize an empty TreeSet if type is given or constructs one with the
        elements contained into the given collection.

        :param generic_type: the generic type of the class
        :type generic_type: type
        :param: sequence: a collection to take items from and add them to
            the TreeSet
        :type sequence: Collection[E]
        :raises TypeError: if the given values does not match the instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        super().__init__(generic_type)

        if not sequence:
            return

        if not isinstance(sequence, Collection):
            raise TypeError(
                f"Second argument must be a sequence but {type(sequence)} was given"
            )

        self.add_all(sequence)

    def add_all(self, values: Collection[E]) -> bool:
        """
        Inserts the given values into the current TreeSet. If the type of some
        value does not match the instance TreeSet type, an exception will
        be thrown, and no element will be added.

        :param values: values to insert into the TreeSet.
        :type values: Collection[E]
        :return: True if all values could be inserted else False
        :rtype: bool
        :raises TypeError: if the given values does not match the
            instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        if not isinstance(values, Collection):
            raise TypeError(
                f"Second argument must be a sequence but {type(values)} was given"
            )

        for value in values:
            if value is None:
                raise NullPointerException("Value cannot be None")

            if not isinstance(value, self.object_type):
                raise TypeError(
                    f"Value type must be '{self.object_type}: {type(value)}'")

        old_size = self.size()
        for value in values:
            super().add(value)

        return old_size == self.size() - len(values)

    def clone(self) -> 'TreeSet':
        """
        Clones the current TreeSet and returns that clone.

        :return: a shallow copy of the current TreeSet instance.
        :rtype: TreeSet
        """
        return TreeSet(self.object_type, self)

    def contains(self, value: E) -> bool:
        """
        Checks if a given value is contained into the current TreeSet
        instance. If the given value type does not match the TreeSet type
        and exception will be thrown.

        :param value: to check if it is contained
        :type value: E
        :return: True if value is contained else False
        :rtype: bool
        :raises TypeError: if the given values does not match the
            instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        return value in self

    @RedBlackTree._null_validation
    @RedBlackTree._type_validation
    @RedBlackTree._check_comparable
    def higher(self, value: E) -> Union[E, None]:
        """
        Returns the next higher value in the tree compared to the given
        value.

        :param value: value to compare
        :return: the next higher value in the tree compared to the given value
        :rtype: Union[E, None]
        :raises TypeError: if the given values does not match the
            instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        current = self._RedBlackTree__root
        result = None

        while current is not RedBlackTree._NULL:
            if current.value > value:
                result = current.value
                current = current.left
            else:
                current = current.right

        return result

    @RedBlackTree._null_validation
    @RedBlackTree._type_validation
    @RedBlackTree._check_comparable
    def lower(self, value: E) -> Union[E, None]:
        """
        Returns the contiguous lower element of the given value from the
        TreeSet.

        :param value: value to compare
        :type value: E
        :return: the greatest element lower than the given value. If it was not
            found, None will be returned.
        :rtype: Union[E, None]
        :raises TypeError: if the given values does not match the
            instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        current = self._RedBlackTree__root
        result = None

        while current is not RedBlackTree._NULL:
            if current.value < value:
                result = current.value
                current = current.right
            else:
                current = current.left

        return result

    @RedBlackTree._null_validation
    @RedBlackTree._type_validation
    @RedBlackTree._check_comparable
    def ceiling(self, value: E) -> Union[E, None]:
        """
        Returns the least element in this set greater than
        or equal to the given element, or null if there is no
        such element.

        :param value: value to compare
        :type value: E
        :return: the least element in this set greater than or equal
            to the given element. If it was not found, None will be returned
        :rtype: TreeSet
        :raises TypeError: if the given values does not match the
            instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        current = self._RedBlackTree__root
        result = None

        while current is not RedBlackTree._NULL:
            if current.value == value:
                return value
            elif current.value > value:
                result = current.value
                current = current.left
            else:
                current = current.right

        return result

    @RedBlackTree._null_validation
    @RedBlackTree._type_validation
    @RedBlackTree._check_comparable
    def floor(self, value: E) -> Union[E, None]:
        """
        Returns the greatest element in this set less than or
        equal to the given element, or null if there is no such
        element.

        :param value: value to compare
        :type value: E
        :return: the greatest element in this set less than or
        equal to the given element
        :rtype: TreeSet
        :raises TypeError: if the given values does not match the
            instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        current = self._RedBlackTree__root
        result = None

        while current is not RedBlackTree._NULL:
            if current.value == value:
                return value
            elif current.value < value:
                result = current.value
                current = current.right
            else:
                current = current.left

        return result

    def first(self) -> E:
        """
        Returns the lowest element contained in the current TreeSet instance.

        :return: the lowest contained element
        :rtype: E
        :raises NoSuchElementException: if there is no such element
        """
        if self.is_empty():
            raise NoSuchElementException()

        return next(self.iterator())

    def last(self) -> E:
        """
        Return the greatest element contained in the current TreeSet
        instance.

        :return: the greatest contained element
        :rtype: E
        :raises NoSuchElementException: if there is no such element
        """
        if self.is_empty():
            raise NoSuchElementException()

        return next(self.descending_iterator())

    def poll_first(self) -> E:
        """
        Retrieves and removes the first (lowest) element, or returns None
        if this set is empty.

        :return: the first (lowest) element, or None if this set is empty
        :rtype: Union[E, None]
        :raises NoSuchElementException: if there is no such element
        """
        try:
            self.remove(item := self.first())
            return item
        except NoSuchElementException:
            return None

    def poll_last(self) -> E:
        """
        Retrieves and removes the first (lowest) element, or returns None
        if this set is empty.

        :return: the first (lowest) element, or None if this set is empty
        :rtype: Union[E, None]
        :raises NoSuchElementException: if there is no such element
        """
        try:
            self.remove(item := self.last())
            return item
        except NoSuchElementException:
            return None

    def iterator(self) -> Iterator[E]:
        """
        Provides an iterator of the current TreeSet instance elements.

        :return: TreeSet elements iterator
        :rtype: Iterator[E]
        """
        return iter(self)

    def descending_iterator(self) -> Iterator[E]:
        """
        Provides a descending iterator of the current TreeSet instance
        elements.

        :return: TreeSet elements descending iterator
        :rtype: Iterator[E]
        """
        return iter(reversed(self))


if __name__ == "__main__":
    items = list(range(150))
    tree = TreeSet(int, items)
    print(tree)
