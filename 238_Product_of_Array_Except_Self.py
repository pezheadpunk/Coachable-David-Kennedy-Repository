'''238. Product of Array Except Self'''
from typing import List

class Solution:
    '''Solution Class'''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Creates an array that is the same length as nums with the first value in
        nums populating the array. Then it iterates fowards through the list and
        placing in the i index of the array the running products of the values
        before. Then starts iterating backwards creating a new running product that 
        multiplies with a previous value in found before the current index in nums to 
        populate the array with the correct values.
        '''
        n = len(nums)
        products = [1] * n
        prefix = 1
        for i in range(n):
            products[i] = prefix
            prefix = products[i] * nums[i]
        suffix = 1
        for j in range(n-1, -1, -1):
            products[j] = suffix * products[j]
            suffix = suffix * nums[j]
        return products
