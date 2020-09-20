class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def morrisInorder(self):
        current = self
        while current != None:
            if current.left == None:
                print(current.val,end=' ')
                current = current.right
            else:
                predecessor = self.getpredecessor(current)                        
                if predecessor.right == None:
                    predecessor.right = current
                    current = current.left
                elif predecessor.right != None:                
                    print(current.val,end=' ')
                    predecessor.right = None                
                    current = current.right
        print()

    def getpredecessor(self, root):
        predecessor = root.left
        while predecessor.right != root and predecessor.right != None:
            predecessor = predecessor.right
        return predecessor


root = Tree('5')

root.left = Tree('3')
root.left.left = Tree('2')
root.left.left.left = Tree('1')
root.left.right = Tree('4')

root.right = Tree('7')
root.right.left = Tree('6')
root.right.right = Tree('8')

root.morrisInorder()


