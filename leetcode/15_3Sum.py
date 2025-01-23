'''15. 3Sum'''
from typing import List

class Solution:
    '''Solution Class'''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Sorts the list to make the movement of the pointers more logical.
        Then it iterates over the list with each element starting from the
        front and has two pointers, one starting on the left side of the list
        after the current element and another on the right side from the end of
        the list. When 3sums are found they are added to the result list.
        Repeats of numbers are skipped to avoid 3sums with the same values.
        runtime: O(n^2) because of the sorting (O(nlog(n))) and the iterating
        over the list with pointers O(n)
        space = O(n) - the copy of the list sorted
        '''
        result = []
        nums_sorted = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue
            cur = nums_sorted[i]
            target = cur * -1
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums_sorted[left] + nums_sorted[right]
                if cur_sum == target:
                    result.append([cur, nums_sorted[left], nums_sorted[right]])
                    while left < right and nums_sorted[left] == nums_sorted[left + 1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
