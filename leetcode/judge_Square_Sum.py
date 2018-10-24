from math import sqrt, ceil
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        mark = False
        if c == 0:
            mark = True
        for a in range(int(ceil(sqrt(c)))):
            if ceil(sqrt(c-a*a)) == sqrt(c-a*a):
                mark = True
        return mark


# 总提交等级太多，排名战胜41.47%