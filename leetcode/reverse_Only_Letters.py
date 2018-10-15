class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        lists=[]
        s = list(S)
        for ele in S:
            if ele.isalpha():
                lists.append(ele)
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = lists.pop()
        return ''.join(s)


# 同等级
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        import string
        sList = list(S)
        letterList = [i for i in sList if i in string.ascii_letters]
        letterList = letterList[::-1]
        resList = []
        num = 0
        for s in S:
            if s not in string.ascii_letters:
                resList.append(s)
            elif s in letterList:
                resList.append(letterList[num])
                num += 1
            else:
                return ""

        return "".join(resList)

# 依次高等级
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        import string
        char = string.ascii_letters
        
        sList = list(S)
        letterList = [i for i in sList if i in char]
        letterList = letterList[::-1]
        resList = []
        num = 0
        
        for s in S:
            if s not in char:
                resList.append(s)
            elif s in letterList:
                resList.append(letterList[num])
                num += 1
            else:
                return ""

        return "".join(resList)


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        s_array = [S[i] for i in range(len(S))]
        i = 0
        j = len(S) - 1
        while i <= j:
            if not s_array[i].isalpha():
                i += 1
                continue
            elif not s_array[j].isalpha():
                j -= 1
                continue
            else:
                s_array[i], s_array[j] = s_array[j], s_array[i]
                i += 1
                j -= 1
        
        return ''.join(s_array)