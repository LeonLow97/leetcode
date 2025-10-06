# 743 - https://leetcode.com/problems/network-delay-time/

# Time: O(E log V) where E is the number of edges and V is the number of vertices
# Space: O(E + V)   

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Prepare adjacency list
        adjList = collections.defaultdict(list)
        for u, v, w in times:
            adjList[u].append((v, w))

        # Perform BFS on all of the neighbors
        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue

            visited.add(n1)
            time = w1

            # visit all neighbors
            for n2, w2 in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return time if len(visited) == n else -1