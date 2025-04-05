from typing import Optional,List

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode])->List[int]:
        result=[]
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root)
        return result
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
output = sol.inorderTraversal(root)
print(output)
