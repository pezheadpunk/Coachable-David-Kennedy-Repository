'''128. Longest Consecutive Sequence'''
from typing import List

class Solution:
    '''Solution Class'''
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Makes a set of the nums list and then iterates
        through the set and if there is no previous
        sequential value, it then starts counting the
        consecutive values from that value. Then when
        the sequence is broken it checks if the current
        count is longer than the longest count so far
        and if it is set that count to the longest.
        Runtime: O(n)
        Space: O(n)
        '''
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                next_num = num + 1
                count = 1
                while next_num in nums_set:
                    next_num += 1
                    count += 1
                longest = max(longest, count)
        return longest
