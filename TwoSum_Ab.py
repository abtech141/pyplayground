class Solution(object):
    def twoSum(self, nums, target):
        self.num_map = {}  

        for i, num in enumerate(nums):
            complement = target - num
            if complement in self.num_map:
                return [self.num_map[complement], i]
            self.num_map[num] = i

        return [] 
print(Solution().twoSum([1,2,3],3))