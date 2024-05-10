"""
TreeSet module.

This module provides a TreeSet class for storing and managing a set of elements
in a red-black tree data structure.
"""

from random import randint

import pruebas
from data_utils import *
from treeset_exceptions import *
import matplotlib.pyplot as plt
import tkinter as tk

from tests.tests_classes import *

E = TypeVar('E')


class TreeSetDrawing:

    def __init__(self, tree: 'TreeSet') -> None:
        self.__tree = tree
        self.draw_tree()

    def draw_tree(self):
        root = tk.Tk()
        root.title("Árbol Rojo-Negro")
        root.geometry("230x350")
        root.resizable(False, False)

        value = tk.StringVar()
        value.set("")

        label = tk.Label(root, text="Nodo:")
        label.grid(row=0, column=0)

        entry = tk.Entry(root, textvariable=value)
        entry.grid(row=1, column=0)

        buttons = list()

        insert = tk.Button(root, text="Insertar Valor",
                           command=lambda: (
                               self.__tree.add(int(value.get())),
                               plt.close('all'),
                               self.__draw()))
        buttons.append(insert)
        delete = tk.Button(root, text="Eliminar Valor",
                           command=lambda: (
                               self.__tree.remove(int(value.get())),
                               plt.close('all'),
                               self.__draw()))
        buttons.append(delete)
        clear = tk.Button(root, text="Borrar Árbol", command=lambda: (
            self.__tree.clear(), plt.close('all'), self.__draw()))
        buttons.append(clear)
        lower = tk.Button(root, text="Lower",
                          command=lambda: (
                              print(self.__tree.lower(int(value.get())))))
        buttons.append(lower)
        higher = tk.Button(root, text="Higher", command=lambda: (
            print(self.__tree.higher(int(value.get())))))
        buttons.append(higher)
        ceiling = tk.Button(root, text="Ceiling", command=lambda: (
            print(self.__tree.ceiling(int(value.get())))))
        buttons.append(ceiling)
        floor = tk.Button(root, text="Floor",
                          command=lambda: (
                              print(self.__tree.floor(int(value.get())))))
        buttons.append(floor)
        first = tk.Button(root, text="First",
                          command=lambda: (print(self.__tree.first())))
        buttons.append(first)
        last = tk.Button(root, text="Last",
                         command=lambda: (print(self.__tree.last())))
        buttons.append(last)
        poll_first = tk.Button(root, text="Poll First",
                               command=lambda: (
                                   print(self.__tree.poll_first()),
                                   plt.close('all'),
                                   self.__draw()))
        buttons.append(poll_first)
        poll_last = tk.Button(root, text="Poll Last",
                              command=lambda: (
                                  print(self.__tree.poll_last()),
                                  plt.close('all'),
                                  self.__draw()))
        buttons.append(poll_last)
        size = tk.Button(root, text="Size", command=lambda: (print(len(self))))
        buttons.append(size)
        random = tk.Button(root, text="Random Tree",
                           command=lambda: (plt.close('all'),
                                            self.__draw_random_tree(
                                                int(value.get())))
                           )
        buttons.append(random)

        row = 0
        for button in buttons:
            button.grid(row=row, column=1)
            row += 1

        root.mainloop()

    def __draw_random_tree(self, number):
        """items = ["a", "b", "c", "d", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        items = items[:int(number.get())]
        self.clear()
        #for item in [randint(1, 1000) for _ in range(int(number.get()))]:
        for item in items:
            self.add(item)
        self.__draw()"""
        self.__draw()

    def __draw(self):
        fig, ax = plt.subplots()
        fig.subplots_adjust(left=0, bottom=0, right=1,
                            top=1)  # Ajustar los márgenes del subplot
        self.__draw_node(ax, self.__tree._TreeSet__root)
        self.__draw_edges(ax, self.__tree._TreeSet__root)
        ax.axis('off')  # Ocultar ejes
        plt.show()

    def __draw_node(self, ax, node, x=0, y=0, dx=1, dy=1):
        if node is not self.__tree.__NULL:
            color = "red" if node.color == self.__tree._TreeSet__RED else "black"
            ax.plot([x], [y], marker='o', markersize=40, color=color,
                    zorder=2)  # Dibujar nodo con un tamaño mayor y detrás de las líneas
            ax.text(x, y, str(node.value), fontsize=12, ha='center',
                    va='center', color='white',
                    zorder=3)  # Etiquetar nodo
            if node.left is not self.__tree.__NULL:
                self.__draw_node(ax, node.left, x - dx, y - dy, dx / 2, dy * 2)
            if node.right is not self.__tree.__NULL:
                self.__draw_node(ax, node.right, x + dx, y - dy, dx / 2, dy * 2)

    def __draw_edges(self, ax, node, x=0, y=0, dx=1, dy=1):
        if node is not self.__tree.__NULL:
            if node.left is not self.__tree.__NULL:
                ax.plot([x, x - dx], [y, y - dy], color='black',
                        zorder=1)  # Dibujar conexión izquierda en negro y detrás de los nodos
                self.__draw_edges(ax, node.left, x - dx, y - dy, dx / 2, dy * 2)
            if node.right is not self.__tree.__NULL:
                ax.plot([x, x + dx], [y, y - dy], color='black',
                        zorder=1)  # Dibujar conexión derecha en negro y detrás de los nodos
                self.__draw_edges(ax, node.right, x + dx, y - dy, dx / 2,
                                  dy * 2)


