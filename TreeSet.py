from TreeNode import *
class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, e):
        if not self.contains(e):
            new_node = TreeNode(e)
            if self.root is None:
                self.root = new_node
                self.root.color = "BLACK"
                return True

            parent = None
            current = self.root
            while current:
                parent = current
                if e < current.value:
                    current = current.left
                else:
                    current = current.right

            if e < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node

            new_node.parent = parent
            return True
        else:
            return False

    def contains(self, item):
        current = self.root
        while current:
            if item == current.value:
                return True
            elif item < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def remove(self, e):
        if not self.contains(e):
            return False
        else:
            self.root = self.remove_helper(self.root, e)
            if self.root is not None:
                self.root.color = "BLACK"
            return True

    def remove_helper(self, node, e):
        if node is None:
            return None

        if e < node.value:
            node.left = self.remove_helper(node.left, e)
        elif e > node.value:
            node.right = self.remove_helper(node.right, e)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.minimum(node.right)
                node.value = successor.value
                node.right = self.remove_helper(node.right, successor.value)

        return self.balance_tree(node)

    def minimum(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def isEmpty(self):
        return self.size(self.root) == 0

    def iterator(self, node):
        if node:
            yield from self.iterator(node.left)
            yield node.value
            yield from self.iterator(node.right)

if __name__ == "__main__":
    my_tree = TreeSet()
    # AGREGAR ELEMENTOS
    print(my_tree.add(1))
    print(my_tree.add(2))
    print(my_tree.add(3))
    print(my_tree.add(2))  # Este ya existe, debería devolver False

    # TAMAÑO
    print(my_tree.size(my_tree.root))

    # SI ESTÁ VACÍO
    print(my_tree.isEmpty())

    # VERIFICAR SI CONTIENE LOS ELEMENTOS
    print(my_tree.contains(1))
    print(my_tree.contains(4))

    # ITERAR SOBRE LOS ELEMENTOS DEL CONJUNTO
    for i in my_tree.iterator(my_tree.root):
        print(i, end=" ")

    # ELIMINAR ELEMENTO
    print(my_tree.remove(2))
