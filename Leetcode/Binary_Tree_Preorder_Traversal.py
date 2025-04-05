from typing import Optional,List

class TreeNode:
    def __init__(self, val, left= None, right= None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode])->List[int]:
        result=[]

        def preorder(node):
            if node:
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)
    

        preorder(root)
        return result
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
output = sol.preorderTraversal(root)
print(output)