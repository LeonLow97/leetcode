# 684 - https://leetcode.com/problems/redundant-connection/

# Time: O(N) - we visit each node once during DFS and we loop through edges once
# Space: O(N) - adjacency list, visited set, cycle set

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 1. Prepare adjacency list to store edges in an undirected graph
        adjList = {}
        for n1, n2 in edges:
            if n1 not in adjList:
                adjList[n1] = []
            if n2 not in adjList:
                adjList[n2] = []
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        # 2. Perform recursive DFS to find all the edges that are in a cycle and return cycle set
        visited, cycle = set(), set()
        cycleStart = -1
        def dfs(node, parentNode):
            nonlocal cycleStart
            # base case
            if node in visited:
                cycleStart = node
                return True
            visited.add(node)

            # Perform DFS on the node's neighbors/child
            for child in adjList[node]:
                if child == parentNode:
                    continue
                # A cycle is found
                if dfs(child, node):
                    # Check if cycle start is found
                    if cycleStart != -1:
                        cycle.add(node)
                    # Check if current node is the cycle start
                    if cycleStart == node:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        # 3. Perform a for loop over edges, check if both nodes belong in the cycle set, return nodes if it is in cycle
        for i in range(len(edges) - 1, -1, -1):
            n1, n2 = edges[i]
            if n1 in cycle and n2 in cycle:
                return [n1, n2]
        return []