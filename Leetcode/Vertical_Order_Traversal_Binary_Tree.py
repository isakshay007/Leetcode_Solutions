from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    def VerticalTraversal(self, root):
        if not root:
            return []
    
        column_table = defaultdict(list)
        queue = deque([(root,0)])

        while queue:
            node, hd = queue.popleft()
            column_table[hd].append(node.val)

            if node.left:
                queue.append((node.left,hd-1))
            if node.right:
                queue.append((node.right,hd+1))

        return [column_table[x] for x in sorted(column_table)]
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))
sol = Solution()
result = sol.VerticalTraversal(root)
print(result)