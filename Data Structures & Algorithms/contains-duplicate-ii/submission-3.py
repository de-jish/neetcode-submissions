class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_ind = {}

        for i, val in enumerate(nums):
            if val not in num_to_ind:
                num_to_ind[val] = i
            else:
                if i - num_to_ind.get(val, 0) <= k:
                    return True
                num_to_ind[val] = i
            
        return False