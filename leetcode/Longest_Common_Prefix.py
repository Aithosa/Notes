class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]


# 这是我想到但是没能实现的方法，关键在于zip(*strs)
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=''
        if len(strs) == 0:
            return ''
        for item in zip(*strs):
            if len(set(item))==1:
                result += item[0]
            else:
                return result
        return result