class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return sum(-1 if "-" in op else 1 for op in operations)
