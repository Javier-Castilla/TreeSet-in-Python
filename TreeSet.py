from TreeNode import *
from data_utils import *

E = TypeVar('E')


class TreeSet:
    """Class that represents a set based on a tree. The elements are ordered
    using its natural ordering.

    Since this implementation uses a Red-Black Tree, it provides guaranteed
    log(n) time cost for the basic operations.

    TreeSet string representation will be provided inorder.
    """

    def __init__(self, class_type: Union[E, Sequence[E]]) -> None:
        """
        Initialize an empty TreeSet if type is given or constructs one with the
        elements contained into the given sequence.

        :param class_type: The generic type of the class or a sequence with
        element to construct the TreeSet
        :type class_type: Union[E, Sequence[E]]
        """
        self.__root = None
        self.__size = 0

        if isinstance(class_type, Sequence):
            if len(set(map(type, class_type))) != 1:
                raise TypeError("Sequence elements type must be the same")

            self.class_type = type(class_type[0])

            for item in class_type:
                self.add(item)
        else:
            self.class_type = class_type

    def add(self, value: Any) -> bool:
        """Inserts the given value into the TreeSet if value is not contained.

        :param: Value to insert into the TreeSet
        :return: True if the value have been added to the TreeSet else False
        :rtype: bool
        :raises AssertionError: If the given value's type does not match generic
        type
        """
        assert isinstance(value, self.class_type), \
            f"Value type must be '{self.class_type}'"

        new_node = TreeNode(value, TreeNode.Color.RED)

        if (parent := self.__contains(value)) != new_node:
            if not parent:
                self.__root = new_node
            elif new_node < parent:
                parent.left = new_node
                new_node.parent = parent
            else:
                parent.right = new_node
                new_node.parent = parent
        else:
            return False

        self.__size += 1

        self.__fix_insertion(new_node)
        return True

    def add_all(self, elements: Sequence[E]) -> bool:
        """Inserts the given values into the TreeSet. If some value is
        already contained, it will not be inserted.

        :param: Values to insert into the TreeSet.
        :return: True if the value have been added to the TreeSet else False
        :rtype: bool
        :raises AssertionError: If the given value's type does not match generic
        type
        """
        old_size = len(self)
        for element in elements:
            self.add(element)

        return len(self) != old_size

    def remove(self, value: Any) -> bool:
        if self.is_empty() or (root := self.__contains(value)).value != value:
            return False

        if root == self.__root and len(self) == 1:
            self.__root = None
        else:
            parent = None
            current = root.right
            while current:
                parent = current
                current = current.left

            if not parent:
                current = root.left
                while current:
                    parent = current
                    current = current.right

            root.value = parent.value
            if parent.parent and parent < parent.parent:
                parent.parent.left = parent.right
            else:
                parent.parent.right = parent.right

        self.__size -= 1
        return True

    def __contains(self, value: TreeNode) -> TreeNode:
        if not len(self):
            return self.__root

        parent = None
        root = self.__root

        while root:
            if root.value == value:
                return root

            parent = root
            root = root.left if value < root.value else root.right

        return parent

    def __fix_insertion(self, node: TreeNode):
        while node != self.__root and node.parent.color == TreeNode.Color.RED:

            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle and uncle.color == TreeNode.Color.RED:
                    node.parent.color = TreeNode.Color.BLACK
                    uncle.color = TreeNode.Color.BLACK
                    node.parent.parent.color = TreeNode.Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__left_rotation(node)

                    node.parent.color = TreeNode.Color.BLACK
                    node.parent.parent.color = TreeNode.Color.RED
                    self.__right_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle and uncle.color == TreeNode.Color.RED:
                    node.parent.color = TreeNode.Color.BLACK
                    uncle.color = TreeNode.Color.BLACK
                    node.parent.parent.color = TreeNode.Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__right_rotation(node)

                    node.parent.color = TreeNode.Color.BLACK
                    node.parent.parent.color = TreeNode.Color.RED
                    self.__left_rotation(node.parent.parent)

        self.__root.color = TreeNode.Color.BLACK

    def __left_rotation(self, node):
        other = node.right
        node.right = other.left

        if other.left:
            other.left.parent = node
        other.parent = node.parent

        if node.parent is None:
            self.__root = other
        elif node == node.parent.left:
            node.parent.left = other
        else:
            node.parent.right = other

        other.left = node
        node.parent = other

    def __right_rotation(self, node: TreeNode):
        other = node.left
        node.left = other.right

        if other.right:
            other.right.parent = node
        other.parent = node.parent

        if node.parent is None:
            self.__root = other
        elif node == node.parent.right:
            node.parent.right = other
        else:
            node.parent.left = other

        other.right = node
        node.parent = other

    def clear(self) -> None:
        self.__root = None

    def is_empty(self):
        return len(self)

    def __len__(self) -> int:
        return self.__size

    def __iter__(self):
        stack = SimpleStack()
        current = self.__root

        while True:
            if current:
                stack.push(current)
                current = current.left
            elif not stack.is_empty():
                current = stack.pull()
                yield current
                current = current.right
            else:
                break

    def __str__(self) -> str:
        return f"{[node.value for node in self]}"

    def __contains__(self, item):
        return self.__contains(node := TreeNode(item, TreeNode.Color.RED)) == node


if __name__ == "__main__":
    t = TreeSet([num for num in range(10)])
    print(t.add_all([num for num in range(10)]))

    print(t)
