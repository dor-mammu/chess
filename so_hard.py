import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
v,e,r = map(int,input().split())
two_list = [[] for _ in range(v+1)]

cnt = 0

for i in range( v + 1):
    x,y = map(int,input().split())
   
def dfs(graph, star_node):
    visited = list()
    global cnt

    visit.append(star_node)
    while visit:
        node = visit.pop()
        if node not in visited:
            visited.append(node)
    return visited
