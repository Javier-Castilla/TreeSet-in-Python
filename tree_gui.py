import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from tree_set import *


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
        self.resizable(False, False)
        self.config(bg="#303030")
        self.protocol("WM_DELETE_WINDOW", self.__on_close)
        self.__tree: TreeSet = tree
        self.fig, self.ax = plt.subplots()
        self.stop = True
        self.looked_size = 0
        self.type = int
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
        self.result.grid(row=3, column=0, padx=10, pady=10, columnspan=8,
                         sticky="ew")

        self.value_entry = tk.Entry(main_frame, width=15, font=('Arial', 10))
        self.value_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=5,
                              sticky="ew")

        self.type_label = tk.Label(main_frame, text="TREE-TYPE:", bg="#303030",
                                   fg="white", font=('Arial', 10, 'bold'))
        self.type_label.grid(row=0, column=6, padx=10, pady=10)

        self.objects = {"int": int, "str": str, "float": float}
        self.classes_combo = ttk.Combobox(
            main_frame, values=list(self.objects.keys()),
            state="readonly", width=10
        )
        self.classes_combo.grid(row=0, column=7, padx=10, pady=10)
        self.classes_combo.bind("<<ComboboxSelected>>", self.__update_tree)
        self.classes_combo.current(0)

        buttons = {"Add": self.__add, "Remove": self.__remove,
                   "Clear": self.__clear, "Lower": self.__tree_lower,
                   "Higher": self.__higher, "Ceiling": self.__ceiling,
                   "Floor": self.__floor,
                   "First": self.__first, "Last": self.__last,
                   "Poll First": self.__poll_first,
                   "Poll Last": self.__poll_last, "Size": self.__size,
                   "Contains": self.__contains, "Test": self.__start_test,
                   "Pause": self.__pause_test, "Stop": self.__stop_test,
                   "Show": self.__show}

        self.button_widgets = dict()

        for i, text in enumerate(buttons):
            button = ttk.Button(main_frame, text=text, width=10,
                                command=lambda t=buttons[text]: t(),
                                style='TButton')
            button.grid(row=(i + 1) // 9 + 1, column=i % 8, padx=5, pady=5)
            self.button_widgets[text] = button

        self.button_widgets["Pause"].config(state="disabled")
        self.button_widgets["Stop"].config(state="disabled")
        self.update()

    def __update_tree(self, event):
        self.__stop_test()
        self.__tree = TreeSet(
            class_type := self.objects[self.classes_combo.get()])
        self.type = class_type

        if self.type is not str:
            self.button_widgets["Test"].config(state="normal")
            self.button_widgets["Pause"].config(state="disabled")
            self.button_widgets["Stop"].config(state="disabled")
        else:
            self.button_widgets["Test"].config(state="disabled")
            self.button_widgets["Pause"].config(state="disabled")
            self.button_widgets["Stop"].config(state="disabled")

        self.__show()

    def __on_close(self):
        if messagebox.askokcancel("Exit", "Do you want to close the window?"):
            print("The window is closing... executing cleaning labours.")
            self.test = False
            self.stop = True
            plt.close('all')
            self.destroy()

    def __get_value(self):
        value = self.value_entry.get()
        self.value_entry.delete(0, tk.END)
        return value

    def __test(self):
        self.__tree.add(random.randint(-100000, 100000))
        self.__reset()
        self.__size()
        plt.pause(self.wait_time_slider.get())

    def __start_test(self):
        self.stop = False
        self.button_widgets["Pause"].config(state="normal")
        self.button_widgets["Stop"].config(state="normal")
        self.button_widgets["Test"].config(state="disabled")
        self.__execute_test()

    def __pause_test(self):
        self.stop = not self.stop
        if not self.stop:
            self.button_widgets["Pause"].config(text="Pause")
            self.__execute_test()
        else:
            self.button_widgets["Pause"].config(text="Unpause")

    def __stop_test(self):
        self.stop = True
        self.looked_size = self.__tree.size()
        self.button_widgets["Pause"].config(state="disabled")
        self.button_widgets["Stop"].config(state="disabled")
        self.button_widgets["Test"].config(state="normal")

    def __execute_test(self):
        if self.looked_size == self.__tree.size() and not self.stop:
            self.looked_size += int(self.__get_value())

        while self.__tree.size() < self.looked_size and not self.stop:
            self.__test()

        if self.__tree.size() >= self.looked_size:
            self.__stop_test()

    def __reset(self):
        self.__draw()

    def __set_result(self, msg) -> None:
        self.result.config(text=f"RESULT: {msg}")

    def __show(self):
        plt.close('all')
        self.fig, self.ax = plt.subplots()
        self.__draw()

    def __add(self):
        try:
            value = self.__get_value()
            self.__set_result(self.__tree.add(self.type(value)))
            self.__reset()
        except ClassCastException:
            self.__set_result("The class cannot be compared!")
        except ValueError:
            self.__set_result("The value could not be initialized!")

    def __remove(self):
        try:
            value = self.__get_value()
            self.__set_result(self.__tree.remove(self.type(value)))
            self.__reset()
        except ClassCastException:
            self.__set_result("The class cannot be compared!")
        except ValueError:
            self.__set_result("The value could not be initialized!")

    def __clear(self):
        self.__tree.clear()
        self.__set_result("Tree correctly cleared!")
        self.__reset()

    def __tree_lower(self):
        try:
            value = self.__get_value()
            self.__set_result(self.__tree.lower(self.type(value)))
        except ClassCastException:
            self.__set_result("The class cannot be compared!")
        except ValueError:
            self.__set_result("The value could not be initialized!")

    def __higher(self):
        try:
            value = self.__get_value()
            self.__set_result(self.__tree.higher(self.type(value)))
        except ClassCastException:
            self.__set_result("The class cannot be compared!")
        except ValueError:
            self.__set_result("The value could not be initialized!")

    def __ceiling(self):
        try:
            value = self.__get_value()
            self.__set_result(self.__tree.ceiling(self.type(value)))
        except ClassCastException:
            self.__set_result("The class cannot be compared!")
        except ValueError:
            self.__set_result("The value could not be initialized!")

    def __floor(self):
        try:
            value = self.__get_value()
            self.__set_result(self.__tree.floor(self.type(value)))
        except ClassCastException:
            self.__set_result("The class cannot be compared!")
        except ValueError:
            self.__set_result("The value could not be initialized!")

    def __first(self):
        try:
            self.__set_result(self.__tree.first())
        except NoSuchElementException as err:
            self.__set_result("The tree is empty!")
        except ValueError:
            self.__set_result("The value could not be initialized!")

    def __last(self):
        try:
            self.__set_result(self.__tree.last())
        except NoSuchElementException as err:
            self.__set_result("The tree is empty!")

    def __poll_first(self):
        try:
            self.__set_result(self.__tree.poll_first())
            self.__reset()
        except NoSuchElementException as err:
            self.__set_result("The tree is empty!")

    def __poll_last(self):
        try:
            self.__set_result(self.__tree.poll_last())
            self.__reset()
        except NoSuchElementException as err:
            self.__set_result("The tree is empty!")

    def __size(self):
        self.__set_result(self.__tree.size())

    def __contains(self):
        try:
            value = self.__get_value()
            self.__set_result(self.__tree.contains(self.type(value)))
        except ClassCastException:
            self.__set_result("The class cannot be compared!")
        except ValueError:
            self.__set_result("The value could not be initialized!")

    def __draw(self):
        self.ax.clear()  # Clear the axis before drawing
        self.fig.subplots_adjust(left=0, bottom=0, right=1,
                                 top=1)  # Adjust the margins of the subplot
        self.__draw_node(self.ax, self.__tree._RedBlackTree__root)
        self.__draw_edges(self.ax, self.__tree._RedBlackTree__root)
        self.ax.axis('off')  # Hide axes
        plt.show(block=False)  # Non-blocking show

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
