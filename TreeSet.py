from TreeNode import *
from simple_queue import *

E = TypeVar('E')

class TreeSet:
    def __init__(self, class_type: E | Sequence[E]) -> None:
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

    def __contains(self, node: TreeNode) -> Any | TreeNode:
        if self.__root is None:
            return self.__root

        parent = None
        root = self.__root

        while root:
            if root == node:
                return root

            parent = root
            root = root.left if node < root else root.right

        return parent

    def r(self):
        return self.__root

    def add(self, value: Any) -> bool:
        assert isinstance(value, self.class_type), \
            f"Value type must be '{self.class_type}'"

        new_node = TreeNode(value, Color.RED)

        if (parent := self.__contains(new_node)) != new_node:
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
        return True

    def remove(self, value: Any) -> bool:
        new_node = TreeNode(value, Color.RED)

        if self.is_empty() or (root := self.__contains(new_node)) != new_node:
            return False

        parent = None
        current = root.right
        while current:
            parent = current
            current = current.left

        if parent:
            root.value = parent.value
            if parent.parent and parent < parent.parent:
                parent.parent.left = parent.right
            else:
                parent.parent.right = parent.right

            self.__size -= 1

    def is_empty(self):
        return len(self) == 0

    def __len__(self) -> int:
        return self.__size

    def __iter__(self):
        queue = SimpleQueue(self.__root)

        while not queue.is_empty():
            node = queue.dequeue()
            yield node

            if not node:
                continue

            queue.enqueue(node.left)
            queue.enqueue(node.right)

    def __str__(self) -> str:
        return f"{[node for node in self]}"

    def __contains__(self, item):
        return self.__contains(node := TreeNode(item, Color.RED)) == node


if __name__ == "__main__":
    t = TreeSet(int)
    t1 = TreeSet([1, 2, 3, 4, 5])
    items = [5, 4, 10, 7, 3, 11, 19, 15, 6]
    non_items = [1, 2, 20]
    t.add(5)
    t.add(4)
    t.add(10)
    t.add(7)
    t.add(3)
    t.add(11)
    t.add(19)
    t.add(15)
    t.add(6)

    print(t)
