'''217. Contains Duplicate'''
class Solution:
    '''Solution Class'''
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''Uses a set to keep track of nums already found
        in the passed in list. If a num is already in the
        set, then it is a duplicate True is returned
        immediately. If the whole list is iterated over
        without out triggering this condition, False is
        returned'''
        memo = set()
        for num in nums:
            if num in memo:
                return True
            memo.add(num)
        return False
