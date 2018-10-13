# 我的代码
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums) == 0:
            return i
        else:
            for j in range(1, len(nums)):
                if nums[j] != nums[i]:
                    i += 1
                    nums[i] = nums[j]

        return i+1

# 同时间的其他代码
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            n = 0
            for index in range(len(nums)):
                if nums[index] != nums[n]:
                    n += 1
                    nums[n] = nums[index]
            n += 1
            return n
        else:
            return 0

# 以下代码等级渐高
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        if l==0 or l==1:
            return l
        temp = 0
        for i in range(1,l):
            if nums[i]!=nums[temp]:
                temp+=1
                nums[temp]=nums[i]
            else:
                continue
        return temp+1

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        i = 0
        for j in range(len(nums)-1):
            if nums[j] != nums[j+1]:
                nums[i+1] = nums[j+1]
                i += 1

        return i+1

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 :
            return 0
        leng = 1
        pre = nums[0]
        for value in nums:
            if value != pre :
                pre = value
                nums[leng] = value
                leng += 1
        return leng

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        l=1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[l]=nums[i+1]
                l+=1
        return l

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l<=1:
            return l
        index = 0
        for i in range(0,l-1):
            if nums[i]!=nums[i+1]:
                nums[index+1]=nums[i+1]
                index+=1
        return index+1