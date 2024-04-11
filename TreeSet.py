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

    def balance_tree(self, node):
        if node is None:
            return None

        # Caso 1: El nodo es rojo, pero su padre es negro (o es la raíz)
        if node.parent is None or node.parent.color == "BLACK":
            return node

        parent = node.parent
        grandparent = parent.parent
        uncle = None

        # Caso 2: El tío del nodo es rojo
        if parent == grandparent.left:
            uncle = grandparent.right
        else:
            uncle = grandparent.left

        if uncle is not None and uncle.color == "RED":
            parent.color = "BLACK"
            uncle.color = "BLACK"
            grandparent.color = "RED"
            return self.balance_tree(grandparent)

        # Caso 3: El tío del nodo es negro o no existe
        if parent == grandparent.left:
            if node == parent.right:
                self.rotate_left(parent)
                node = parent
                parent = node.parent
            self.rotate_right(grandparent)
        else:
            if node == parent.left:
                self.rotate_right(parent)
                node = parent
                parent = node.parent
            self.rotate_left(grandparent)

        parent.color = "BLACK"
        grandparent.color = "RED"

        return node

    def rotate_left(self, node):
        # Rotación a la izquierda
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        # Rotación a la derecha
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child
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
