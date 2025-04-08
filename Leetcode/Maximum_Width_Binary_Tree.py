from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        queue = deque()
        queue.append((root,0))
        max_width=0
        while queue:
            level_size = len(queue)
            _,first_idx = queue[0]
            for i in range(level_size):
                node, idx = queue.popleft()
                curr_idx = idx-first_idx
                if i==0:
                    left_idx = curr_idx
                if i== level_size-1:
                    right_idx = curr_idx
                if node.left:
                    queue.append((node.left,2*curr_idx))
                if node.right:
                    queue.append((node.right,2*curr_idx+1))

            level_width = right_idx-  left_idx +1
            max_width = max(max_width,level_width)
        return max_width



        