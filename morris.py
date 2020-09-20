class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def morrisInorder(self):
        ptr = self
        while ptr != None:
            if ptr.left == None:
                print(ptr.val,end=' ')
                ptr = ptr.right
            else:
                predecessor = self.getpredecessor(ptr)                        
                if predecessor.right == None:
                    predecessor.right = ptr
                    ptr = ptr.left
                elif predecessor.right != None:                
                    print(ptr.val,end=' ')
                    predecessor.right = None                
                    ptr = ptr.right
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


