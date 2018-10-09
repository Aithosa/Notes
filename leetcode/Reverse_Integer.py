class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        symbol = 1
        ans = 0
        pows = 0
        elements = list(str(x))
        
        if elements[0] == '-':
            symbol = -1
            elements.remove('-')

        length = len(elements)
        
        for element in elements:
            if pows <= length-1:
                ans = ans + 10**pows * int(element)
                pows = pows + 1
        ans = ans * symbol
        if (ans < -(2**31)) or (ans > 2**31 -1):
            return 0
        else:
            return ans


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)
        reversed = 0
        
        while x != 0:
            reversed = reversed * 10 + x%10
            x //= 10
            
        if reversed > 2**31 - 1:
            return 0
        return reversed if not negative else -reversed


import math

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        fix = -1
        absX = abs(x)
        if absX == x:
            fix = 1
        strX = str(absX)
        result = strX[::-1]
        #strArray = strX[i] for i in range(len(strX))
        if int(result) > 2 ** 31 - 1:
            return 0
        return int(result) * fix


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >=0:
            result = int(str(x)[::-1])
        else:
            result = int('-'+str(-x)[::-1])
        if result >= 2**31-1 or result<=-2**31:
            result = 0
        return result