#! /usr/bin/python

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Binarytree:
  def __init__(self):
    self.root = None
  
  def insert(self, rt, new_node):
    print "inserting value %s" % new_node.value 
    if rt == None:
      rt = new_node
    else:
      # its not empty tree
      if rt.value > new_node.value:
        # insert to the left
        if rt.left == None:
          rt.left = new_node
        else:
          self.insert(rt.left, new_node)
      else:
        # insert to the right
        if rt.right == None:
          rt.right = new_node
        else:
          self.insert(rt.right, new_node)

	def minimumBST(self, rt):
		if rt == None:
			return
		cur = rt
		while cur.left:
			if cur.left:
				cur = cur.left
		return cur.value
	
	def maximumBST(self, rt):
		if rt == None:
			return
		cur = rt
		while cur.right:
			if cur.right:
				cur = cur.right
		return cur.value
		
  def print_inorder(self, rt):
    if rt == None:
      return 
    self.print_inorder(rt.left)
    print rt.value
    self.print_inorder(rt.right)
 
  
  def print_preorder(self, rt):
    if rt is None:
      return 
    
    print rt.value
    self.print_preorder(rt.left)
    self.print_preorder(rt.right)
 
  def print_postorder(self, rt):
    if rt is None:
      return 

    self.print_postorder(rt.left)
    self.print_postorder(rt.right)
    print rt.value
 
def main():
  bt = Binarytree()
  bt.root = Node(10)
  bt.print_inorder(bt.root) 
  bt.insert(bt.root, Node(30))
  bt.print_inorder(bt.root) 
  bt.insert(bt.root, Node(20))
  bt.print_inorder(bt.root) 
  bt.insert(bt.root, Node(5))
  bt.print_inorder(bt.root) 
  bt.insert(bt.root, Node(6))
  bt.print_inorder(bt.root) 

if __name__ == "__main__":
  main()
