'''347. Top K Frequent Elements'''
class Max_Heap:
    '''Custom max heap class'''
    def __init__(self):
        '''Constructor method'''
        self.heap = [None]
        self.size = 0

    def _swap(self, m, n):
        '''Swaps the places in the heap of the given indices'''
        self.heap[m], self.heap[n] = self.heap[n], self.heap[m]

    def _sink(self, k):
        '''Sinks value to its correct place on the heap'''
        if k >= self.size:
            return
        child_1 = k*2
        child_2 = (k*2)+1
        if child_1 > self.size:
            return
        max_child = child_1
        if child_2 <= self.size:
            if self.heap[child_2][1] > self.heap[child_1][1]:
                max_child = child_2
        if self.heap[k][1] > self.heap[max_child][1]:
            return
        self._swap(k, max_child)
        self._sink(max_child)

    def _swim(self, val, k):
        '''Swims a newly added value to its correct place on the heap'''
        if k <= 1:
            return
        if val[1] <= self.heap[k//2][1]:
            return
        self._swap(k//2, k)
        self._swim(val, k//2)

    def get_max(self):
        '''Gets and removes the current max value of the heap'''
        self._swap(1, self.size)
        cur_max = self.heap.pop()
        self.size -= 1
        self._sink(1)
        return cur_max

    def add(self, val):
        '''Adds a value to the heap'''
        self.heap.append(val)
        self.size += 1
        self._swim(val, self.size)

class Solution:
    '''Solution Class'''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''Creates a dictionary with each unique number being keys and the
        number of occurences being the values. Then the keys value pairs are
        add to a custom max heap as tuples. Then the k max values of the
        heap are added to a list that is returned'''
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
        max_heap = Max_Heap()
        for num in nums_dict.keys():
            max_heap.add((num, nums_dict[num]))
        top_k = []
        for _ in range(k):
            top_k.append(max_heap.get_max()[0])
        return top_k
