import time
import tkinter as tk
from random import randint
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Person import Person
from TreeSet import TreeSet

if __name__ == "__main__":
    t = TreeSet(int)
    person1=  Person("Nombre1", "Apellido1", "EDAD1", "DNI1")
    person2=  Person("Nombre2", "Apellido2", "EDAD2", "DNI2")


    print(t)

