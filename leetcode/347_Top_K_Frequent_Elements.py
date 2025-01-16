'''347. Top K Frequent Elements'''
import heapq
import random
from typing import List

class Solution:
    '''Solution Class'''
    def topKFrequent_heapq(self, nums: List[int], k: int) -> List[int]:
        '''Creates a dictionary with each unique number being keys and the
        number of occurences being the values. Then the keys value pairs are
        add to a heap as tuples. Then the k max values of the
        heap are added to a list that is returned'''
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
        nums_data = [(val, key) for key, val in nums_dict.items()]
        heapq.heapify(nums_data)
        top_nums= heapq.nlargest(k, nums_data)
        top_k = []
        for num in top_nums:
            top_k.append(num[1])
        return top_k

    def topKFrequent_quickselect(self, nums: List[int], k: int) -> List[int]:
        '''Creates a dictionary with each unique number being keys and the
        number of occurences being the values and convert that dictionary
        to a list of key value tuples. Then the quickselect algorithm is used 
        to find the top k frequent values.'''
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
        nums_dict = list(nums_dict.items())

        def partition(l: int, r: int, p: int) -> int:
            pivot = nums_dict[p]
            nums_dict[p], nums_dict[r] = nums_dict[r], nums_dict[p]
            i = l
            for j in range(l, r):
                if nums_dict[j][1] < pivot[1]:
                    nums_dict[j], nums_dict[i] = nums_dict[i], nums_dict[j]
                    i += 1
            nums_dict[r], nums_dict[i] = nums_dict[i], nums_dict[r]
            return i

        def select(l: int, r: int, k: int) -> int:
            if l == r:
                return l
            p = random.randint(l, r)
            p = partition(l, r, p)
            if p < k:
                return select(p + 1, r, k)
            if p > k:
                return select(l, p - 1, k)
            else:
                return p

        top_k = [num[0] for num in nums_dict[select(0, len(nums_dict) - 1, len(nums_dict) - k):]]
        return top_k
