from math import inf, log2


class SegmentTree:
    def __init__(self, array, func=max):
        self.n = len(array)
        self.size = 2**(int(log2(self.n-1))+1) if self.n != 1 else 1
        self.func = func
        self.default = 0 if self.func != min else inf
        self.data = [self.default] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size: self.size+self.n] = array
        for i in range(self.size-1, -1, -1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])

    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        if alpha == omega:
            return self.data[alpha + self.size]
        res = self.default
        alpha += self.size
        omega += self.size + 1
        while alpha < omega:
            if alpha & 1:
                res = self.func(res, self.data[alpha])
                alpha += 1
            if omega & 1:
                omega -= 1
                res = self.func(res, self.data[omega])
            alpha >>= 1
            omega >>= 1
        return res

    def update(self, index, value):
        """Updates the element at index to given value!"""
        index += self.size
        self.data[index] = value
        index >>= 1
        while index:
            self.data[index] = self.func(
                self.data[2*index], self.data[2*index+1])
            index >>= 1


arr = [1, 5, 2, 3]
seg = SegmentTree(arr, func=lambda a, b: a+b)  # for min just give fun=min

print("sum of elements between 1 and 3 is:", seg.query(1, 3))
seg.update(2, 4)  # updates element at 2nd index to 4
print("sum of elements between 1 and 3 is:", seg.query(1, 3))

# Normal Implementation


class segTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (4*self.n)
        self.build(0, 0, len(nums)-1)
        print(self.tree)

    def build(self, node, l, r):
        if l == r:
            self.tree[node] = self.nums[l]
        else:
            m = (r-l)//2 + l
            self.tree[node] = self.build(
                2*node+1, l, m) + self.build(2*node+2, m+1, r)
        return self.tree[node]

    def _update(self, node, l, r, index, val):
        if l == r:
            self.tree[node] = val
            return
        m = (r-l)//2 + l
        if index <= m:
            self._update(2*node+1, l, m, index, val)
        else:
            self._update(2*node+2, m+1, r, index, val)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def _query(self, node, l, r, left, right):
        if left <= l and r <= right:
            return self.tree[node]
        if r < left or l > right:
            return 0
        m = (r-l)//2 + l

        return self._query(2*node+1, l, m, left, right) + self._query(2*node+2, m+1, r, left, right)

    def update(self, index, val):
        self._update(0, 0, self.n-1, index, val)

    def query(self, left, right):
        return self._query(0, 0, self.n-1, left, right)
    
