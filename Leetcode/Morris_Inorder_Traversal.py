from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def morrisInorderTraversal(self, root: Optional[TreeNode])->List[int]:
        result=[]
        curr = root

        while curr:

            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right!=curr:
                    pre = pre.right

                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    result.append(curr.val)
                    curr = curr.right
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.morrisInorderTraversal(root))  # Output: [1, 3, 2]