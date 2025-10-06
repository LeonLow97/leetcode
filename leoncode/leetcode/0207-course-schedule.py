# 207 - https://leetcode.com/problems/course-schedule/

# Time: O(V + E)
# Space: O(V + E)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for course in range(numCourses):
            adjList[course] = []
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visited = set()
        processed = set()

        def dfs(course):
            if course in visited:
                return False
            if course in processed:
                return True

            visited.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            processed.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
