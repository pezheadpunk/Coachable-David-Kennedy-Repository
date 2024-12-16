'''70. Climbing Stairs'''
class Solution:
    '''Solution Class'''
    def climbStairs(self, n: int) -> int:
        '''Uses the bottom-up approach to basically
        so the fibanacci sequence as when taking steps
        there are only two chocies: 1 step or 2 steps.'''
        if n <= 1:
            return n
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
