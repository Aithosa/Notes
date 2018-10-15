class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while(start <= end):
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            else:
                start += 1
        return start


# 同速度
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
        return j

# 以下依次快
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for k in range(0,len(nums)):
            if nums[k] != val:
                
                nums[i] = nums[k]
                i += 1
        return i


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for v in nums[:]:
            if val == v:
                nums.pop(nums.index(v))
        return len(nums)


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.pop(nums.index(val))
        return len(nums)

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        for e in nums:
            if e != val:
                nums[begin] = e
                begin += 1
        return begin


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)