# PreOrder: Root, Left, Right

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return self
        else:
            current = self.root
            while True:
                if val == current.val: return None

                if val < current.val:
                    if current.left is None:
                        current.left = newNode
                        return self
                    else:
                        current = current.left

                if val > current.val:
                    if current.right is None:
                        current.right = newNode
                        return self
                    else:
                        current = current.right

    def preOrder(self):
        if self.root is None: return None

        data = []
        current = self.root

        def traverse(node):
            data.append(node.val)
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
            return

        traverse(current)
        return data

tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(16)
tree.insert(7)

print(tree.preOrder())

'''
            10
        5       13
      2   7   11   16
'''















