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


class TreeSet:
    """Class that represents a set based on a tree. The elements are ordered
    using its natural ordering.

    Since this implementation uses a Red-Black Tree, it provides guaranteed
    log(n) time cost for the basic operations.

    TreeSet string representation will be provided inorder.
    """

    RED = TreeNode.Color.RED
    BLACK = TreeNode.Color.BLACK

    def __init__(self, generic_type: Any, sequence: Collection[E] = None) -> None:
        """
        Initialize an empty TreeSet if type is given or constructs one with the
        elements contained into the given sequence.

        :param generic_type: The generic type of the class or a sequence with
        element to construct the TreeSet
        :type generic_type: E
        :param: sequence: A sequence to take items from and add them to the TreeSet
        :type sequence: Sequence[E]
        """
        self.__root = self.__first = self.__last = None
        self.__size = 0
        self.class_type = generic_type

        if sequence:
            if isinstance(sequence, Collection):
                if len(set(map(type, sequence))) != 1:
                    raise TypeError("Sequence elements type must be the same")

                if type(next(iter(sequence))) != self.class_type:
                    raise TypeError(
                        f"Expected elements of type {self.class_type} ")

                for item in sequence:
                    self.add(item)

    def add(self, value: E) -> bool:
        """Inserts the given value into the TreeSet if value is not contained.

        :param value: Value to insert into the TreeSet
        :type value: E
        :return: True if the value have been added to the TreeSet else False
        :rtype: bool
        :raises AssertionError: If the given value's type does not match generic
        type
        """
        assert type(value) == self.class_type, \
            f"Value type must be '{self.class_type}'"

        if not self.__check_comparable(value):
            raise NonComparableObject(f"class {type(value)} cannot be compared")

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
                    if root.parent.left == root:
                        root.parent.left = successor
                    else:
                        root.parent.right = successor
                    successor.parent = root.parent
                else:
                    self.__root = successor

            if len(self) == 1:
                self.__first = self.__last = None
            else:
                if prev := root.previous_node:
                    prev.next_node = root.next_node
                if next_node := root.next_node:
                    next_node.previous_node = root.previous_node

        self.__size -= 1
        self.__fix_removal(successor if successor else root)
        return True

    def clear(self) -> None:
        """Clears the TreeSet from all its inserted elements."""
        self.__root = None
        self.__size = 0

    def clone(self) -> 'TreeSet':
        """Clones the current TreeSet and returns that clone.

        :return: A shallow copy of the current TreeSet instance
        :rtype: TreeSet
        """
        clone_tree = TreeSet(self.class_type)
        for value in self:
            clone_tree.add(value)

        return clone_tree

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
        other = None

        while current:
            if value <= current.value:
                if not current.left:
                    return other.value if other else None
                current = current.left
            else:
                if not current.right:
                    return current.value
                if current.right.value >= value:
                    other = current
                current = current.right

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
        other = None

        while current:
            if current.value > value:
                if not current.left:
                    return current.value
                if current.left.value <= value:
                    other = current
                current = current.left
            else:
                if not current.right:
                    if other:
                        return other.value
                    else:
                        return None
                current = current.right

    def ceiling(self, value: E) -> Union[E, None]:
        """Returns the least element in this set greater than
        or equal to the given element, or null if there is no
        such element.

        :param value: Value to compare
        :return: least element in this set greater than or equal
        to the given element
        :rtype: TreeSet
        """
        current = self.__root
        other = None

        while current:
            if current.value > value:
                if not current.left:
                    return current.value
                if current.left.value < value:
                    other = current
                current = current.left
            elif current.value < value:
                if not current.right:
                    if other:
                        return other.value
                    else:
                        return current.value
                current = current.right
            else:
                return current.value

    def floor(self, value: E) -> Union[E, None]:
        """Returns the greatest element in this set less than or
          equal to the given element, or null if there is no such
          element.

        :param value: Value to compare
        :return: the greatest element in this set less than or
        equal to the given element
        :rtype: TreeSet
        """
        current = self.__root
        other = None

        while current:
            if current.value > value:
                if not current.left:
                    if other:
                        return other.value
                    else:
                        return current.value
                current = current.left
            elif current.value < value:
                if not current.right:
                    return current.value
                if current.right.value > value:
                    other = current
                current = current.right
            else:
                return current.value

    def first(self) -> E:
        """Returns the lowest element contained in the current TreeSet instance.

        :return: Lowest contained element
        :rtype: E
        """
        if self.is_empty():
            return None

        return next(self.iterator())

    def last(self) -> E:
        """Return the greatest element contained in the current TreeSet
        instance.

        :return: Greatest contained element
        :rtype: E
        """
        if self.is_empty():
            return None

        return next(self.descending_iterator())

    def poll_first(self):
        """Retrieves and removes the first (lowest) element, or returns None
        if this set is empty.

        :return: The first (lowest) element, or None if this set is empty
        :rtype: Union[E, None]
        """
        if self.is_empty():
            return None

        self.remove(item := next(self.iterator()))
        return item

    def poll_last(self):
        """Retrieves and removes the first (lowest) element, or returns None
        if this set is empty.

        :return: The first (lowest) element, or None if this set is empty
        :rtype: Union[E, None]"""
        if self.is_empty():
            return None

        self.remove(item := next(self.descending_iterator()))
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

    def __check_comparable(self, value: E) -> bool:
        try:
            value < value
            value > value
            return True
        except TypeError:
            return False

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

    def __insertion_order(self) -> None:
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

    def __inorder(self, reverse: bool) -> E:
        stack = SimpleStack()
        current = self.__root

        while True:
            if current:
                stack.push(current)
                current = current.left if not reverse else current.right
            elif not stack.is_empty():
                current = stack.pull()
                yield current
                current = current.right if not reverse else current.left
            else:
                break

    def __str__(self) -> str:
        return f"{[value for value in self]}"

    def __contains__(self, value) -> bool:
        return self.__contains(value).value == value

    def __eq__(self, other) -> bool:
        if isinstance(other, TreeSet):
            for value in self:
                if value not in other:
                    return False

            return True
        else:
            return False

    def draw_tree(self):
        root = tk.Tk()
        root.title("Árbol Rojo-Negro")
        root.geometry("400x200")
        root.resizable(False, False)

        value = tk.StringVar()
        value.set("")

        label = tk.Label(root, text="Nodo:")
        label.grid(row=0, column=0)

        entry = tk.Entry(root, textvariable=value)
        entry.grid(row=1, column=0)

        buttons = list()

        insert = tk.Button(root, text="Insertar Valor", command=lambda: (self.add(int(value.get())), plt.close('all'), self.__draw()))
        buttons.append(insert)
        delete = tk.Button(root, text="Eliminar Valor", command=lambda: (self.remove(int(value.get())), plt.close('all'), self.__draw()))
        buttons.append(delete)
        clear = tk.Button(root, text="Borrar Árbol", command=lambda: (self.clear(), plt.close('all'), self.__draw()))
        buttons.append(clear)
        lower = tk.Button(root, text="Lower", command=lambda: (print(self.lower(int(value.get())))))
        buttons.append(lower)
        higher = tk.Button(root, text="Higher", command=lambda: (print(self.higher(int(value.get())))))
        buttons.append(higher)
        ceiling = tk.Button(root, text="Ceiling", command=lambda: (print(self.ceiling(int(value.get())))))
        buttons.append(ceiling)
        floor = tk.Button(root, text="Floor", command=lambda: (print(self.floor(int(value.get())))))
        buttons.append(floor)
        first = tk.Button(root, text="First", command=lambda: (print(self.first())))
        buttons.append(first)
        last = tk.Button(root, text="Last", command=lambda: (print(self.last())))
        buttons.append(last)
        poll_first = tk.Button(root, text="Poll First", command=lambda: (print(self.poll_first()), plt.close('all'), self.__draw()))
        buttons.append(poll_first)
        poll_last = tk.Button(root, text="Poll Last", command=lambda: (print(self.poll_last()), plt.close('all'), self.__draw()))
        buttons.append(poll_last)
        size = tk.Button(root, text="Size", command=lambda: (print(len(self))))

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
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1)  # Ajustar los márgenes del subplot
        self.__draw_node(ax, self.__root)
        self.__draw_edges(ax, self.__root)
        ax.axis('off')  # Ocultar ejes
        plt.show()

    def __draw_node(self, ax, node, x=0, y=0, dx=1, dy=1):
        if node is not None:
            color = "red" if node.color == self.RED else "black"
            ax.plot([x], [y], marker='o', markersize=40, color=color,
                    zorder=2)  # Dibujar nodo con un tamaño mayor y detrás de las líneas
            ax.text(x, y, str(node.value), fontsize=12, ha='center', va='center', color='white',
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
                self.__draw_edges(ax, node.right, x + dx, y - dy, dx / 2, dy * 2)


if __name__ == "__main__":
    items = [randint(1, 1000) for _ in range(10)]
    # items = ["a", "b", "c", "d", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # items = [Test1() for _ in range(10)]
    # items = [98, 3, 4, 2, 37, 78, 47, 16, 81, 23]
    t = TreeSet(int, items)
    print("Items", items)
    print("Tree:", t)
    print(t.lower(0))
    print("===================")
    #t.draw_tree()

    t = TreeSet(Test3)
    t.add(Test3())

    def loop_test():
        t = TreeSet(int)
        for _ in range(10):
            items = [randint(1, 1000) for _ in range(10)]
            t = TreeSet(int, items)
            print("Items", items)
            print("Tree:", t)
            print(t.lower(0))
            print("===================")
            # t.draw_tree()

    #loop_test()