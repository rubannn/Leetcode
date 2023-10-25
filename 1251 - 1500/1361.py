class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        nodes = (set(leftChild + rightChild) - set([-1])) ^ set(range(n))
        if len(nodes) != 1:
            return False

        visited = nodes.copy()
        while nodes:
            next_nodes = []
            for node in nodes:
                if leftChild[node] in visited or rightChild[node] in visited:
                    return False

                if leftChild[node] != -1:
                    visited.add(leftChild[node])
                    next_nodes.append(leftChild[node])

                if rightChild[node] != -1:
                    visited.add(rightChild[node])
                    next_nodes.append(rightChild[node])

            nodes = next_nodes
        return len(visited) == n
