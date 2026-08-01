# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        ans1 = []
        def dfs(root):
            if not root:
                ans1.append("Null")
                return 
            
            ans1.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(p)

      

        ans2 = []
        def dfs(root):
            if not root:
                ans2.append("Null")
                return
            
            ans2.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(q)
        
      
        return ans1 == ans2
        
        