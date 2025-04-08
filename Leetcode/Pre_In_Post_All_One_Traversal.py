class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    def All_Traversal(self, root):
        if not root:
            return [], [], []
        preorder, postorder, inorder  = [], [], []
        stack = [(root,1)] # state : pre,in,post

        while stack:
            node, state = stack.pop()
            if state==1:
                preorder.append(node.val)
                stack.append((node,2))
                if node.left:
                    stack.append((node.left,1))

            elif state ==2:
                inorder.append(node.val)
                stack.append((node,3))
                if node.right:
                    stack.append((node.right,1))
            
            else:

                postorder.append(node.val)
        return preorder,inorder, postorder
    
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
sol = Solution()
pre, ino, post = sol.All_Traversal(root)
print("Preorder:", pre)
print("Inorder:", ino)
print("Postorder:", post)