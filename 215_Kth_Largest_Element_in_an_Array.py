'''215. Kth Largest Element in an Array'''
from typing import List
import random


class Solution:
    '''Solution Class'''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Uses quickselect algorithm to parse the list into three parts based
        on a random pivot. The seciton partioned to the left in the list 
        are values less than the pivot, in the middle are values equal to 
        the pivot, and to the right are values greater than the pivot. Then
        select function class itself recursively until the index is found 
        in its correct place or is not in the left or right partitions so 
        its in the middle with its equal values.
        Runtime: O(nlogn) -> quicksearch average O(n^2) -> worst case
        Space: O(1) -> the swapping is done in place 
        '''
        def partition(l: int, r: int, p: int) -> int:
            pivot = nums[p]
            nums[p], nums[r] = nums[r], nums[p]
            m = l
            while m <= r:
                if nums[m] < pivot:
                    nums[m], nums[l] = nums[l], nums[m]
                    m += 1
                    l += 1
                elif nums[m] == pivot:
                    m += 1
                elif nums[m] > pivot:
                    nums[m], nums[r] = nums[r], nums[m]
                    r -= 1
            return l - 1, m

        def select(l: int, r: int, k: int) -> int:
            if l >= r:
                return l
            p = random.randint(l, r)
            low_r, high_l = partition(l, r, p)
            if high_l <= k:
                return select(high_l, r, k)
            if low_r >= k:
                return select(l, low_r, k)
            return low_r + 1
        return nums[select(0, len(nums) - 1, len(nums) - k)]
