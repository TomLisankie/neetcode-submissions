from math import floor
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3 and target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1
        center_index = floor(len(nums) / 2)
        left_most = 0
        right_most = len(nums) - 1
        found = False
        while not found:
            if nums[center_index] == target:
                return center_index
            if left_most == right_most or left_most == right_most - 1:
                if nums[left_most] == target:
                    return left_most
                if nums[right_most] == target:
                    return right_most
                return -1
            if nums[center_index] > target:
                # go left
                right_most = center_index
                center_index = floor((left_most + center_index) / 2)
                continue
            if nums[center_index] < target:
                # go right
                left_most = center_index
                center_index = floor((center_index + right_most) / 2)
                continue
        return -1
