class Tree():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root):  # 前序遍历
    st = [(root, 0)]
    while st:
        root, task = st.pop()
        if task:  # 0为遍历 1为输出
            print(root.val)
        else:  # 改变顺序可得到前序 中序 后续遍历
            if not root.right:
                st.append([root.right, 0])
            if not root.left:
                st.append([root.left, 0])
            st.append([root, 1])


def preOrder(root):
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)


def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)


def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)


def levels(root):
    que = [root]
    while que:
        node = que.pop(0)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)

# 前序+中序 重建树
def rebuiltTree(pre, in_):
    if len(pre) == 0:
        return
    if len(pre) == 1:
        return Tree(pre)
    root = Tree(pre[0])
    idx = in_.index(pre[0])
    Tree.left = rebuiltTree(pre[1:idx], in_[:idx])
    Tree.right = rebuiltTree(pre[idx+1:], in_[idx+1:])
    return root


# 由前序和后序 推出有多少中序
# 只有一棵树只有一个孩子时中序有两种情况
def count_inOrder(pre, post):
    ans = 1
    for i in range(len(pre)-1):
        for j in range(len(post)):
            if pre[i] == post[j] and pre[i+1] == post[j-1]:
                ans *= 2
    return ans


# 二叉树的深度 递归
def treeDepth(root):
    if not root:return -1
    ld = treeDepth(root.left)
    rd = treeDepth(root.right)
    return max(ld,rd)+1

# 二叉树的深度 bfs
from collections import deque
def treeDpthBFS(root):
    if not root:return -1
    que = deque([root])
    ans = -1 # 根据条件初始化
    while que:
        size = len(que)
        for i in range(que):
            root = que.popleft()
            if not root.left:
                que.append(root.left)
            if not root.right:
                que.append(root.right)
        ans+=1
    return ans

# 二叉树的叶子结点数
def count(root):
    if not root:return -1
    if not root.left and root.right:
        return 1
    return count(root.left)+count(root.right)