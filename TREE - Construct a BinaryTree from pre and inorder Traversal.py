from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildtree(a):
    if a is None or a[0] == -1:
        return None

    root = TreeNode(a[0])
    q = deque([root])
    i = 1

    while q and i < len(a):
        node = q.popleft()

        if a[i] != -1:
            node.left = TreeNode(a[i])
            q.append(node.left)

        i += 1

        if i < len(a) and a[i] != -1:
            node.right = TreeNode(a[i])
            q.append(node.right)

        i += 1

    return root





class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : index + 1], inorder[ : index])

        root.right = self.buildTree(preorder[index + 1 : ], inorder[index + 1 : ])


        return root

def printtree(root):
    q = deque([root])
    ans = []

    while q:
        node = q.popleft()

        if node is None:
            ans.append(-1)
            continue

        ans.append(node.val)

        q.append(node.left)
        q.append(node.right)

    # Remove extra -1s at the end
    while ans and ans[-1] == -1:
        ans.pop()

    print(*ans)

preorder = list(map(int,input().split()))
inorder = list(map(int,input().split()))
solution = Solution()
root = solution.buildTree(preorder, inorder)
printtree(root) # Print the tree in level-order traversal to verify the tree construction