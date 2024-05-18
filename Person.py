class Person:
    def __init__(self, name, surname, age, DNI):
        self.__name = name
        self.__surname=surname
        self.__age=age
        self.__DNI=DNI

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def DNI(self):
        return self.__DNI

    @DNI.setter
    def DNI(self, DNI):
        self.__DNI = DNI

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.DNI == other.DNI
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Person):
            return self.DNI <= other.DNI
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.DNI < other.DNI
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Person):
            return self.DNI >= other.DNI
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Person):
            return self.DNI > other.DNI
        return NotImplemented
    
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
    
    def __hash__(self):
        return hash(self.DNI)
    
    def __str__(self):
        return self.name+",\n"+self.surname+",\n"+self.age+",\n"+self.DNI

class Person_NoComparable:
    def __init__(self, name, surname, age, DNI):
        self.__name = name
        self.__surname=surname
        self.__age=age
        self.__DNI=DNI

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def DNI(self):
        return self.__DNI

    @DNI.setter
    def DNI(self, DNI):
        self.__DNI = DNI

    def __hash__(self):
        return hash(self.DNI)
    
    def __str__(self):
        return self.name+",\n"+self.surname+",\n"+self.age+",\n"+self.DNI

class Person_HalfComparable:
    def __init__(self, name, surname, age, DNI):
        self.__name = name
        self.__surname=surname
        self.__age=age
        self.__DNI=DNI

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def DNI(self):
        return self.__DNI

    @DNI.setter
    def DNI(self, DNI):
        self.__DNI = DNI

    def __eq__(self, other):
        if isinstance(other, Person_NoComparable):
            return self.DNI == other.DNI
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Person_NoComparable):
            return self.DNI < other.DNI
        return NotImplemented    

    def __hash__(self):
        return hash(self.DNI)
    
    def __str__(self):
        return self.name+",\n"+self.surname+",\n"+self.age+",\n"+self.DNI


