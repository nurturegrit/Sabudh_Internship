class SparseVector:
    '''
    Only Vecotr not a Tensor/Matrix
    '''
    def __init__(self, nums):
        self.vec = self.efficient(nums)

    def efficient(self, nums):
        vec = {i: nums[i] for i in range(len(nums)) if nums[i] != 0}
        return vec

    def dotProduct(self, other):
        result = 0
        for i in self.vec:
            if i in other.vec:
                result += self.vec[i] * other.vec[i]
        return result