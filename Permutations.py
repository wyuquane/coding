class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        index = dict()
        for i, num in enumerate(nums):
            index[num] = i
        queues = [[num] for num in nums]
        for i in range(len(nums) - 1):
            for j in range(len(queues)):
                queue = queues.pop(0)
                non_appear = list()
                for num in queue:
                    non_appear.append(index[num])
                for k in range(len(nums)):
                    if k not in non_appear:
                        queues.append(queue + [nums[k]])
        return queues

if __name__ == '__main__':
    import numpy as np
    result = Solution().permute([1, 2, 3, 4, 5])
    print(np.array(result))