# ---- CODE IS UNDER NOTES ----
#? ------------------------------------------------------------------------------------------------------------------------------------
#? Notes START
#? ------------------------------------------------------------------------------------------------------------------------------------

# AVL trees are BST's with the smallest height possible. They are height balanced BST's.

# Through rotations they improve the worst case runtime of BST's (linear time), to logarithmic a runtime.
# Rotations are always done on 3 nodes, regardless of position in tree

#! Balance Factor
# Each node has a balance facotor => height_of_left_subtree - height_of_right_subtree
#                                 => balance_factor should be either -1, 0, 1
#                                    => if the subtree has any other number, it is not balanced and must have rotations applied to it.
#                                       To determine where subtree is balanced, use the formula: 
#                                           => if |height_of_left_subtree - height_of_right_subtree| <= 1, subtree is balanced
#                                         

#! Types of rotations:
#? --------------------------------------------------------
#? Left-Left-imbalance. (one step rotation)
#? --------------------------------------------------------
#       => perform right rotation on imbalanced node

#                                            * rotation 1 (30 ->)*
#
#             30 (BF: 2)                       20 (BF: 0)
#           /                               /              \
#        20 (BF: 1)         ----->       10 (BF:0)          30 (BF: 0)
#      /       
#   10 (BF: 0)                                 

#? --------------------------------------------------------
#? Left-Right-imbalance. (two step rotation)
#? --------------------------------------------------------
#       => perform right rotation on imbalanced node

#                                            * rotation 1 (10 <-) *             * rotation 2 (30 ->) *                                 

#             30 (BF: 2)                       30 (BF: 2)                              20 (BF: 0)
#           /                                /                                      /              \
#        10 (BF: 1)         ----->         20 (BF: 1)           ----->        10 (BF:0)             30: (BF: 0)
#           \                             /
#             20 (BF: 0)                10 (BF: 0)

# Note: programmatically you can do this in one step, there doesn't need to be a seperate function for each rotation
# To shortcut this, when performing LR rotation (using the above example), replace 30 with 20 and put 30 as 20's new right child
# same applies for RL rotation, only 30 would be 20's new left child

# For the special case, (like below) where nodes have multiple subtrees, the left branch of 20 would become 10's new right node, and the right
# branch of 20 would become 30's new left child

#? --------------------------------------------------------
#? Right-Right-imbalance. (one step rotation)
#? --------------------------------------------------------
#       => perform right rotation on imbalanced node

#                                                           * rotation 1 (30 <-) *
#
#             30 (BF: -2)                                          20 (BF: 0)
#                  \                                           /              \
#                   20 (BF: -1)               ----->       30 (BF:0)           10 (BF: 0)
#                      \       
#                       10 (BF: 0)                                 

#? --------------------------------------------------------
#? Right-Left-imbalance. (two step rotation)
#? --------------------------------------------------------
#       => perform right rotation on imbalanced node

#                                            * rotation 1 (10 ->) *             * rotation 2 (30 <-) *                                 

#             30 (BF: -2)                      30 (BF: -2)                                  20 (BF: 0)
#               \                                \                                      /              \
#               10 (BF: 1)         ----->         20 (BF: -1)           ----->        30 (BF:0)          10: (BF: 0)
#               /                                   \
#             20 (BF: 0)                            10 (BF: 0)



#? --------------------------------------------------------
#? Special case LL or RR.
#? --------------------------------------------------------
# In this case where a LL rotation must be applied, b1 would become A's new left branch

#                             A                                              B
#                           /   \                                       /         \
#                         B       a1...                               C             A
#                       /   \                       ---->            /  \         /   \
#                     C       b1...                               c1..  c2..    b1..   a1..
#                  /     \
#              c1...       c2...


#? --------------------------------------------------------
#? General
#? --------------------------------------------------------
# If multiple nodes have become inbalanced, pick the first ancestor that is imbalanced from the leaf up. That will balance older ancestors.

# Don't allow any node to exceed balance factor of -2 or 2. Perform rotation as soon as node is imbalanced, i.e. DON'T insert all the nodes, then balance.

# If you encounter a RLLR situation, only perform the first 2 (i.e. RL) from the imbalanced node



#? ------------------------------------------------------------------------------------------------------------------------------------
#? Notes START
#? ------------------------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class AVL:
    def __init__(self):
        self.root = None

    def add(self, number):        
        self.root = self.addHelper(self.root, number)

    def addHelper(self, root, number):
        if root == None:            
            return Node(number)
        
        if number < root.val:
            root.left = self.addHelper(root.left, number)
        
        elif number >= root.val:
            root.right = self.addHelper(root.right, number)
        
        return root            

    def inorder(self):
        self.inorderHelper(self.root)
    
    def inorderHelper(self, root):
        if root == None:
            return
        
        self.inorderHelper(root.left)
        print(root.val)
        self.inorderHelper(root.right)    

avl = AVL()
avl.add(10)
# left branch
avl.add(5)
avl.add(2)
avl.add(1)
avl.add(5)
# right branch
avl.add(15)
avl.add(13)
avl.add(12)
avl.add(14)
avl.add(22)
# ----------------
avl.inorder()
avl.delete(10)
avl.inorder()