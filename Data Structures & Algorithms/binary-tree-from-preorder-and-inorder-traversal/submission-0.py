# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
What im thinking is that preorder traversal prints everything (fills in the gap) that is shown by inorder traversal
Inorder traversal will only pring the node once we are at the end of the tree (leaf), preorder traversal prints all the nodes we took to get to that point.

I.e in our example the leaf node is 2, dfs will start at 1 and then go to 2, inorder will print 2 then 1, while pre order will print 1 then 2. 

This is usefull because inorder will give us the lowest most node and we wont know what comes between that and the root, so we need to use preorder to identify that information.

Pick a node in p
everything in i that is to the left of p's value in i will be on the left tree and everything to the right will be in the right tree, this crease our sub problems i.e
i: [1, 2, 3, 4, 5, 6, 7]
p: [5, 3, 2, 1, 4, 7, 6]

so we start at p[0] which is 5, which in i is i[4]. we call our recursive function 
    * (5).left = (i: [1, 2, 3, 4], p:[3, 2, 1, 4]) -> (3)
    * (5).right = (i: [6, 7], p:[7, 6]) -> (7)

    in the left case we then pick and return 3, but we do a recursive call so 
    (3).left = (i: [1, 2], p[2, 1]) -> (2)
    (3).right = (i: [4], p[4]) -> (4)

    in the left case we then do 2 
    (2).left = (i: [1], p: [1]) -> (1)
    (2).right = (i: [], p: []) -> None
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not (preorder and inorder):
            return None

        root = TreeNode(preorder[0])
        i = inorder.index(root.val) # 4
        p = i + 1 # 5

        root.left = self.buildTree(preorder[1:p], inorder[0:i]) 
        root.right = self.buildTree(preorder[p::], inorder[i+1::]) 
        
        return root
    


        