class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
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

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def pre_order(self) -> None:
        print(self.key, ' -> ', end='')
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

    def insertTree(self, the_side_to_insert, newTree):
        if the_side_to_insert == 'right':
            t = newTree
            if self.rightChild == None:
                self.rightChild = t
            else:
                t.getRightChild().rightChild = self.rightChild
                self.rightChild = t
        elif the_side_to_insert == 'left':
            t = newTree
            if self.leftChild == None:
                self.leftChild = t
            else:
                t.getLeftChild().leftChild = self.leftChild
                self.leftChild = t

    def delSubTree(self, the_side_to_delete):
        if the_side_to_delete == 'right':
            if self.rightChild == None:
                print('There nothing to delete')
            else:
                self.rightChild = None
        elif the_side_to_delete == 'left':
            if self.leftChild == None:
                print('There nothing to delete')
            else:
                self.leftChild = None

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

root2 = BinaryTree(33)
root2.insertLeft(55)
root2.insertRight(44)

root.pre_order()
print(root)

# вставляємо замість 10 нове дерево (root2) і з лівої дитини нового дерева (55) піде вліво вітка 10(ліва),5(ліва),23(права)
root.insertTree('left', root2)

root.pre_order()
print(root)

# Видаляємо 10,5,23
root.getLeftChild().getLeftChild().delSubTree('left')

root.pre_order()
print(root)

# Видаляємо 44
root.getLeftChild().delSubTree('right')

root.pre_order()
print(root)