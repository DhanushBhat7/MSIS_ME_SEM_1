class Tree:
    def __init__(self,data):
        self.data = data
        self.child =[]

    def add_child(self,childnode):
        self.child.append(childnode)

    def print_tree(self,level=0):
        indent = "  " * level + "|--" if level > 0 else ""
        print(f"{indent}{self.data}")
        for child in self.child:
            child.print_tree(level+1)


tree = Tree("Electronics")

laptop = Tree("Laptop")
Mobile = Tree("Mobile")

tree.add_child(laptop)
tree.add_child(Mobile)

hp = Tree("HP")
dell = Tree("Dell")

Samsung =Tree("Samsung")
Apple = Tree("Apple")

laptop.add_child(hp)
laptop.add_child(dell)

Mobile.add_child(Samsung)
Mobile.add_child(Apple)

tree.print_tree()

