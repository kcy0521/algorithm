### DFS 버전

n = int(input())
m = int(input())

graph = [[]for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

visited = [0] * (n+1)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
dfs(1)

print(sum(visited)-1)