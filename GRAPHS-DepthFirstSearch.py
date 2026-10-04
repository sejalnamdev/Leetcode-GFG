class sol:
    

    def dfs(self, adj):
        n = len(adj)
        res = []
        vis = [False]*n

        def solve(node):
            res.append(node)
            vis[node] = True

            for neigh in adj[node]:
                if not vis[neigh]:
                    solve(neigh)

        solve(0)

        return res

obj = sol()

n = int(input())
adj = []
for i in range(n):
    neighbours = list(map(int, input().split()))
    adj.append(neighbours)

print(adj)

print(obj.dfs(adj))

                

        