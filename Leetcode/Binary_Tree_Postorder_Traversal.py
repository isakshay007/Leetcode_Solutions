from typing import Optional,List

class TreeNode:
    def __init__(self, val, left= None, right= None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode])->List[int]:
        result=[]

        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                result.append(node.val)
    

        postorder(root)
        return result
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
output = sol.postorderTraversal(root)
print(output)