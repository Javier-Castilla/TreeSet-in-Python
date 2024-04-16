import time
import tkinter as tk
from random import randint
from tkinter import ttk

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from TreeSet import TreeSet

if __name__ == "__main__":
    items = [randint(0, 100) for _ in range(30)]
    t = TreeSet(int, items)
    print(t, items)
    t.draw_tree()
