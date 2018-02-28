from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src, dst):
        self.graph[src].append(dst)

    def BFS(self, start):
        visited = [ False ] * len(self.graph)

        output = []
        queue  = []
        queue.append(start)
        visited[start] = True
        while(queue):
            curr = queue.pop(0)
            output.append(curr)
            for i in self.graph[curr]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return output

    def __DFSUtil(self, curr, visited, output):
        output.append(curr)
        visited[curr] = True
        for i in self.graph[curr]:
            if visited[i] == False:
                self.__DFSUtil(i, visited, output)
        
    def DFS(self, start):
        visited = [ False ] * len(self.graph)
        output = []
        self.__DFSUtil(start, visited, output)
        return output
        
if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    
    nodes = graph.BFS(2)
    print("BFS Nodes: " + str(nodes))

    nodes = graph.DFS(2)
    print("DFS Nodes: " + str(nodes))