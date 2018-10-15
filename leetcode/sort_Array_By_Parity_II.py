# 非常耗费时间，待改进
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd=[]
        odd_not=[]
        for ele in A:
            if ele%2 == 0:
                odd_not.append(ele)
            else:
                odd.append(ele)
        for i in range(len(A)):
            if i%2==0:
                A[i] = odd_not.pop()
            else:
                A[i] = odd.pop()
        return A