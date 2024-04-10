from TreeNode import *


class TreeSet:

    RED = TreeNode.Color.RED
    BLACK = TreeNode.Color.BLACK

    def __init__(self):
    
        self.root = None
        self.size = 0


    def add(self, valor):
        
        if self.contains(valor):
            return False
        
        else:
            nodo = TreeNode(valor)
            if not self.root:
                self.root = nodo
            else:
                self._add_recursive(nodo, valor)
        self.size + 1
        return True
    
    def _add_recursive(self, nodo: TreeNode, valor):
        if valor < nodo.value:
            if nodo.left:
                self._add_recursive(nodo.left, valor)
            else:
                nodo.left = TreeNode(valor)
        elif valor > nodo.value:
            if nodo.right:
                self._add_recursive(nodo.right, valor)
            else:
                nodo.right = TreeNode(valor)

    def remove(self, valor):
        if self.is_empty or not self.contains(valor):
            return False
        else:
            self.root = self._remove_recursive(self.root, valor)

    def _remove_recursive(self, node:TreeNode, valor):
        if valor < node.value:
            node.left = self._remove_recursive(node.left, valor)
        elif valor > node.value:
            node.right = self._remove_recursive(node.right, valor)
        else: # Found the node to remove
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                # Node has both left and right children
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._remove_recursive(node.right, successor.value)

        return node

    def _find_min(self, node: TreeNode):
        current = node
        while current.left:
            current = current.left
        return current

    def is_empty(self):
        return len(self) == 0

    def contains(self, valor):
        return valor in self

  