class TreeSet:
    """Class that represents a set based on a tree. The elements are ordered
    using its natural ordering.

    Since this implementation uses a Red-Black Tree, it provides guaranteed
    log(n) time cost for the basic operations.

    TreeSet string representation will be provided inorder.
    """

    __RED = TreeNode.TreeNodeUtils.RED
    __BLACK = TreeNode.TreeNodeUtils.BLACK
    __attributes = {
        "_TreeSet__root", "_TreeSet__size",
        "_TreeSet__class_type", "_TreeSet__attributes",
        '_TreeSet__is_comparable', "iteraciones", "contar"
    }

    @staticmethod
    def __type_validation(function):
        """Decorator used to validate item type when adding or deleting it from a TreeSet.
        This decorator should not be used with other object instance but a TreeSet.

        :param function: function used of the TreeSet
        :return: function return statement
        """

        def wrapper(self, item):
            if not isinstance(item, self.__class_type):
                raise TypeError(
                    f"Value type must be '{self.__class_type}: {type(item)}'")

            return function(self, item)

        return wrapper

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
                        return False
                    return not self.__gt__(other)
                return False

            setattr(value_type, '__lt__', __lt__)
        elif value_type.__gt__ is object.__gt__ and value_type.__lt__ is not object.__lt__:
            def __gt__(self, other):
                if isinstance(other, type(self)):
                    if self == other:
                        return False
                    return not self.__lt__(other)
                return False

            setattr(value_type, '__gt__', __gt__)

        return value_type

    @__check_comparable
    def __init__(self, generic_type: Type,
                 sequence: Collection[E] = None) -> None:
        """Initialize an empty TreeSet if type is given or constructs one with the
        elements contained into the given sequence.

        :param generic_type: The generic type of the class or a sequence with
        element to construct the TreeSet
        :type generic_type: E
        :param: sequence: A sequence to take items from and add them to the TreeSet
        :type sequence: Sequence[E]
        """
        super().__init__()
        self.__root = self.__NULL = TreeNode(
            TreeNode.TreeNodeUtils.NULL, None, None, self.__BLACK
        )
        self.__size = 0
        self.__class_type = self.__complete_comparator(generic_type)
        self.iteraciones = 0
        self.contar = False

        if not sequence:
            return

        if not isinstance(sequence, Collection):
            raise TypeError(
                f"Second argument must be a sequence but {type(sequence)} was given"
            )

        self.add_all(sequence)

    def add_all(self, values):
        for value in values:
            self.add(value)

    @__type_validation
    def add(self, value: E) -> bool:
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

    @__type_validation
    def remove(self, value):
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

    def __symmetrical_successor(self, node):
        while node.left is not self.__NULL:
            node = node.left
        return node

    def size(self) -> int:
        """Provides the size of the current TreeSet.

        :return: size of the TreeSet instance
        :rtype: int
        """
        return self.__size

    def clear(self) -> None:
        """Clears the TreeSet from all its inserted elements."""
        self.__root = None
        self.__size = 0

    def clone(self) -> 'TreeSet':
        """Clones the current TreeSet and returns that clone.

        :return: A shallow copy of the current TreeSet instance
        :rtype: TreeSet
        """
        cloned = TreeSet(self.__class_type)
        cloned._TreeSet__root = self.__root
        cloned._TreeSet__size = self.__size
        return cloned

    def is_empty(self) -> bool:
        """Checks if the current TreeSet is empty or not.

        :return: True if TreeSet is empty else False
        :rtype: bool
        """
        return len(self) == 0

    @__type_validation
    def contains(self, value: E) -> bool:
        """Checks if a given value is contained into the current TreeSet
        instance.

        :param value: To check if it is contained
        :type value: E
        :return: True if value is contained else False
        :rtype: bool
        """
        return value in self

    @__type_validation
    def higher(self, value: E) -> Union[E, None]:
        """Returns the contiguous greater element of the given value from the
        TreeSet.

        :param value: Value to compare
        :return: Lowest element greater than the given value. If it was not
            possible, None will be returned.
        :rtype: Union[E, None]
        """
        if self.is_empty() or self.last() <= value:
            return None

        current = self.__root
        result = None

        while current is not self.__NULL:
            if current.value > value:
                result = current.value
                current = current.left
            else:
                current = current.right

        return result

    @__type_validation
    def lower(self, value: E) -> Union[E, None]:
        """Returns the contiguous lower element of the given value from the
        TreeSet.

        :param value: Value to compare
        :return: Greatest element lower than the given value. If it was not
            possible, None will be returned.
        :rtype: Union[E, None]
        """
        if self.is_empty() or self.first() >= value:
            return None

        current = self.__root
        result = None

        while current is not self.__NULL:
            if current.value < value:
                result = current.value
                current = current.right
            else:
                current = current.left

        return result

    @__type_validation
    def ceiling(self, value: E) -> Union[E, None]:
        """Returns the least element in this set greater than
        or equal to the given element, or null if there is no
        such element.

        :param value: Value to compare
        :return: the least element in this set greater than or equal
        to the given element
        :rtype: TreeSet
        """
        if self.is_empty() or self.last() < value:
            return None

        current = self.__root
        result = None

        while current is not self.__NULL:
            if current.value == value:
                return value
            elif current.value > value:
                result = current.value
                current = current.left
            else:
                current = current.right

        return result

    @__type_validation
    def floor(self, value: E) -> Union[E, None]:
        """Returns the greatest element in this set less than or
          equal to the given element, or null if there is no such
          element.

        :param value: Value to compare
        :return: the greatest element in this set less than or
        equal to the given element
        :rtype: TreeSet
        """
        if self.is_empty() or self.first() > value:
            return None

        current = self.__root
        result = None

        while current is not self.__NULL:
            if current.value == value:
                return value
            elif current.value < value:
                result = current.value
                current = current.right
            else:
                current = current.left

        return result

    def first(self) -> E:
        """Returns the lowest element contained in the current TreeSet instance.

        :return: Lowest contained element
        :rtype: E
        """
        if self.is_empty():
            raise NoSuchElementError()

        return next(self.iterator())

    def last(self) -> E:
        """Return the greatest element contained in the current TreeSet
        instance.

        :return: Greatest contained element
        :rtype: E
        """
        if self.is_empty():
            raise NoSuchElementError()

        return next(self.descending_iterator())

    def poll_first(self) -> E:
        """Retrieves and removes the first (lowest) element, or returns None
        if this set is empty.

        :return: The first (lowest) element, or None if this set is empty
        :rtype: Union[E, None]
        """
        if self.is_empty():
            raise NoSuchElementError()

        self.remove(item := self.first())
        return item

    def poll_last(self) -> E:
        """Retrieves and removes the first (lowest) element, or returns None
        if this set is empty.

        :return: The first (lowest) element, or None if this set is empty
        :rtype: Union[E, None]
        """
        if self.is_empty():
            raise NoSuchElementError()

        self.remove(item := self.last())
        return item

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

        while current is not self.__NULL:
            self.iteraciones += 1 if self.contar else 0
            if current.value == value:
                return current

            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return parent

    def __len__(self) -> int:
        """Provides the length og the current TreeSet. It is used with the
        built-in method len().

        :return: the length of the TreeSet.
        :rtype: nt
        """
        return self.__size

    def __iter__(self) -> E:
        """Method to iterate over the TreeSet instance."""
        for node in self.__inorder(True):
            yield node.value

    def __reversed__(self) -> E:
        """Method to iterate reversely over the TreeSet instance."""
        for node in self.__inorder(False):
            yield node.value

    def __inorder(self, inorder: bool) -> E:
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

    def __str__(self) -> str:
        """String representation of the current TreeSet.

        :return: TreeSet string representation
        :rtype: str
        """
        return f"{[value for value in self]}"

    def __contains__(self, value) -> bool:
        """Check if the given value is contained into the TreeSet or not.
        This method is called when using built-in operator 'in'.

        :param value: value to check
        :return: True if it is contained else False
        :rtype: bool
        """
        return self.__contains(value).value == value

    def __eq__(self, other) -> bool:
        """Check equality between the current instance and a given object.
        This method is called when using built-in operator '=='.

        :param other: other instance to compare with
        :return: True if instances are equal else False
        :rtype: bool
        """
        if isinstance(other, TreeSet):
            for value in self:
                if value not in other:
                    return False

            return True
        else:
            return False

    def __setattr__(self, key, value):
        """Method called when trying to set a value to an attribute that does not exists.
        Once the class is created, new attributes cannot be added.

        :param key: name of the attribute
        :param value: value to assign to the attribute
        """
        """if key not in self.__attributes:
            raise AttributeError(f"Cannot add more attributes to this instance {key}")"""
        super().__setattr__(key, value)

    def draw_tree(self):
        TreeSetDrawing(self)

    def __get_color(self, value):
        return node.color if (node := self.__contains(value)).value == value \
            else None

    def __array_color(self):
        return [self.__get_color(value) for value in self]


if __name__ == "__main__":
    items = [i for i in range(10, 30)]
    # items = ["a", "b", "c", "d", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    t = TreeSet(int, [i for i in range(20)])
    print(t)

    def loop_test():
        t = TreeSet(int)
        for _ in range(10):
            items = [randint(1, 1000) for _ in range(10)]
            t = TreeSet(int, items)
            print("Items", items)
            print("Tree:", t)
            print(t.ceiling(400))
            print("===================")
            # t.draw_tree()

    # loop_test()
