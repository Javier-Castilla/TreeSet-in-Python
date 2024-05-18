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


if __name__ == "__main__":
    s1 = Student("John", 1)
    s2 = Student("Mary", 2)
    print(id(Student.__eq__), id(object.__eq__))