class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])

# 同时间
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        else:
            a = s.split(' ')
            return len(a[-1]) if s[-1] != ' ' else self.lengthOfLastWord(s[:-1])


# 依次快
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = s.strip().split(" ")
        if len(ls)>0:
            return len(ls[-1])
        else:
            return 0


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(' ')
        i = -1
        while words[i] == '' and -i < len(words):
            i -= 1
        return len(words[i])



class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0:
            if s[i] == " ":
                break
            length += 1
            i -= 1
        return length


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        if len(s)<1:
        	result=0
        elif not s.strip():
            result=0
        else:
        	l=[]
        	l=s.split()
        	l.reverse()
        	result=len(l[0])

        return result