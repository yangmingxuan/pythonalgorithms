"""
    Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

    Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.
    Follow up: Can you solve it with time complexity O(height of tree)?



    Example 1:
            5                     5
           / \                   / \
          3   6     ===>        4   6
         / \   \               /     \
        2   4   7             2       7

    Input: root = [5,3,6,2,4,null,7], key = 3
    Output: [5,4,6,2,null,null,7]
    Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
    One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
    Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

    Example 2:

    Input: root = [5,3,6,2,4,null,7], key = 0
    Output: [5,3,6,2,4,null,7]
    Explanation: The tree does not contain a node with value = 0.
    Example 3:

    Input: root = [], key = 0
    Output: []


    Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -105 <= Node.val <= 105
    Each node has a unique value.
    root is a valid binary search tree.
    -105 <= key <= 105

"""
from btree import TreeNode


class DeleteNodeinaBST:
    """
     * 1. BST特征 left < parent < right, 用inorder方式遍历[2,3,4,5,6,7]为一个递增的数列
     * 2. 要删除一个结点，如果这个结点是叶结点，直接删除，而如果为其它的情况，则取它前一个数(left不为空)或后一个数(right不为空)为其结点的值
     * 3. BST一个结点的前一个数为其左子树(若有)的最大值，而后一个数为其右子树(若有)的最小值
     * 1. BST's feature is left < parent < right, its inorder traversal is an increasing array such like [2,3,4,5,6,7]
     * 2. To delete a node, if this node is a leaf node, delete it directly; and in other case, take the previous number(left is not null)
     *    or the next number(right is not null) as its node value
     * 3. In BST, a node's previous number is the maximum of its left subtree(if not null), its next number is the minimum of its right subtree(if not null)
    """
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def previousNumber(node: TreeNode) -> int:
            """
            previous number is the maximum of its left subtree(if not null), one left, other right
            :param node:
            :return:
            """
            #node and node.left is not null
            node = node.left
            while node.right:
                node = node.right
            return node.val

        def nextNumber(node: TreeNode) -> int:
            """
            next number is the minimum of its right subtree(if not null), one right, other left
            :param node:
            :return:
            """
            #node and node.right is not null
            node = node.right
            while node.left:
                node = node.left
            return node.val

        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  #key = root.val
            """
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = nextNumber(root)
                root.right = self.deleteNode(root.right, root.val)
            else: #root.left
                root.val = previousNumber(root)
                root.left = self.deleteNode(root.left, root.val)
            """
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.val = nextNumber(root)
            root.right = self.deleteNode(root.right, root.val)
        return root
