class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def pre_order(self) -> None:
        print(self.key, ' -> ', end ='')
        if self.leftChild:
            self.leftChild.pre_order()
        if self.rightChild:
            self.rightChild.pre_order()

    def post_order(self) -> None:
        if self.leftChild:
            self.leftChild.post_order()
        if self.rightChild:
            self.rightChild.post_order()
        # print(self.key)
        print(self.key, ' -> ', end='')

    def in_order(self) -> None:
        if self.leftChild:
            self.leftChild.in_order()
        # print(self.get_root_val())
        print(self.key, ' -> ', end='')
        if self.rightChild:
            self.rightChild.in_order()

    def insert_tree(self, position, new_tree):
        if position == 'left':
            if self.leftChild is None:
                self.leftChild = new_tree
            else:
                tree = new_tree
                tree.leftChild = self.leftChild
                self.leftChild = tree
        elif position == 'right':
            if self.rightChild is None:
                self.rightChild = new_tree
            else:
                tree = new_tree
                tree.rightChild = self.rightChild
                self.rightChild = tree

    def remove_subtree(self, position):
        if position == "left":
            self.leftChild = None
        elif position == "right":
            self.rightChild = None



root = BinaryTree(3)
print(root.getRootVal())
root.insertLeft(5)
print(root.getLeftChild().getRootVal())
root.insertLeft(10)
print(root.getLeftChild().getRootVal())
root.getLeftChild().getLeftChild().insertRight(23)
print(root.getLeftChild().getLeftChild().getRightChild().getRootVal())
root.insertRight(4)
print(root.getRightChild().getRootVal())
root.pre_order()
print()
root.post_order()
print()
root.in_order()

# creating a subtree

subtree = BinaryTree('100')
subtree.insertLeft('200')
subtree.insertRight('500')
print()
print('here is a subtree:')
subtree.pre_order()

# inserting a subtree to root

root.insert_tree('left', subtree)
print()
print('here is a root after subtree inserting:')
root.in_order()

# removing subtree

root.remove_subtree('left')
print()
print('here is a root after subtree removing:')
root.in_order()

