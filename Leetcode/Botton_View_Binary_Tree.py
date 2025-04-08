from collections import defaultdict
from queue import Queue

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def bottomView(self, root):
        ans = []
        if root is None:
            return ans
        
        mpp = defaultdict(int)

        q = Queue()
        q.put((root,0))

        while not q.empty():
            node, hd = q.get()

            mpp[hd] = node.val

            if node.left:
                q.put((node.left,hd-1))
            
            if node.right:
                q.put((node.right,hd+1))
        
        for key in sorted(mpp.keys()):
            ans.append(mpp[key])
        return ans
        
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(10)
root.left.left.right = TreeNode(5)
root.left.left.right.right = TreeNode(6)
root.right = TreeNode(3)
root.right.left = TreeNode(9)
root.right.right = TreeNode(10)


solution = Solution()
bottomView = solution.bottomView(root)

print("Bottom View Traversal:")
for node in bottomView:
    print(node, end=" ")