# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        target = subRoot.val

        ans1 = []

        def dfs_find(root):
            if not root :
                return 
            if root.val == target:
                ans1.append(root)
            dfs_find(root.left)
            dfs_find(root.right)
        dfs_find(root)
    
        
        def dfs(root):
            if not root:
                ans.append("none")
                return 
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
            return ans

        ans = []
        target_ans = dfs(subRoot)
        

        for r in ans1:
            ans = []
            ans = dfs(r)
            if target_ans == ans:
                return True
        
        return False


        

        
        