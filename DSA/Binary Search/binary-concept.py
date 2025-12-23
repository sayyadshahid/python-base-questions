# Binary tree terminology =============================================================
# A node stores a value plus references to its left child and right child; missing children are stored as null (none).​

# The root node is the topmost node of the tree, and every node acts as the root of its own subtree.​

# Leaf nodes are nodes with no left child and no right child; both references are null.​

# Complete and perfect binary trees ===================================================
# A complete binary tree has every level completely filled, except possibly the last level, which is filled from left to right.​

# A perfect binary tree has all levels fully filled, so the node counts per level follow powers of two (one, two, four and so on).​

# The height (also called maximum depth) of a tree is the number of nodes on the longest path from the root node down to a leaf node.​

# Array representation of a binary tree ===================================================
# A binary tree can be stored in an array by placing the root node at index one, its left child at index two times index, and its right child at index two times index plus one.​

# If the computed index is outside the array or explicitly marked as a special value like negative one, that position represents a null child.​

# Depth first search traversals ==============================================================
# Depth first search means going as far down a branch as possible before backtracking to explore other branches.​

# Preorder traversal (depth first search preorder) processes node, then left subtree, then right subtree, giving sequence one, two, four, five, three, ten for the example tree.​

# Inorder traversal (depth first search inorder) processes left subtree, then node, then right subtree, giving sequence four, two, five, one, ten, three in the example.​

# Postorder traversal (depth first search postorder) processes left subtree, then right subtree, then node, giving sequence four, five, two, ten, three, one.​

# Breadth first search traversal =====================================================================
# Breadth first search visits nodes level by level, which in trees is called level order traversal.​

# Level order traversal of the example tree visits one, then two and three, then four, five and ten, in that order.​

# Implementing traversals ==========================================================================
# Recursive traversals use the program call stack: each call stores the current node while calling left child and right child functions.​

# Iterative depth first search uses an explicit stack data structure: push the root node, pop a node to process it, then push right child and push left child so that the left side is processed first.​

# Iterative breadth first search uses a queue data structure: enqueue the root node, then repeatedly dequeue a node, process it, enqueue its left child and enqueue its right child.​

# Time and space complexity =======================================================================
# Searching for a value in a general binary tree takes order of n time, where n is the number of nodes, because each node may need to be visited.​

# Recursive depth first search uses order of height space on the call stack; in the worst skewed case height equals n, giving order of n space.​

# Breadth first search can store about half of the tree nodes at the last level in the queue, which also leads to order of n space in the worst case.​

# Binary search trees ================================================================================
# A binary search tree is a binary tree where for every node, all values in the left subtree are smaller and all values in the right subtree are larger, and this rule holds recursively.​

# Searching in a height balanced binary search tree takes order of logarithm of n time because each step discards about half of the remaining search space.​

# In a very unbalanced binary search tree that looks like a linked list, search time can degrade to order of n, because almost all nodes may be checked.​

# Inorder traversal and sorting in binary search trees  ==========================================
# In a binary search tree, inorder traversal visits nodes in nondecreasing sorted order of their values.​

# The video example shows node values negative one, one, three, five, seven, eight, nine being printed in sorted order by inorder traversal of a binary search tree.​

# TreeNode class and functions (Python idea) ========================================
# The TreeNode class has a value, a left child reference and a right child reference, each defaulting to none in the constructor.​

# A special string method is implemented so that printing a TreeNode object prints its stored value.​

# Recursive preorder function: if node is null return, otherwise print node value, then call preorder on left child, then call preorder on right child.​

# Recursive inorder function: if node is null return, otherwise call inorder on left child, then print node value, then call inorder on right child.​

# Iterative preorder function: create a stack with the root node, while stack not empty pop a node, print it, push right child if not null, then push left child if not null.​