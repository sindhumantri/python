class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insertion(self,rt, new_node):
        if rt.val > new_node.val:
            if rt.left == None:
                rt.left = new_node
            else:
                self.insertion(rt.left, new_node)
        else:
            if rt.right == None:
                rt.right = new_node
            else:
                self.insertion(rt.right, new_node)
                
    def levelOrderTraversal(self,rt):
        queue = []
        levelOrder = []
        cur = rt
        queue.append((cur,0))
        while len(queue) > 0:
            node, depth = queue.pop(0)
            levelOrder.append((node.val, depth))
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        i = 0
        j = 0
        while i < len(levelOrder):
            while i < len(levelOrder) and levelOrder[i][1] == j:
                print ("%d %d" % (levelOrder[i][0], levelOrder[i][1]))
                i = i+1
            print ("-----")
            j = j + 1
        print (levelOrder) 
        
    def height(self,rt):
        if rt == None:
            return 0
        if rt.left == None and rt.right == None:
            return 1
        else:
            return max(self.height(rt.right), self.height(rt.left)) + 1
    
    def isBalancedTree(self,rt):
        if rt == None:
            return True
        if rt.left == None and rt.right == None:
            return True
        left_height = self.height(rt.left)
        right_height = self.height(rt.right)
        if abs(left_height - right_height) > 1:
            return False
        else:
            return self.isBalancedTree(rt.left) and self.isBalancedTree(rt.right)
    
    def search(self,rt,value):
        cur = rt
        if cur == None:
            return None
        elif cur.val == value:
            return cur
        elif cur.val > value:
            self.search(cur.left, value)
        else:
            self.search(cur.right, value)
            
    
    def topView(self,rt):
        topview = []
        cur = rt
        while cur:
            topview.append(cur.val)
            cur = cur.left
        topview.reverse()
        topview.pop()
        cur = rt
        while cur:
            topview.append(cur.val)
            cur = cur.right
        return topview

    def preOrder(self,rt):
        if rt == None:
            return
        print (rt.val)
        self.preOrder(rt.left)
        self.preOrder(rt.right)
    
    def postOrder(self,rt):
        if rt == None:
            return
        self.postOrder(rt.left)
        self.postOrder(rt.right)
        print (rt.val)
        
    def inOrder(self,rt):
        if rt == None:
            return
        self.inOrder(rt.left)
        print (rt.val)
        self.inOrder(rt.right)
    

bt = BinaryTree()
bt.root = Node(20)
"""bt.root.left = Node(30)
bt.root.right = Node(40)
bt.root.left.left = Node(30)
bt.root.right.left = Node(50)
print ("------PreOrder-------")
bt.preOrder(bt.root)
print ("-----PostOrder--------")
bt.postOrder(bt.root)
print ("-----InOrder-------")
bt.inOrder(bt.root)
print ("-------Height of the tree-------")
height = bt.height(bt.root)
print (height)
print ("-----TopView------")
print (bt.topView(bt.root))
print ("------Level Order Traversal-------")
bt.levelOrderTraversal(bt.root)"""
print ("------Binary Tree Insertion------")
bt.insertion(bt.root, Node(10))
bt.insertion(bt.root, Node(5))
bt.insertion(bt.root, Node(20))
bt.insertion(bt.root, Node(30))
bt.insertion(bt.root, Node(60))
bt.inOrder(bt.root)
print ("-----is Balanced Tree------")
print (bt.isBalancedTree(bt.root))
print ("-----Search Element in BT------")
res = bt.search(bt.root, 20)
print (res)
