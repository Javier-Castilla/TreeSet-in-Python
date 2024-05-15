"""
TreeSet module.

This module provides a TreeSet class for storing and managing a set of elements
in a red-black tree data structure.
"""
import time
from random import randint
from data_utils import *
from treeset_exceptions import *
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox

E = TypeVar('E')


class GUI(tk.Tk):
    """
    GUI class used to show a Tkinter window in order to
    visualize the TreeSet base Red - Black Tree.
    """

    def __init__(self, tree):
        """
        Class constructor

        :param tree: The TreeSet object to be visualized.
        :type tree: TreeSet
        """
        super().__init__()
        self.title("TREESET")
        self.geometry("815x300")
        self.resizable(False, False)
        self.config(bg="#303030")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.__tree: TreeSet = tree
        self.fig, self.ax = plt.subplots()
        self.test = False
        self.stop = True

        self.title_label = tk.Label(self, text="TREESET", bg="#303030",
                                    fg="white", font=('Arial', 16, 'bold'))
        self.title_label.pack(side="top", pady=10)

        style = ttk.Style()
        style.configure('TButton',
                        background='#f2f2f2',
                        foreground='#333',
                        font=('Arial', 10, 'bold'),
                        bordercolor="#333",
                        relief="solid",
                        borderwidth=1)

        style.map('TButton',
                  background=[('active', '#f2f2f2')],
                  foreground=[('active', '#333')],
                  relief=[('active', 'groove')],
                  bordercolor=[('active', '#333')],
                  borderwidth=[('active', 1)])

        main_frame = tk.Frame(self, bg="#303030")
        main_frame.pack(expand=True, fill="both")

        self.wait_time_slider = tk.Scale(self, from_=0.01, to=1,
                                         resolution=0.01, orient="horizontal",
                                         length=self.winfo_screenwidth(),
                                         label="Wait Time (s)", bd=0)
        self.wait_time_slider.set(0.01)
        self.wait_time_slider.pack(side="top", fill="x")

        self.wait_time_slider.config(bg="#303030", fg="white",
                                     troughcolor="white", sliderlength=20,
                                     width=20, highlightbackground="#303030")

        self.value_label = tk.Label(main_frame, text="VALUE:", bg="#303030",
                                    fg="white", font=('Arial', 10, 'bold'))
        self.value_label.grid(row=0, column=0, padx=10, pady=10)

        self.result = tk.Label(main_frame, text="RESULT: ", bg="#303030",
                               fg="white", font=('Arial', 10, 'bold'))
        self.result.grid(row=3, column=0, padx=10, pady=10, columnspan=7,
                         sticky="ew")

        self.value_entry = tk.Entry(main_frame, width=15, font=('Arial', 10))
        self.value_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=6,
                              sticky="ew")

        buttons = {"Add": self.add, "Remove": self.remove,
                   "Clear": self.clear, "Lower": self.tree_lower,
                   "Higher": self.higher, "Ceiling": self.ceiling,
                   "Floor": self.floor,
                   "First": self.first, "Last": self.last,
                   "Poll First": self.poll_first,
                   "Poll Last": self.poll_last, "Size": self.size,
                   "Contains": self.contains, "Test": self.__execute_test,
                   "Pause": self.pause_test, "Stop": self.stop_test}

        for i, text in enumerate(buttons):
            button = ttk.Button(main_frame, text=text, width=10,
                                command=lambda t=buttons[text]: t(),
                                style='TButton')
            button.grid(row=(i + 1) // 9 + 1, column=i % 8, padx=5, pady=5)

    def on_close(self):
        if messagebox.askokcancel("Exit", "Do you want to close the window?"):
            print("The window is closing... executing cleaning labours.")
            self.test = False
            self.stop = True
            plt.close('all')
            self.destroy()

    def __get_value(self):
        try:
            value = int(self.value_entry.get())
            return value
        except ValueError:
            self.__set_result("Value must be int!")

    def __test(self):
        self.__tree.add(randint(-100000, 100000))
        self.__reset()
        self.size()
        plt.pause(self.wait_time_slider.get())

    def pause_test(self):
        self.test = not self.test
        if self.test:
            self.__execute_test()

    def stop_test(self):
        self.stop = True
        self.__tree.clear()
        self.__reset()

    def __execute_test(self):
        value = self.__get_value()
        if self.stop:
            self.__tree.clear()
        self.test = True
        self.stop = False
        while self.__tree.size() != value:
            if self.stop:
                break
            if self.test:
                self.__test()
            else:
                break
        if not self.stop and self.test:
            self.test = False
            self.stop = True

    def __reset(self):
        self.draw()

    def __set_result(self, msg) -> None:
        self.result.config(text=f"RESULT: {msg}")

    def add(self):
        self.__set_result(self.__tree.add(self.__get_value()))
        self.__reset()

    def remove(self):
        self.__set_result(self.__tree.remove(self.__get_value()))
        self.__reset()

    def clear(self):
        self.__tree.clear()
        self.__set_result("Tree correctly cleared!")
        self.__reset()

    def tree_lower(self):
        self.__set_result(self.__tree.lower(self.__get_value()))

    def higher(self):
        self.__set_result(self.__tree.higher(self.__get_value()))

    def ceiling(self):
        self.__set_result(self.__tree.ceiling(self.__get_value()))

    def floor(self):
        self.__set_result(self.__tree.floor(self.__get_value()))

    def first(self):
        try:
            self.__set_result(self.__tree.first())
        except NoSuchElementError as err:
            self.__set_result("The tree is empty!")

    def last(self):
        try:
            self.__set_result(self.__tree.last())
        except NoSuchElementError as err:
            self.__set_result("The tree is empty!")

    def poll_first(self):
        try:
            self.__set_result(self.__tree.poll_first())
            self.__reset()
        except NoSuchElementError as err:
            self.__set_result("The tree is empty!")

    def poll_last(self):
        try:
            self.__set_result(self.__tree.poll_last())
            self.__reset()
        except NoSuchElementError as err:
            self.__set_result("The tree is empty!")

    def size(self):
        self.__set_result(self.__tree.size())

    def contains(self):
        self.__set_result(self.__tree.contains(self.__get_value()))

    def draw(self):
        self.ax.clear()  # Clear the axis before drawing
        self.fig.subplots_adjust(left=0, bottom=0, right=1,
                                 top=1)  # Adjust the margins of the subplot
        self.__draw_node(self.ax, self.__tree._RedBlackTree__root)
        self.__draw_edges(self.ax, self.__tree._RedBlackTree__root)
        self.ax.axis('off')  # Hide axes
        plt.show(block=False)  # Non-blocking show

    def __draw_node(self, ax, node, x=0, y=0, dx=1, dy=1):
        if node is not RedBlackTree.NULL:
            color = "red" if node.color == RedBlackTree.RED else "black"
            ax.plot([x], [y], marker='o', markersize=40, color=color,
                    zorder=2)  # Dibujar nodo con un tamaño mayor y detrás de las líneas
            ax.text(x, y, str(node.value), fontsize=12, ha='center',
                    va='center', color='white',
                    zorder=3)  # Etiquetar nodo
            if node.left is not RedBlackTree.NULL:
                self.__draw_node(ax, node.left, x - dx, y - dy, dx / 2, dy * 2)
            if node.right is not RedBlackTree.NULL:
                self.__draw_node(ax, node.right, x + dx, y - dy, dx / 2, dy * 2)

    def __draw_edges(self, ax, node, x=0, y=0, dx=1, dy=1):
        if node is not RedBlackTree.NULL:
            if node.left is not RedBlackTree.NULL:
                ax.plot([x, x - dx], [y, y - dy], color='black',
                        zorder=1)  # Dibujar conexión izquierda en negro y detrás de los nodos
                self.__draw_edges(ax, node.left, x - dx, y - dy, dx / 2, dy * 2)
            if node.right is not RedBlackTree.NULL:
                ax.plot([x, x + dx], [y, y - dy], color='black',
                        zorder=1)  # Dibujar conexión derecha en negro y detrás de los nodos
                self.__draw_edges(ax, node.right, x + dx, y - dy, dx / 2,
                                  dy * 2)


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
        :return: function return statement
        """

        def wrapper(self, item):
            if not isinstance(item, self.__class_type):
                raise TypeError(
                    f"Value type must be '{self.__class_type}: {type(item)}'")

            return function(self, item)

        return wrapper

    def __check_comparable(function):
        """
        Decorator used to check comparability of the type specified when
        creating the TreeSet.

        :param function: used functions of the TreeSet
        :return: function return statement
        :raise NonComparableObjectError: if the given value is not comparable
        """

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
        """
        Private method used to complete specified type comparator.
        If the given class has only one of the two lateral
        comparators, the other will be added to the class with
        the help of the one already implemented.

        :param value_type: the type to complete its comparator
        :type value_type: type
        :return: the given value type
        :rtype: type
        """
        if value_type.__lt__ is object.__lt__ \
                and value_type.__gt__ is not object.__gt__:
            def __lt__(self, other):
                if isinstance(other, type(self)):
                    if self == other:
                        return False
                    return not self.__gt__(other)
                return False

            setattr(value_type, '__lt__', __lt__)
        elif value_type.__gt__ is object.__gt__ \
                and value_type.__lt__ is not object.__lt__:
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
        """
        Initialize an empty TreeSet if type is given or constructs one with the
        elements contained into the given sequence.

        :param generic_type: the generic type of the class
        :type generic_type: type
        :param: sequence: a collection to take items from and add them to the TreeSet
        :type sequence: Collection[E]
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
        be thrown.

        :param values: Values to insert into the TreeSet.
        :type values: Collection[E]
        :return: True if all values could be inserted else False.
        :rtype: bool
        :raises TypeError: If the given values does not match the
            instance type.
        """
        old_size = self.size()

        for value in values:
            self.add(value)

        return old_size == self.size() - len(values)

    @__type_validation
    def add(self, value: E) -> bool:
        """
        Inserts the given value into the current TreeSet. If the type of
        the value does not match the instance TreeSet type, an exception will
        be thrown.

        :param value: value to insert into the TreeSet
        :type value: E
        :return: True if the value could be inserted else False
        :rtype: bool
        :raises TypeError: if the given values does not match the
            instance type
        """
        return self.insert(value)

    @__type_validation
    def remove(self, value: E):
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
        """
        return self.delete(value)

    def size(self) -> int:
        """
        Provides the size of the current TreeSet.

        :return: size of the TreeSet instance
        :rtype: int
        """
        return super().size()

    def clear(self) -> None:
        """Clears the TreeSet from all its inserted elements."""
        self._RedBlackTree__root = RedBlackTree.NULL
        self._RedBlackTree__size = 0

    def clone(self) -> 'TreeSet':
        """
        Clones the current TreeSet and returns that clone.

        :return: A shallow copy of the current TreeSet instance.
        :rtype: TreeSet
        """
        cloned = TreeSet(self.__class_type)
        cloned._RedBlackTree__root = self._RedBlackTree__root
        cloned._RedBlackTree__size = self._RedBlackTree__size
        return cloned

    def is_empty(self) -> bool:
        """
        Checks if the current TreeSet is empty or not.

        :return: True if TreeSet is empty else False
        :rtype: bool
        """
        return self.size() == 0

    @__type_validation
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
        """
        return value in self

    @__type_validation
    def higher(self, value: E) -> Union[E, None]:
        """
        Returns the next higher value in the tree compared to the given
        value.
        """
        current = self._RedBlackTree__root
        result = None

        while current is not RedBlackTree.NULL:
            if current.value > value:
                result = current.value
                current = current.left
            else:
                current = current.right

        return result

    @__type_validation
    def lower(self, value: E) -> Union[E, None]:
        """
        Returns the contiguous lower element of the given value from the
        TreeSet.

        :param value: value to compare
        :type value: E
        :return: the greatest element lower than the given value. If it was not
            possible, None will be returned.
        :rtype: Union[E, None]
        :raises TypeError: if the given values does not match the
            instance type
        """
        current = self._RedBlackTree__root
        result = None

        while current is not RedBlackTree.NULL:
            if current.value < value:
                result = current.value
                current = current.right
            else:
                current = current.left

        return result

    @__type_validation
    def ceiling(self, value: E) -> Union[E, None]:
        """
        Returns the least element in this set greater than
        or equal to the given element, or null if there is no
        such element.

        :param value: Value to compare.
        :type value: E
        :return: The least element in this set greater than or equal
            to the given element.
        :rtype: TreeSet
        :raises TypeError: If the given values does not match the
            instance type.
        """
        current = self._RedBlackTree__root
        result = None

        while current is not RedBlackTree.NULL:
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
        """
        current = self._RedBlackTree__root
        result = None

        while current is not RedBlackTree.NULL:
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
            raise NoSuchElementError()

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
            raise NoSuchElementError()

        return next(self.descending_iterator())

    def poll_first(self) -> E:
        """
        Retrieves and removes the first (lowest) element, or returns None
        if this set is empty.

        :return: the first (lowest) element, or None if this set is empty
        :rtype: Union[E, None]
        :raises NoSuchElementException: if there is no such element
        """
        if self.is_empty():
            raise NoSuchElementError()

        self.remove(item := self.first())
        return item

    def poll_last(self) -> E:
        """
        Retrieves and removes the first (lowest) element, or returns None
        if this set is empty.

        :return: the first (lowest) element, or None if this set is empty
        :rtype: Union[E, None]
        :raises NoSuchElementException: if there is no such element
        """
        if self.is_empty():
            raise NoSuchElementError()

        self.remove(item := self.last())
        return item

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

    def __setattr__(self, key, value):
        """
        Method called when trying to set a value to an attribute that does not exists.
        Once the class is created, new attributes cannot be added.

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
        return node.color if (node := self.__contains(value)).value == value \
            else None

    def __array_color(self):
        return [self.__get_color(value) for value in self]


if __name__ == "__main__":
    items = [i for i in range(10, 30)]
    # items = ["a", "b", "c", "d", "d", "f", "g", "h", "i", "j", "k", "l",
    # "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    t = TreeSet(int, [i for i in range(20)])


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
