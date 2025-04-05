class TreeNode:
    def __init__(self, val=0, left= None, right=None):
        self.val = val
        self.left= left
        self.right = right

class Solution:
    def rightView(self, root):
        res=[]
        self.rightRecursion(root,0,res)
        return res
    
    def leftView(self, root):
        res=[]
        self.leftRecursion(root,0,res)
        return res
    
    def rightRecursion(self, root, level, res):
        if root is None:
            return
        
        if len(res)==level:
            res.append(root.val)

        self.rightRecursion(root.right, level+1,res)
        self.rightRecursion(root.left, level+1,res)

    def leftRecursion(self, root, level, res):
        if root is None:
            return
        
        if len(res)==level:
            res.append(root.val)

        self.leftRecursion(root.left, level+1,res)
        self.leftRecursion(root.right, level+1,res)
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left =TreeNode(4)
root.left.right = TreeNode(10)
root.left.left.right = TreeNode(5)
root.left.left.right.right = TreeNode(6)
root.right = TreeNode(3)
root.right.left = TreeNode(9)
root.right.right = TreeNode(10)

solution = Solution()

# Get and print Right View
rightView = solution.rightView(root)
print("Right View Traversal:", end=" ")
for node in rightView:
    print(node, end=" ")
print()

# Get and print Left View
leftView = solution.leftView(root)
print("Left View Traversal:", end=" ")
for node in leftView:
    print(node, end=" ")
print()