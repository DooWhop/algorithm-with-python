'''
二叉树是每个节点最多有两个子树的树结构，子树有左右之分，二叉树常被用于实现二叉查找树和二叉堆。

二叉树的第i层至多有 2^{i-1}个结点；深度为k的二叉树至多有 2^k-1个结点；对任何一棵二叉树T，如果其终端结点数为 n_0, 度为2的结点数为 n_2,则 n_0=n_2+1。
因为度为1的节点对度为0的节点数目不会有影响，而每增加一个度为2的节点总的来说则会相应增加一个度为0的节点。

一棵深度为 k, 且有 2^k-1个节点称之为满二叉树；深度为 k，有 n个节点的二叉树，当且仅当其每一个节点都与深度为 k的满二叉树中序号为 1至 n的节点对应时，称之为完全二叉树。完全二叉树中重在节点标号对应。

二叉查找树(BST)是一颗二叉树，其中每个节点都含有一个可进行比较的键及相应的值，且每个节点的键都大于等于左子树中的任意节点的键，而小于右子树中的任意节点的键。
使用中序遍历可得到有序数组，这是二叉查找树的又一个重要特征。
二叉查找树使用的每个节点含有两个链接，它是将链表插入的灵活性和有序数组查找的高效性结合起来的高效符号表实现。
'''

class TreeNode():

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


'''
    按照访问根元素(当前元素)的前后顺序，遍历方式可划分为如下几种：
        深度优先：先访问子节点，再访问父节点，最后访问第二个子节点。根据根节点相对于左右子节点的访问先后顺序又可细分为以下三种方式。
            前序(pre-order)：先根后左再右
            中序(in-order)：先左后根再右
            后序(post-order)：先左后右再根
        广度优先：先访问根节点，沿着树的宽度遍历子节点，直到所有节点均被访问为止。
'''
class Traversal(object):
    def __init__(self):
        self.traverse_path = list()

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)
    
        
if __name__ == '__main__':
    pass               