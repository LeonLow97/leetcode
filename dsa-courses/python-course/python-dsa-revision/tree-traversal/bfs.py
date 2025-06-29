class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
                if val == current.val:
                    return False
                # visit right side of the tree
                elif val > current.val:
                    # check if right side of tree has space
                    if current.right is None:
                        current.right = newNode
                        return self
                    else:
                        current = current.right
                # visit left side of the tree
                elif val < current.val:
                    if current.left is None:
                        current.left = newNode
                        return self
                    else:
                        current = current.left

    def BFS(self):
        queue = []
        visited = []
        current = self.root

        if self.root is None:
            return False
        else:
            queue.append(current)

        while len(queue) > 0:
            current = queue.pop(0)
            visited.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return visited

tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(16)
tree.insert(7)

print(tree.BFS()) # [10, 5, 13, 2, 7, 11, 16]