# 我的，无法全通过
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        lists = []
        s = ''
        for ele in S:
            if ele.isalnum():
                lists.append(ele.upper())
        for _ in lists:
            count = K
            while(count > 0):
                s += lists.pop()
                count -= 1
                if count == 0:
                    s += '-'
        if s[-1] == '-':
            s = s[:len(s)-1]
        return s[::-1]

# 找到的答案
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        formatted = []
        key = S.replace('-', '').upper()
        
        i = len(key) - K
        
        while(i>=0):
            formatted.append(key[i:i+K])
            i -= K
            
        if i != -K:
            formatted.append(key[:i+K])
        return '-'.join(formatted[::-1])

# 同等级
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        a_s = ''.join(S.upper().split('-'))
        length = len(a_s)
        r = []
        first = length % K if length %K != 0 else K
        r.append(a_s[:first])
        for i in range(first, length, K):
            r.append(a_s[i:i+K])
        return '-'.join(r)


# 依次快
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S=S.replace('-','').upper()
        if len(S)%K:
            S='#'*(K-len(S)%K)+S
        return '-'.join(S[x:x+K] for x in range(0,len(S),K)).replace('#','')


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        a_s = ''.join(S.upper().split('-'))
        length = len(a_s)
        r = []
        first = length % K if length %K != 0 else K
        r.append(a_s[:first])
        for i in range(first, length, K):
            r.append(a_s[i:i+K])
        return '-'.join(r)