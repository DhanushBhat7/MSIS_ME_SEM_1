class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if root is None:
            return Node(data) 
        if data < root.data:
            root.left = self.insert(root.left,data)
        elif data > root.data:
            root.right = self.insert(root.right,data)

        return root

    def display(self,root,level=0):
        if root is not None:
            self.display(root.right,level+1)
            print("  " * level+str(root.data))
            self.display(root.left,level+1)

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end =" ")
            self.inorder(root.right)

    def preorder(self,root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end =" ")

    def find_min(self,root):
        while root.left is not None:
            root = root.left
        return root 

    def delete(self,root,data):
        if root is None:
            return None

        if data < root.data:
            root.left = self.delete(root.left,data)

        elif data > root.data:
            root.right = self.delete(root.right,data)

        else:
            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,temp.data)
        return root 


bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for i in values:
    bst.root = bst.insert(bst.root,i)

bst.display(bst.root)

bst.inorder(bst.root)
bst.preorder(bst.root)
bst.postorder(bst.root)


bst.delete(bst.root,30)

bst.display(bst.root)
