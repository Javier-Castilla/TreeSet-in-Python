import time
import tkinter as tk
from random import randint
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from TreeSet import TreeSet

if __name__ == "__main__":
    t = TreeSet(int)
    t.add_all([1,2,3,4])
    t.draw_buttons()
