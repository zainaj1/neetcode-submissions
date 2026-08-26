# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        right_view = []

        if root:
            queue.append(root)
        
        while queue:
            layer_nodes = []
            for i in range(len(queue)):
                curr = queue.popleft()
                layer_nodes.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                

            right_view.append(layer_nodes[-1])

        return right_view
        