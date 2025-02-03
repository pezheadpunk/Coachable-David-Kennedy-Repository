'''236. Lowest Common Ancestor of a Binary Tree'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''Soution Class'''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Uses recursion to do a Depth First Search of the binary tree and if the
        root passed in is None or is one of the TreeNodes passed in, we return
        the root whether it is None or the p or q TreeNode becaus then we use 
        that result later on when determining what to return as the lowest
        common ancestot. If both left and right are not None then the current
        TreeNode is the common ancestor and we return it. If there only one of
        left and right is not None, then we return the one that is not None.
        Runtime: O(n) -> traversing the binary tree
        Space: O(1) -> No extra space is used
        '''
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
