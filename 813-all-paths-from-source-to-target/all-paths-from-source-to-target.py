class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        ans = []

        def backtrack(currNode, path):
            if currNode == target:
                ans.append(list(path))
                return
            for node in graph[currNode]:
                path.append(node)
                backtrack(node, path)
                path.pop()
        path = [0]
        backtrack(0, path)
        return ans                
        