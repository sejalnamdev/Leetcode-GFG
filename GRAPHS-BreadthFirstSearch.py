from collections import deque
class sol:
    def bfs(self, adj):
        n = len(adj)
        vis = [False]*n
        res = []

        q = deque()
        q.append(0)
        vis[0] = True

        while q:
            node = q.popleft()
            res.append(node)

            for neigh in adj[node]:
                if not vis[neigh]:
                    q.append(neigh)
                    vis[neigh] = True

        return res


