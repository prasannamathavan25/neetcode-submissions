class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        target = subRoot.val
        candidates = []

        def find(node):
            if not node:
                return
            if node.val == target:
                candidates.append(node)
            find(node.left)
            find(node.right)
        find(root)


        def serialize(node):
            result = []
            def dfs(cur):
                if not cur:
                    result.append("None")
                    return
                result.append(cur.val)
                dfs(cur.left)
                dfs(cur.right)
            dfs(node)
            return result

        target_tree = serialize(subRoot)
        for node in candidates:
            if serialize(node) == target_tree:
                return True

        return False





        