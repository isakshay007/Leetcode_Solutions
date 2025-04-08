class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def gets_path(self, root, arr, x):
        if not root:
            return False

        arr.append(root.val)

        if root.val == x:
            return True

        if self.gets_path(root.left, arr, x) or self.gets_path(root.right, arr, x):
            return True
        arr.pop()
        return False

    def solve(self, A, B):
        arr=[]
        if not A:
            return arr

        self.gets_path(A,arr,B)

        return arr

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

sol = Solution()

target_leaf_value = 7

path = sol.solve(root, target_leaf_value)

print(f"Path from root to leaf with value {target_leaf_value}: ", end="")
print(path)