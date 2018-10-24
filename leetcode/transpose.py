class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = [[0 for i in range(len(A))] for i in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                B[j][i] = A[i][j]
        return B


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [list(a) for a in zip(*A)]


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(list, zip(*A)))


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(A), len(A[0])
        res = [[0] * rows for _ in range(cols)] # 由于不能引入numpy库，因此需要这样写
        for row in range(rows):
            for col in range(cols):
                res[col][row] = A[row][col]
        return res


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A[:] = map(list,zip(*A))
        return A