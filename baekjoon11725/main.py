# DFS Stack

import sys
from collections import deque

sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

tree = [[]for i in range(N+1)]
parent = [[]for i in range(N+1)]
visited = [False]*(N+1)

for i in range(N-1):
    x, y = map(int,sys.stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)

def bfs(node):
    que = deque([node])
    visited[node] = True

    while que:
        popData = que.popleft()
        for i in tree[popData]:
            if not visited[i]:
                parent[i] = node
                que.append(i)
                visited[node] = True
bfs(1)
for i in range(2,N+1):
    print(parent[i])

# def stack(node):
#     visited[node] = True
#     stack = deque([node])
#     # print(stack)
#
#     while stack:
#         popData = stack.pop()
#         # print(popData)
#         for i in tree[popData]:
#             if not visited[i]:
#                 stack.append(i)
#                 visited[i] = True
#                 parent[i] = popData
# stack(1)

# def DFS(node):
#     visited[node] = True
#     for i in tree[node]:
#         if visited[i] == False:
#             parent[i] = node
#             DFS(i)
#
# for i in tree:
#     i.sort()
#
# DFS(1)
#
# for i in range(2,N+1):
#     print(parent[i])