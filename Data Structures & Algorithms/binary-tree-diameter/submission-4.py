class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0  # 1. This is the variable name we must use
        
        def dfs(node):
            nonlocal max_dia  # 2. Crucial fix: allows dfs to modify the outer variable
            
            if not node:
                return 0
                
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            dia = left_height + right_height
            
            if dia > max_dia:  # 3. Changed from max_height to max_dia
                max_dia = dia  # 4. Changed from max_height to max_dia
                
            return max(left_height + 1, right_height + 1)
            
        dfs(root)
        return max_dia
