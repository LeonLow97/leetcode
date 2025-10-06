# 621 - https://leetcode.com/problems/task-scheduler/

# Time: O(n log n)
# Space: O(n)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for task in tasks:
            hashmap[task] = 1 + hashmap.get(task, 0)
        maxHeap = [-count for count in hashmap.values()]
        heapq.heapify(maxHeap)

        q = deque() # stores [idleTime, count]
        time = 0

        # maxHeap stores the tasks that are currently available
        # q stores the tasks that are currently idling
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                if count + 1 < 0:
                    idleTime = time + n
                    q.append([idleTime, count+1])
            if q and q[0][0] == time:
                idleTime, count = q.popleft()
                heapq.heappush(maxHeap, count)

        return time
