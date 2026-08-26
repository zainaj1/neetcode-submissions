class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for src, des in prerequisites:
            if src not in graph:
                graph[src] = []
            elif des not in graph:
                graph[des] = []
            graph[src].append(des)     
        
        for course in range(numCourses):
            visited = set()
            if not self.dfs(course, graph, visited):
                return False
        return True
    
    def dfs(self, target, graph, visited) -> bool:
        
        if not target in graph or graph[target] == []:
            return True
        elif target in visited:
            return False
        
        canTake = True
        visited.add(target)
        for req in graph[target]:
            canTake = canTake and self.dfs(req, graph, visited)
        
        visited.remove(target)
        return canTake


        


        