'''528. Random Pick with Weight'''
from typing import List
import random

class Solution:
    '''Solution Class'''
    def __init__(self, w: List[int]):
        '''
        Initializes the object and stores the values of the total of
        all the weights in the list summed and an array of the sums
        up to that weight in the list.
        Runtime: O(n) -> for loop
        Space: O(n) -> self.weight_sums list 
        '''
        self.total_weight = 0
        self.weight_sums = []
        for weight in w:
            self.total_weight += weight
            self.weight_sums.append(self.total_weight)


    def pickIndex(self) -> int:
        '''
        Gets a random target value from among the weights and then uses
        binary search to find where that value would fall in the weights
        in the sums.
        Runtime: O(nlogn) -> binary search
        Space: O(1)
        '''
        target = random.randint(1, self.total_weight)
        low = 0
        high = len(self.weight_sums)-1
        while low < high:
            mid = (low + high) // 2
            if target > self.weight_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
