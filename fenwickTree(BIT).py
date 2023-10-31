class BIT:
    def __init__(self, nums): # Builds BIT based on nums
        self.nums = nums
        self.bit = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])

    def _query(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & (-idx)
        return s

    def query(self, left, right):  # sum from left, right inclusive, 0-based indexing
        return self._query(right+1) - self._query(left)

    def update(self, idx, val):  # increase index(0-based) by val
        idx += 1
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & (-idx)