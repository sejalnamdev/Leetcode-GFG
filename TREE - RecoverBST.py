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
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        galat1first = None
        galat1second = None
        galat2first = None
        galat2second = None
        prev = None

        galat = 0

        def inorder(root):
            nonlocal prev,galat1first,galat2first,galat1second,galat2second,galat
            if root is None:
                return
            
            inorder(root.left)

            if prev is not None and prev.val > root.val:
                if galat == 0:
                    galat1first = prev
                    galat1second = root
                    galat += 1

                else:
                    galat2first = prev
                    galat2second = root
                    galat += 1

            prev = root

            inorder(root.right)

        inorder(root)

        if galat == 1:
            galat1first.val, galat1second.val = galat1second.val, galat1first.val

        else:
            galat1first.val, galat2second.val = galat2second.val, galat1first.val

        
a = list(map(int,input().split()))
root = buildtree(a)
s = Solution()
s.recoverTree(root)