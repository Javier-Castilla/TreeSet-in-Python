class TreeNode(Node):
    def __init__(self, value, color: 'TreeNode.Color') -> None:
        self.value = value
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

    class Color(Enum):
        RED = 1
        BLACK = 0
