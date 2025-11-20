from queue import Queue

def bfs(start,adj,Q,visited):
    visited[start] = 1
    Q.put_nowait(start)
    while not Q.empty():
        node = Q.get_nowait()
        print(f"visited node: {node}")
        for i in range(len(adj[node])):
            if adj[node][i] == 1 and visited[i] == 0:
                visited[i] = 1
                Q.put_nowait(i)

if __name__ == '__main__':
    adj = []
    visited = []
    n = int(input("Please enter how nodes are there in your graph: "))
    Q = Queue(maxsize=n)
    for i in range(n):
        adj.append(list())
        for j in range(n):
            ch = int(input(f"Is {i} and {j} are nieghbours? [ yes(1)/ no(0) ]: "))
            adj[i].append(ch)
        visited.append(0)
    
    start = 0
    bfs(start,adj,Q,visited)
                