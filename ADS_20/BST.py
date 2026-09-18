class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right=None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root,data)

    def insert_recursive(self,current,data):
        if data< current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self.insert_recursive(current.left,data)
        elif data> current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self.insert_recursive(current.right,data)


    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
        return

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end= " ")
        return
    
    def preorder(self,root):
        if root:
            print(root.data,end =" ")
            self.preorder(root.left)
            self.preorder(root.right)
        return

    def print_2d_tree(self, root, space=0, height=5):
        if root is None:
            return
        space += height
        self.print_2d_tree(root.right, space, height)
        print()
        print('-- ' * (space - height) + str(root.data))
        self.print_2d_tree(root.left, space, height)


Tree = BST()

def main():
    while True:
    
        print("\n========== BST MENU ==========")
        print("1. Insert")
        print("2. Inorder")
        print("3. Preorder")
        print("4. Postorder")
        print("5. Display")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = input("Enter value: ")
            Tree.insert(value)

        elif choice == 2:
            Tree.inorder(Tree.root)
        elif choice == 3:
            Tree.preorder(Tree.root)
        elif choice == 4:
            Tree.postorder(Tree.root)
        elif choice == 5:
            Tree.print_2d_tree(Tree.root)

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


# print("The Inorder Traversal:")
# Tree.inorder(Tree.root)
# print("\nThe Postorder Traversal: ")
# Tree.postorder(Tree.root)
# print("\nThe Preorder Traversal:")
# Tree.preorder(Tree.root)

# Tree.print_2d_tree(Tree.root)   