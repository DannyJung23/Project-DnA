"""
Approach:
The total number of courses is the number of nodes in the graph.
For a prerequisite [[1, 0]], (0, 1) is an edge and 0 is the predecessor of 1.
Return True if it's possible to topologically sort the graph -> check if the graph is acyclic.
Build a graph using a dict and perform recursive DFS to detect a back-arc.
"""

# 11ms solution - O(n+e)

def canFinish(self, numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    visited = [0] * numCourses  # 0 = unvisited, 1 = visited, 2 = done

    def dfs(node):
        if visited[node] == 1:
            return False  # cycle detected (back-arc)
        if visited[node] == 2:
            return True  # already done
        
        visited[node] = 1  # mark as visited in current DFS path
        for neighbour in graph[node]:
            if not dfs(neighbour):  # if any child has a cycle
                return False
        visited[node] = 2  # mark as done
        return True
    
    for i in range(numCourses):
        if visited[i] == 0:
            if not dfs(i):
                return False
    return True


"""
Approach:
Topologically sort the graph by performing BFS and Zero-Indegree Sorting using deque().
If the graph is not a DAG, the algorithm will eventually stop when it can't find a zero-indegree node.
Return True if the algorithm successfully visits all the nodes.

Algorithm:
Kahn's topological sorting (zero-indegree sorting)
"""

# 3ms solution - O(n+e)

from collections import deque

def canFinish(self, numCourses, prerequisites):
    graph = {i : [] for i in range(numCourses)}
    inDegree = {i : 0 for i in range(numCourses)}
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        inDegree[course] += 1

    sources = deque()
    
    for course in inDegree:
        if inDegree[course] == 0:
            sources.append(course)
    
    visited = 0
    while sources:
        node = sources.popleft()
        visited += 1
        for neighbour in graph[node]:
            inDegree[neighbour] -= 1
            if inDegree[neighbour] == 0:
                sources.append(neighbour)
    
    return visited == numCourses
