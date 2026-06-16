class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, val in enumerate(nums):
            diff = target - val

            if diff in num_to_index:
                return [num_to_index[diff], i]

            num_to_index[val] = i

        
