from enum import Enum
from functools import total_ordering
from typing import *


class Color(Enum):
    BLACK = 0
    RED = 1


@total_ordering
class TreeNode:
    def __init__(self, value: Any, color: Color) -> None:
        self.value = value
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

    @property
    def value(self) -> Any:
        return self.__value

    @value.setter
    def value(self, value: Any) -> None:
        self.__value = value

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, color: Color) -> None:
        assert isinstance(color, Color), "Value type should be Color"
        assert color in {Color.RED, Color.BLACK},\
            "Value must be 0 ('BLACK') or 1 ('RED')"

        self.__color = color

    @property
    def left(self) -> Any:
        return self.__left

    @left.setter
    def left(self, node: 'TreeNode') -> None:
        self.__left = node

    @property
    def right(self) -> Any:
        return self.__right

    @right.setter
    def right(self, node: 'TreeNode') -> None:
        self.__right = node

    def __eq__(self, other: 'TreeNode') -> bool:
        if isinstance(other, TreeNode):
            return self.value == other.value
        else:
            return False

    def __lt__(self, other: 'TreeNode') -> bool:
        if isinstance(other, TreeNode):
            return self.value < other.value
        else:
            raise False

    def __str__(self) -> str:
        #return f"({self.value}, {self.color})"
        return f"({self.value}: {self.left if self.left is None else self.left.value}, {self.right if self.right is None else self.right.value})"

    def __repr__(self) -> str:
        return f"TreeNode({self.value}, {self.color})"


if __name__ == "__main__":
    nodes = [TreeNode(i, Color.RED) for i in range(10)]
    for node in nodes:
        print(node)