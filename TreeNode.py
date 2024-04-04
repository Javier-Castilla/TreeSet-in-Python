class Node:
    def __init__(self, value : object) -> None:


    @property
    def value(self) -> object:
        return self.__value

    @value.setter
    def value(self, value: object) -> None:
        self.__value = value
    
    @property
    def color(self) -> int:
        return self.__color

    @color.setter
    def color(self, color: int) -> None:
        assert isinstance(color, int), "Value type should be int"
        assert isinstance()

        self.__color = color