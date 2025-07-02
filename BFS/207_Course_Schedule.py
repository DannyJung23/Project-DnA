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
