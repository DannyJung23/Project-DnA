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
