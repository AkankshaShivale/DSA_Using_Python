def dfs(node, adj, visited):
    visited[node] = 1
    print(node)
    for i in range(len(adj[node])):
        if adj[node][i] == 1 and visited[i]==0:
            dfs(i,adj,visited)

if __name__ == '__main__':
    adj = []
    visited = []
    n = int(input("Please enter how nodes are there in your graph: "))
    for i in range(n):
        adj.append(list())
        for j in range(n):
            ch = int(input(f"Is {i} and {j} are nieghbours? [ yes(1)/ no(0) ]: "))
            adj[i].append(ch)
        visited.append(0)
    
    start = 0
    dfs(start,adj,visited)
    



