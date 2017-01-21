class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.l = len(nums)
        self.table = [[float('inf') for i in range(self.l)] for j in range(self.l)]
        for i in range(self.l):
            self.table[i][i] = nums[i]
        for line in self.table:
            print(line)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        print(i, j)
        if self.table[i][j] != float('inf'):
            return self.table[i][j]
        t = self.nums[j] + self.sumRange(i, j - 1)
        self.table[i][j] = t
        return t

class NumArray2(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        l = len(nums)
        self.table = [0 for i in range(l)]
        s = 0
        for i in range(l):
            s += nums[i]
            self.table[i] = s
            
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.table[j] - (self.table[i - 1] if i - 1 >= 0 else 0) 

def main():
    nums = [-2, 0, 3, -5, 2, -1]
    na = NumArray2(nums)
    print(na.table)
    print(na.sumRange(0, 2))

if __name__ == '__main__':
    main()