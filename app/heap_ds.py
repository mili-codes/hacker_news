
# class Tree:
#     def __init__(self, val=None, right=None, left=None) -> None:    
#         self.val = val
#         self.right = right
#         self.left = left

class Heap:
    def __init__(self, arr = None) -> None:
        self.heap = []
        self.heap = arr.copy()
        for i in range(len(self.heap))[::-1]:
            self._siftdown(i)
            
    def _siftup(self, i):
        parent = (i-1)//2
        while i!=0 and self.heap[i]<self.heap[parent]:
            self.heap[i],self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2
    
    def _siftdown(self, i):
        left = 2*i+1
        right = 2*i+1
        heap_len = len(self.heap)
        while (left < heap_len and self.heap[i] > self.heap[left]) or (right < heap_len and self.heap[i] > self.heap[right]):
            smallest = left if(right>=heap_len or self.heap[left]<self.heap[right]) else right
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i+1
            right = 2*i+1
    
    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)
    
    def getmin(self):
        return self.heap[0] if len(self.heap) > 0 else None
    
    def extract_min(self):
        if len(self.heap) == 0: return None
        minval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return minval
    
    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new>old:
            self._siftdown(i)
        else:
            self._siftup(i)
    
    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)
    

    

