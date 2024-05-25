from abc import ABC, abstractmethod


# EQ LT
class Person:
    """
    Class to represent a person. Implements eq and lt methods to compare objects.
    """

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.__age == other.age
        return False

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return False

    def __str__(self):
        return f"{self.__name} ({self.__age})"

    def __repr__(self):
        return f"Person({self.__name}, {self.__age})"


# (PERSON) EQ LT
class Worker(Person):
    """
    Class to represent a worker. Inherits from Person and adds a job attribute.
    Implements eq and lt methods to compare objects.
    """

    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.__job = job

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, job):
        self.__job = job


class LazyWorker(Worker):
    """
    Class to represent a lazy worker. Inherits from Worker and adds a laziness attribute.
    Implements eq and lt methods to compare objects.
    """

    def __init__(self, name, age, job, laziness):
        super().__init__(name, age, job)
        self.__laziness = laziness

    @property
    def laziness(self):
        return self.__laziness

    @laziness.setter
    def laziness(self, laziness):
        self.__laziness = laziness

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass


# EQ GT
class Professor:
    """
    Class to represent a professor. Implements eq and gt methods to compare objects.
    Implements eq and gt methods to compare objects.
    """

    def __init__(self, name, subject):
        self.__name = name
        self.__subject = subject

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject

    def __eq__(self, other):
        if isinstance(other, Professor):
            return self.__subject == other.subject
        return False

    def __gt__(self, other):
        if isinstance(other, Professor):
            return self.name > other.name
        return False


# LT
class Student:
    """
    Class to represent a student. Implements lt method to compare objects.
    Implements lt method to compare objects.
    """

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__id < other.id
        return False


# Abstract class
class Alien(ABC):
    """
    Abstract class to represent an alien. Implements eq method to compare objects.
    """

    def __init__(self, name, planet):
        self.__name = name
        self.__planet = planet

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def planet(self):
        return self.__planet

    @planet.setter
    def planet(self, planet):
        self.__planet = planet

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass


# EQ LT from abstract class
class Martian(Alien):
    """
    Class to represent a Martian. Inherits from Alien and adds a color attribute.
    Implements eq and lt methods to compare objects.
    """

    def __init__(self, name, planet, color):
        super().__init__(name, planet)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def __eq__(self, other):
        if isinstance(other, Alien):
            return self.planet == other.planet
        return False

    def __lt__(self, other):
        if isinstance(other, Alien):
            return self.planet < other.planet
        return False

    def __repr__(self):
        return f"Martian({self.name}, {self.planet})"


class Venusian(Alien):
    """
    Class to represent a Venusian. Inherits from Alien and adds a size attribute.
    Implements eq and lt methods to compare objects.
    """

    def __init__(self, name, planet, size):
        super().__init__(name, planet)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def __eq__(self, other):
        if isinstance(other, Alien):
            return self.planet == other.planet
        return False

    def __lt__(self, other):
        if isinstance(other, Alien):
            return self.planet < other.planet
        return False

    def __repr__(self):
        return f"Venusian({self.name}, {self.planet})"
