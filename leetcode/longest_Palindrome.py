from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        left = 0
        count = Counter(s)
        if len(s) <= 1010:
            for _, value in count.items():
                if value%2 == 0:
                    length += value
                elif value%2 != 0 and left <= value:
                    left = value
        
        length += left
        return length


# 最快
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        letters = set()
        for c in s:
            if c in letters:
                max_length += 2
                letters.remove(c)
            else:
                letters.add(c)
        return max_length + bool(letters)


# 同等级
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size <= 1:
            return size
        hashMap = {}
        for i in range(size):
            if s[i] in hashMap:
                hashMap[s[i]] += 1
            else:
                hashMap[s[i]] = 1
        odd = False
        res = 0
        for key in hashMap:
            if hashMap[key] % 2 == 0:
                res += hashMap[key]
            else:
                res += hashMap[key]-1
                odd = True
        if odd:
            res += 1
        return res


# 依次变慢
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        lens = 0
        ans = 0
        for d in dic:
            if dic[d] % 2:
                ans += dic[d] - 1
                lens += 1
            else:
                ans += dic[d]
        return ans if lens == 0 else ans + 1


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = odd = 0
        cnt = collections.Counter(s)
        for c in cnt:
            ans += cnt[c]
            if cnt[c] % 2 == 1:
                ans -= 1
                odd += 1
        return ans + (odd > 0)


from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        has_odd = False
        for k, v in dic.items():
            if v % 2 == 0:
                num += v
            else:
                if v > 2:
                    num += (v-1)
                has_odd = True
        if has_odd:
            num += 1
        return num