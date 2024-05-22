"""
TreeSet module.

This module provides a TreeSet class for storing and managing a set of elements
in a red-black tree data structure.
"""
import random
from data_utils import *
from tests.tests_classes import *
from tree_set_exceptions import *

E = TypeVar('E')


class TreeSet(RedBlackTree):
    """
    Class that represents a set based on a tree. The elements are ordered
    using its natural ordering.

    Since this implementation uses a Red-Black Tree, it provides guaranteed
    *O*\ (log *n*) time cost for the basic operations.

    TreeSet string representation will be provided inorder.
    """

    __attributes = {
        "_RedBlackTree__root", "_RedBlackTree__size",
        "_TreeSet__class_type", "iterations", "count"
    }

    def __type_validation(function):
        """
        Decorator used to validate item type when adding or deleting it from a TreeSet.
        This decorator should not be used with other object instance but a TreeSet.

        :param function: used function of the TreeSet
        :return: given function return statement
        :raises TypeError: if the item type does not match the TreeSet type
        """

        def wrapper(self, item):
            if not isinstance(item, self.__class_type):
                raise TypeError(
                    f"Value type must be '{self.__class_type}: {type(item)}'")

            return function(self, item)

        return wrapper

    def __null_validation(function):
        """
        Decorator used to validate if the given value is None or not.

        :param function: used function of the TreeSet
        :return: given function return statement
        :raises NullPointerException: if the item is None
        """
        def wrapper(self, value):
            if value is None:
                raise NullPointerException("Value cannot be None")
            return function(self, value)

        return wrapper

    def __check_comparable(function):
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

    def __init__(self, generic_type: Type,
                 sequence: Collection[E] = None) -> None:
        """
        Initialize an empty TreeSet if type is given or constructs one with the
        elements contained into the given collection.

        :param generic_type: the generic type of the class
        :type generic_type: type
        :param: sequence: a collection to take items from and add them to the TreeSet
        :type sequence: Collection[E]
        :raises TypeError: if the given values does not match the instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        super().__init__()
        self.__class_type = self.__complete_comparator(generic_type)

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

        if len(set(map(type, values))) > 1:
            raise TypeError(
                f"All values must be of the same type: {self.__class_type}"
            )

        old_size = self.size()
        for value in values:
            self.add(value)

        return old_size == self.size() - len(values)

    @__null_validation
    @__type_validation
    @__check_comparable
    def add(self, value: E) -> bool:
        """
        Inserts the given value into the current TreeSet. If the type of
        the value does not match the instance TreeSet type, an exception will
        be thrown.

        :param value: value to insert into the TreeSet
        :type value: E
        :return: True if the value could be inserted else False
        :rtype: bool
        :raises TypeError: if the given value does not match the
            instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        return super().add(value)

    @__null_validation
    @__type_validation
    @__check_comparable
    def remove(self, value: E) -> bool:
        """
        Removes the given value from the current TreeSet. If the type of
        the value does not match the instance TreeSet type, an exception will
        be thrown.

        :param value: value to remove from the TreeSet
        :type value: E
        :return: True if the value could be removed else False
        :rtype: bool
        :raises TypeError: if the given values does not match the
            instance type
        :raises NullPointerException: if the given value is None
        :raises ClassCastException: if the given value is not comparable
        """
        return super().remove(value)

    def size(self) -> int:
        """
        Provides the size of the current TreeSet.

        :return: size of the TreeSet instance
        :rtype: int
        """
        return super().size()

    def clear(self) -> None:
        """
        Clears the TreeSet from all its inserted elements.
        """
        super().clear()

    def clone(self) -> 'TreeSet':
        """
        Clones the current TreeSet and returns that clone.

        :return: a shallow copy of the current TreeSet instance.
        :rtype: TreeSet
        """
        return TreeSet(self.__class_type, self)

    def is_empty(self) -> bool:
        """
        Checks if the current TreeSet is empty or not.

        :return: True if TreeSet is empty else False
        :rtype: bool
        """
        return self.size() == 0

    @__null_validation
    @__type_validation
    @__check_comparable
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

    @__null_validation
    @__type_validation
    @__check_comparable
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

    @__null_validation
    @__type_validation
    @__check_comparable
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

    @__null_validation
    @__type_validation
    @__check_comparable
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

    @__null_validation
    @__type_validation
    @__check_comparable
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
        :raises NoSuchElementError: if there is no such element
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
        :raises NoSuchElementError: if there is no such element
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
        :raises NoSuchElementError: if there is no such element
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
        :raises NoSuchElementError: if there is no such element
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

    def __get_color(self, value):
        return node.color if (node := self._RedBlackTree__contains(
            value)).value == value \
            else None

    def __array_color(self):
        return [self.__get_color(value) for value in self]


if __name__ == "__main__":
    items = [i for i in range(10, 30)]
    # items = ["a", "b", "c", "d", "d", "f", "g", "h", "i", "j", "k", "l",
    # "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    tree = TreeSet(Worker)
    print(tree.add(Worker("Juan", 20, "job1")))
    print(tree)
    tree.add(worker := LazyWorker("Juan", 20, "job1", 1000))


    def loop_test():
        t = TreeSet(int)
        for _ in range(10):
            items = [random.randint(1, 1000) for _ in range(10)]
            t = TreeSet(int, items)
            print("Items", items)
            print("Tree:", t)
            print(t.ceiling(400))
            print("===================")
            # t.draw_tree()

    # loop_test()
