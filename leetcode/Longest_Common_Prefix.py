class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        strs.sort()
        # 排序之后第一个和最后一个就是差异最大的一对
        first = strs[0]
        last = strs[-1]
        
        i = 0
        # 可以用个最小值
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


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        cstr = ""
        idx = 0
        end = 0
        is_break = False
        while True:
            if len(strs[0]) > idx:
                cstr = strs[0][idx]
            else:
                break
            for i in range(1,len(strs)):
                if strs[i] == "":
                    is_break =True
                    break
                elif idx < len(strs[i]) and cstr == strs[i][idx]:
                    continue
                else:
                    is_break = True
                    break
            if is_break:
                break
            idx += 1
            end = idx
        return strs[0][:end]

class Solution:
    def longestCommonPrefix(self, strs):
        l=min([len(t) for t in strs],default=0)
        if l==0:
            return ""
        if len(strs)==1:
            return strs[0]
        init=strs[0]
        for i in range(l):
            for s in strs[1:]:
                if s[i]!=init[i]:
                    return init[:i]
        return init[:l]