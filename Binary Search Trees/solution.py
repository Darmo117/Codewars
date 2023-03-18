class Tree:
    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left:
            assert type(left) == Tree and left.root < root
        if right:
            assert type(right) == Tree and root < right.root
        self.root = root
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        return not self.left and not self.right

    def __eq__(self, other):
        return (isinstance(other, Tree) and self.root == other.root
                and self.left == other.left and self.right == other.right)

    def __str__(self):
        if self.is_leaf():
            return f'[{self.root}]'
        left = '_' if not self.left else str(self.left)
        right = '_' if not self.right else str(self.right)
        return f'[{left} {self.root} {right}]'


class Node:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)
