"""
TreeSet module.

This module provides a TreeSet class for storing and managing a set of elements
in a red-black tree data structure.
"""

from random import randint
from data_utils import *
from treeset_exceptions import *
import matplotlib.pyplot as plt
import tkinter as tk
from test_classes import *

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
                               self.__tree.add(int(value.get())), plt.close('all'),
                               self.__draw()))
        buttons.append(insert)
        delete = tk.Button(root, text="Eliminar Valor",
                           command=lambda: (
                               self.__tree.remove(int(value.get())), plt.close('all'),
                               self.__draw()))
        buttons.append(delete)
        clear = tk.Button(root, text="Borrar Árbol", command=lambda: (
            self.__tree.clear(), plt.close('all'), self.__draw()))
        buttons.append(clear)
        lower = tk.Button(root, text="Lower",
                          command=lambda: (print(self.__tree.lower(int(value.get())))))
        buttons.append(lower)
        higher = tk.Button(root, text="Higher", command=lambda: (
            print(self.__tree.higher(int(value.get())))))
        buttons.append(higher)
        ceiling = tk.Button(root, text="Ceiling", command=lambda: (
            print(self.__tree.ceiling(int(value.get())))))
        buttons.append(ceiling)
        floor = tk.Button(root, text="Floor",
                          command=lambda: (print(self.__tree.floor(int(value.get())))))
        buttons.append(floor)
        first = tk.Button(root, text="First",
                          command=lambda: (print(self.__tree.first())))
        buttons.append(first)
        last = tk.Button(root, text="Last",
                         command=lambda: (print(self.__tree.last())))
        buttons.append(last)
        poll_first = tk.Button(root, text="Poll First",
                               command=lambda: (
                                   print(self.__tree.poll_first()), plt.close('all'),
                                   self.__draw()))
        buttons.append(poll_first)
        poll_last = tk.Button(root, text="Poll Last",
                              command=lambda: (
                                  print(self.__tree.poll_last()), plt.close('all'),
                                  self.__draw()))
        buttons.append(poll_last)
        size = tk.Button(root, text="Size", command=lambda: (print(len(self))))
        buttons.append(size)
        random = tk.Button(root, text="Random Tree",
                           command=lambda: (plt.close('all'),
                                            self.__draw_random_tree(int(value.get())))
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
        if node is not None:
            color = "red" if node.color == self.__tree.RED else "black"
            ax.plot([x], [y], marker='o', markersize=40, color=color,
                    zorder=2)  # Dibujar nodo con un tamaño mayor y detrás de las líneas
            ax.text(x, y, str(node.value), fontsize=12, ha='center',
                    va='center', color='white',
                    zorder=3)  # Etiquetar nodo
            if node.left:
                self.__draw_node(ax, node.left, x - dx, y - dy, dx / 2, dy * 2)
            if node.right:
                self.__draw_node(ax, node.right, x + dx, y - dy, dx / 2, dy * 2)

    def __draw_edges(self, ax, node, x=0, y=0, dx=1, dy=1):
        if node is not None:
            if node.left:
                ax.plot([x, x - dx], [y, y - dy], color='black',
                        zorder=1)  # Dibujar conexión izquierda en negro y detrás de los nodos
                self.__draw_edges(ax, node.left, x - dx, y - dy, dx / 2, dy * 2)
            if node.right:
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

    RED = TreeNode.Color.RED
    BLACK = TreeNode.Color.BLACK
    __attributes = {
        "_TreeSet__root", "_TreeSet__size",
        "_TreeSet__class_type", "_TreeSet__attributes"
    }

    @staticmethod
    def __type_validation(function):
        """Decorator used to validate item type when adding or deleting it from a TreeSet.
        This decorator should not be used with other object instance but a TreeSet.

        :param function: function used of the TreeSet
        :return: function return statement
        """

        def wrapper(self, item):
            assert type(item) == self.__class_type, \
                f"Value type must be '{self.__class_type}'"

            return function(self, item)

        return wrapper

    @staticmethod
    def __check_comparable(function):
        def wrapper(self, *args):
            item = args[0]
            value_type = type(item) if not isinstance(item, type) else item
            if value_type.__eq__ is object.__eq__ \
                    and value_type.__lt__ is object.__lt__ \
                    and value_type.__gt__ is object.__gt__:
                raise NonComparableObjectError(
                    f"class {value_type} cannot be compared")

            return function(self, *args)

        return wrapper

    @__check_comparable
    def __init__(self, generic_type: type,
                 sequence: Collection[E] = None) -> None:
        """Initialize an empty TreeSet if type is given or constructs one with the
        elements contained into the given sequence.

        :param generic_type: The generic type of the class or a sequence with
        element to construct the TreeSet
        :type generic_type: E
        :param: sequence: A sequence to take items from and add them to the TreeSet
        :type sequence: Sequence[E]
        """
        self.__root = None
        self.__size = 0
        self.__class_type = generic_type

        if not sequence:
            return

        if not isinstance(sequence, Collection):
            raise TypeError(
                f"Second argument must be a sequence but {type(sequence)} was given"
            )

        if len(set(map(type, sequence))) != 1:
            raise TypeError("Sequence elements type must be the same")

        if type(next(iter(sequence))) != self.__class_type:
            raise TypeError(
                f"Expected elements of type {self.__class_type} ")

        for item in sequence:
            self.add(item)

    @__check_comparable
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
        new_node = TreeNode(value)

        if (parent := self.__contains(value)) != new_node:
            if not parent:
                self.__root = new_node
            else:
                if new_node < parent:
                    parent.left = new_node
                else:
                    parent.right = new_node

                new_node.parent = parent

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

    @__type_validation
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
                    if root.parent.left == root:
                        root.parent.left = successor
                    else:
                        root.parent.right = successor

                    successor.parent = root.parent
                else:
                    self.__root = successor

        self.__size -= 1
        self.__fix_removal(successor if successor else root)
        return True

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
        if self.is_empty():
            return TreeSet(self.__class_type)

        current_stack = SimpleStack(self.__root)
        copy_stack = SimpleStack(copy_root := TreeNode(self.__root.value, self.__root.color))

        while not current_stack.is_empty():
            current = current_stack.pull()
            copy = copy_stack.pull()

            if right := current.right:
                copy.right = TreeNode(right.value, current.color)
                current_stack.push(right)
                copy_stack.push(copy.right)

            if left := current.left:
                copy.left = TreeNode(left.value, current.color)
                current_stack.push(left)
                copy_stack.push(copy.left)

        cloned_tree = TreeSet(self.__class_type)
        cloned_tree.__root = copy_root
        cloned_tree.__size = self.__size
        return cloned_tree

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

    @__type_validation
    def higher(self, value: E) -> Union[E, None]:
        """Returns the contiguous greater element of the given value from the
        TreeSet.

        :param value: Value to compare
        :return: Lowest element greater than the given value. If it was not
            possible, None will be returned.
        :rtype: Union[E, None]
        """
        if self.is_empty() or self.last() < value:
            return None

        current = self.__root
        result = None

        while current:
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
        if self.is_empty() or self.first() > value:
            return None

        current = self.__root
        result = None

        while current:
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

        while current:
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

        while current:
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
        :rtype: Union[E, None]"""
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
        root = self.__root

        while root:
            if root.value == value:
                return root

            parent = root
            root = root.left if value < root.value else root.right

        return parent

    def __fix_insertion(self, node: TreeNode) -> None:
        """Balance the TreeSet if needed after an insertion.

        :param node: to start the balancing from
        """
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
        """Balance the TreeSet if needed after a deletion.

        :param node: to start the balancing from
        """
        while node != self.__root and (not node or node.color == TreeSet.BLACK):
            if not node.parent:
                break

            if node == node.parent.left:
                sibling = node.parent.right
                if not sibling:
                    break

                if sibling and sibling.color == TreeSet.RED:
                    sibling.color = TreeSet.BLACK
                    node.parent.color = TreeSet.RED
                    self.__left_rotation(node.parent)
                    sibling = node.parent.right

                if not sibling:
                    break

                if (
                        (
                                not sibling.right or sibling.right.color == TreeSet.BLACK)
                        and (
                        not sibling.left or sibling.left.color == TreeSet.BLACK)
                ):
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
                    break

                if sibling and sibling.color == TreeSet.RED:
                    sibling.color = TreeSet.BLACK
                    node.parent.color = TreeSet.RED
                    self.__right_rotation(node.parent)
                    sibling = node.parent.left

                if not sibling:
                    break

                if ((not sibling.right or sibling.right.color == TreeSet.BLACK)
                        and (
                                not sibling.left
                                or sibling.left.color == TreeSet.BLACK)
                ):
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
        """Rotates the given TreeNode to the left.

        :param node: TreeNode to rotate
        """
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
        """Rotates the given TreeNode to the right.

        :param node: TreeNode to rotate
        """
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
            if current:
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
        """Method called when trying to set a value to an attribute.
        Once the class is created, new attributes cannot be added.

        :param key: name of the attribute
        :param value: value to assign to the attribute
        """
        if key not in self.__attributes:
            raise AttributeError(f"Cannot add more attributes to this instance {key}")
        super().__setattr__(key, value)

    def draw_tree(self):
        TreeSetDrawing(self)


if __name__ == "__main__":
    items = [randint(1, 1000) for _ in range(10)]
    # items = ["a", "b", "c", "d", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # items = [Test1() for _ in range(10)]
    # items = [98, 3, 4, 2, 37, 78, 47, 16, 81, 23]
    t = TreeSet(int, set([num for num in range(10)]))
    t1 = t.clone()
    print(t)
    print(t1)
    t.draw_tree()


    # t.pepe = None
    # t.draw_tree()
    # t = TreeSet(Test3)
    # t.add(Test3())
    # print(t)

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
