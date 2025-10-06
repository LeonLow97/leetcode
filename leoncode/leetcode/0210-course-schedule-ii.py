# 210 - https://leetcode.com/problems/course-schedule-ii/

# Time: O(V + E) where V is the number of courses and E is the number of prerequisites
# Space: O(V + E) for the adjacency list, O(V) for the recursion

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        for course in range(numCourses):
            adjList[course] = []
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visited, processed = set(), set()
        res = []

        def dfs(course):
            if course in processed:
                return True
            if course in visited:
                return False # cycle

            visited.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            processed.add(course)
            res.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res