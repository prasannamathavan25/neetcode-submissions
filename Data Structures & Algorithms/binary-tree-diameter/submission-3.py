class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(curr):

            nonlocal ans                      # FIX: Allows updating ans from the outer function.

            if not curr:
                return 0

            l_height = dfs(curr.left)
            r_height = dfs(curr.right)

            ans = max(ans, l_height + r_height)   # FIX: Diameter = left height + right height.

            cur_height = 1 + max(l_height, r_height)

            return cur_height                     # FIX: Reuse the computed height.

        dfs(root)

        return ans                                # FIX: Return the computed diameter.