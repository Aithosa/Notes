# nums = [3,2,4]
# target = 6
# for i in range(len(nums)):
#   if nums[i] >= target/2:
#       mid_index = i
#       break
# print([(nums[low], nums[high]) for low in range(mid_index) for high in range(mid_index, len(nums)) if nums[low]+nums[high] == target])


# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         nums_sort = sorted(nums)
#         for i in range(len(nums)):
#             if nums_sort[i] >= target/2:
#                 mid_index = i
#                 break
#         # return [(low, high) for low in range(mid_index) for high in range(mid_index, len(nums)) if nums[low]+nums[high] == target]
#         ans = []
#         for low in range(mid_index): 
#             for high in range(mid_index, len(nums)):
#                 if nums_sort[low]+nums_sort[high] == target:
#                     ans.extend([nums_sort[low], nums_sort[high]])

#         return [nums.index(nums_sort[low]), nums.index(nums_sort[low])]


# nums = [3,3]
# target = 6

# print('start...')

# nums_sort = sorted(nums)
# for i in range(len(nums)):
#     if nums_sort[i] >= target/2:
#         mid_index = i
#         break
# ans = []

# print('begin go into first two for loop')
# print(mid_index, len(nums))

# for low in range(mid_index): 
#     print("low")
#     for high in range(mid_index, len(nums)):
#         print('into first two for loop')
#         if (mid_index != len(nums)-1 and nums_sort[low] + nums_sort[high] == target):
#             ans = [nums.index(nums_sort[low]), nums.index(nums_sort[high])]
#         elif (nums.count(nums[mid_index])==2 and nums[mid_index] == mid_index):
#             print('elif')
#             if ((nums_sort[mid_index] + nums_sort[mid_index+1]) == target):
#                 print('last if')
#                 for j in range(len(nums)):
#                     ans.append(nums.index(nums_sort[mid_index]))


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        
        for i, num in enumerate(nums):
            print([i, num])
            if target-num in num_to_index:
                return [i, num_to_index[target - num]]
            num_to_index[num] = i
            
        return []



nums = [3,2,4]
target = 6

num_to_index = {}

for i, num in enumerate(nums):

    print([i, num])
    print('before', num_to_index)

    if target-num in num_to_index:
        print('ans = ', [i, num_to_index[target - num]])
    num_to_index[num] = i
    
    print('after', num_to_index, '\n')
    
print([])