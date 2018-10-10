from math import floor
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            test = list(str(x))
            for i in range(floor(len(test)/2)):
                if test.pop(0) == test.pop():
                    pass
                else:
                    return False
            if len(test) in [0, 1]:
                return True

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x==int(str(x)[::-1]):
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return True if str(x) == str(x)[::-1] else False