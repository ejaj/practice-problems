from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while True:
            if val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left

    def insertIntoBSTRecursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBSTRecursive(root.right, val)
        else:
            root.left = self.insertIntoBSTRecursive(root.left, val)
        return root
    
 