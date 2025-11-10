class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def search(self, node, key):
        if node is None:
            return None
        if node.data == key:
            return node
        if key < node.data:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self.delete(node.left, key)
        elif key > node.data:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.findMin(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


obj = BST()

while True:
    print("1. Insert Node")
    print("2. Search Node")
    print("3. Delete Node")
    print("4. Display (Inorder)")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        val = int(input("Enter value to insert: "))
        obj.root = obj.insert(obj.root, val)
    elif ch == 2:
        key = int(input("Enter value to search: "))
        res = obj.search(obj.root, key)
        if res:
            print("Node Found")
        else:
            print("Node Not Found")
    elif ch == 3:
        key = int(input("Enter value to delete: "))
        obj.root = obj.delete(obj.root, key)
    elif ch == 4:
        print("Inorder Traversal:")
        obj.inorder(obj.root)
        print()
    elif ch == 5:
        break
    else:
        print("Invalid Choice")