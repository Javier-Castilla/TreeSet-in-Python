"""
TreeSet module.

This module provides a TreeSet class for storing and managing a set of elements
in a red-black tree data structure.
"""
import ast
import copy
import inspect
import random
import time
import tkinter as tk
from tkinter import messagebox, ttk

import matplotlib.pyplot as plt

from data_utils import *
from Person import *
from treeset_exceptions import *

E = TypeVar('E')


class GUI(tk.Tk):
    """
    GUI class used to show a Tkinter window in order to
    visualize the TreeSet base Red - Black Tree.
    """

    def __tree_exists(function):
        def wrapper(self, *args, **kwargs):
            if self.__tree is None:
                self.__set_result("Tree not initialized!")
            else:
                return function(self, *args, **kwargs)

        return wrapper

    def __init__(self, tree=None):
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
        self.protocol("WM_DELETE_WINDOW", self.__on_close)
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

        self.objects = {"int": int, "str": str, "float": float}

        """with open(__file__, 'r') as f:
            source_code = f.read()

        tree = ast.parse(source_code)
        self.imported_modules = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.imported_modules.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                self.imported_modules.append(node.module)

        self.modules_combo = ttk.Combobox(
            main_frame, values=self.imported_modules, state="readonly",
            width=10, postcommand=self.__update_combo
        )
        self.modules_combo.grid(row=0, column=7, padx=10, pady=10)
        self.modules_combo.bind("<<ComboboxSelected>>", self.__update_combo)

        self.classes_combo = ttk.Combobox(
            main_frame, values=list(self.objects.keys()), state="readonly",
            width=10, postcommand=self.__update_combo
        )
        self.classes_combo.grid(row=0, column=8, padx=10, pady=10)
        self.classes_combo.bind("<<ComboboxSelected>>", self.__update_tree)"""

        buttons = {"Add": self.add, "Remove": self.remove,
                   "Clear": self.clear, "Lower": self.tree_lower,
                   "Higher": self.higher, "Ceiling": self.ceiling,
                   "Floor": self.floor,
                   "First": self.first, "Last": self.last,
                   "Poll First": self.poll_first,
                   "Poll Last": self.poll_last, "Size": self.size,
                   "Contains": self.contains, "Test": self.__execute_test,
                   "Pause": self.pause_test, "Stop": self.stop_test,
                   "Show": self.draw}

        for i, text in enumerate(buttons):
            button = ttk.Button(main_frame, text=text, width=10,
                                command=lambda t=buttons[text]: t(),
                                style='TButton')
            button.grid(row=(i + 1) // 9 + 1, column=i % 8, padx=5, pady=5)

    def __update_tree(self):
        self.__tree = self.objects[self.classes_combo.get()](
            self.objects[self.modules_combo.get()]
        )

    def __update_combo(self, event):
        for module in self.imported_modules:
            for name, module_object in inspect.getmembers(module):
                if inspect.isclass(module_object):
                    self.objects[name] = module_object

        self.classes_combo["values"] = list(self.objects.keys())

    def __on_close(self):
        if messagebox.askokcancel("Exit", "Do you want to close the window?"):
            print("The window is closing... executing cleaning labours.")
            self.test = False
            self.stop = True
            plt.close('all')
            self.destroy()

    def __get_value(self):
        try:
            value = self.__tree._TreeSet__class_type(self.value_entry.get())
            return value
        except ValueError:
            self.__set_result(
                "Value must be {self.__tree_TreeSet__class_type}!")

    def __test(self):
        self.__tree.add(random.randint(-100000, 100000))
        self.__reset()
        self.size()
        plt.pause(self.wait_time_slider.get())

    def pause_test(self):
        self.test = not self.test
        if self.test and self.__tree:
            self.__execute_test()

    @__tree_exists
    def stop_test(self):
        self.stop = True
        self.__tree.clear()
        self.__reset()

    @__tree_exists
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

    @__tree_exists
    def add(self):
        self.__set_result(self.__tree.add(self.__get_value()))
        self.__reset()

    @__tree_exists
    def remove(self):
        self.__set_result(self.__tree.remove(self.__get_value()))
        self.__reset()

    @__tree_exists
    def clear(self):
        self.__tree.clear()
        self.__set_result("Tree correctly cleared!")
        self.__reset()

    @__tree_exists
    def tree_lower(self):
        self.__set_result(self.__tree.lower(self.__get_value()))

    @__tree_exists
    def higher(self):
        self.__set_result(self.__tree.higher(self.__get_value()))

    @__tree_exists
    def ceiling(self):
        self.__set_result(self.__tree.ceiling(self.__get_value()))

    @__tree_exists
    def floor(self):
        self.__set_result(self.__tree.floor(self.__get_value()))

    @__tree_exists
    def first(self):
        try:
            self.__set_result(self.__tree.first())
        except NoSuchElementError as err:
            self.__set_result("The tree is empty!")

    @__tree_exists
    def last(self):
        try:
            self.__set_result(self.__tree.last())
        except NoSuchElementError as err:
            self.__set_result("The tree is empty!")

    @__tree_exists
    def poll_first(self):
        try:
            self.__set_result(self.__tree.poll_first())
            self.__reset()
        except NoSuchElementError as err:
            self.__set_result("The tree is empty!")

    @__tree_exists
    def poll_last(self):
        try:
            self.__set_result(self.__tree.poll_last())
            self.__reset()
        except NoSuchElementError as err:
            self.__set_result("The tree is empty!")

    @__tree_exists
    def size(self):
        self.__set_result(self.__tree.size())

    @__tree_exists
    def contains(self):
        self.__set_result(self.__tree.contains(self.__get_value()))

    @__tree_exists
    def draw(self):
        self.ax.clear()  # Clear the axis before drawing
        self.fig.subplots_adjust(left=0, bottom=0, right=1,
                                 top=1)  # Adjust the margins of the subplot
        self.__draw_node(self.ax, self.__tree._RedBlackTree__root)
        self.__draw_edges(self.ax, self.__tree._RedBlackTree__root)
        self.ax.axis('off')  # Hide axes
        plt.show(block=False)  # Non-blocking show

    @__tree_exists
    def __draw_node(self, ax, node, x=0, y=0, dx=1, dy=1):
        if node is not RedBlackTree._NULL:
            color = "red" if node.color == RedBlackTree._RED else "black"
            ax.plot([x], [y], marker='o', markersize=40, color=color,
                    zorder=2)  # Dibujar nodo con un tamaño mayor y detrás de las líneas
            ax.text(x, y, str(node.value), fontsize=12, ha='center',
                    va='center', color='white',
                    zorder=3)  # Etiquetar nodo
            if node.left is not RedBlackTree._NULL:
                self.__draw_node(ax, node.left, x - dx, y - dy, dx / 2, dy * 2)
            if node.right is not RedBlackTree._NULL:
                self.__draw_node(ax, node.right, x + dx, y - dy, dx / 2, dy * 2)

    @__tree_exists
    def __draw_edges(self, ax, node, x=0, y=0, dx=1, dy=1):
        if node is not RedBlackTree._NULL:
            if node.left is not RedBlackTree._NULL:
                ax.plot([x, x - dx], [y, y - dy], color='black',
                        zorder=1)  # Dibujar conexión izquierda en negro y detrás de los nodos
                self.__draw_edges(ax, node.left, x - dx, y - dy, dx / 2, dy * 2)
            if node.right is not RedBlackTree._NULL:
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
        :return: given function return statement
        :raises TypeError: if the item type does not match the TreeSet type
        """

        def wrapper(self, item):
            if not isinstance(item, self.__class_type):
                raise TypeError(
                    f"Value type must be '{self.__class_type}: {type(item)}'")

            return function(self, item)

        return wrapper

    def __check_comparable(function):
        """
        Private decorator used to check comparability of the type specified when
        creating the TreeSet.

        :param function: used functions of the TreeSet
        :return: given function return statement
        """

        def wrapper(self, *args):
            """
            Wrapper function used to check the comparability of the given value.

            :param self: the instance of the current TreeSet
            :param args: arguments given dynamically
            :return: the given function return statement
            :rtype: Any
            :raise NonComparableObjectError: if the given value is not comparable
            """
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
        c_type = value_type.__base__ if value_type.__base__ is not object \
            else value_type

        if value_type.__lt__ is object.__lt__ \
                and value_type.__gt__ is not object.__gt__:
            setattr(value_type, f"_{value_type}__comparator_class", c_type)

            def __lt__(self, other):
                if self == other:
                    return False
                else:
                    return not self.__gt__(other)

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

    @__check_comparable
    def __init__(self, generic_type: Type,
                 sequence: Collection[E] = None) -> None:
        """
        Initialize an empty TreeSet if type is given or constructs one with the
        elements contained into the given collection.

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
        be thrown, and no element will be added.

        :param values: values to insert into the TreeSet.
        :type values: Collection[E]
        :return: True if all values could be inserted else False.
        :rtype: bool
        :raises TypeError: if the given values does not match the
            instance type.
        """
        if not isinstance(values, Collection):
            raise TypeError(
                f"Second argument must be a sequence but {type(values)} was given"
            )

        old_size = self.size()
        added_values = []

        try:
            for value in values:
                self.add(value)
                added_values.append(value)
        except TypeError as e:
            for value in added_values:
                self.remove(value)

            raise e

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
        :raises TypeError: if the given value does not match the
            instance type
        """
        return super().add(value)

    @__type_validation
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
        self._RedBlackTree__root = RedBlackTree._NULL
        self._RedBlackTree__size = 0

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

        :param value: value to compare
        :return: the next higher value in the tree compared to the given value
        :rtype: Union[E, None]
        :raises TypeError: if the given values does not match the
            instance type
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

    @__type_validation
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

    @__type_validation
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
            instance type.
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
            raise NoSuchElementError()

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
            raise NoSuchElementError()

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
        except NoSuchElementError:
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
        except NoSuchElementError:
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
    tree = TreeSet(Person)
    ids = {random.randint(10, 40) for _ in range(10)}
    ids = sorted(list(ids))
    items = [Person(f"Person{identifier}", identifier) for identifier in ids]

    tree = TreeSet(Person, items)
    print(tree)

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