'''238. Product of Array Except Self'''
class Solution:
    '''Solution Class'''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Creates an array that is the same length as nums with the first value in
        nums populating the array. Then if iterates fowards through the list and
        placing in the i index of the array the running products of the values
        before. Then swaps the running product in the second to last index with
        the last value of nums and then starts iterating backwards creating a new
        running product that multiplies with a previous value in found before the
        current index in nums to populate the array with the correct values.
        '''
        products = [nums[0]] * len(nums)
        for i in range(1, len(nums)-1):
            products[i] = nums[i] * products[i-1]
        products[-1], products[-2] = products[-2], nums[-1]
        for i in range(len(nums)-2, 0, -1):
            products[i-1], products[i] = products[i]*nums[i], products[i]*products[i-1]
        return products
