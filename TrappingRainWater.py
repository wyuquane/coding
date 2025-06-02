class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) in (0, 1):
            return 0

        n = len(height)
        maximum = list()
        if height[0] >= height[1]:
            maximum.append(0)
        for i in range(1, n - 1):
            if height[i] >= height[i + 1] and height[i] >= height[i - 1]:
                maximum.append(i)
        if height[-1] >= height[-2]:
            maximum.append(n - 1)

        if len(maximum) in (0, 1):
            return 0
        print(maximum)
        i = 1
        while i < len(maximum) - 1:
            if height[maximum[i]] <= height[maximum[i + 1]] and height[maximum[i]] <= height[maximum[i - 1]]:
                maximum.pop(i)
            else:
                i += 1
        print(maximum)


        result = 0
        for i in range(len(maximum) - 1):
            h = min(height[maximum[i]], height[maximum[i + 1]])
            water = h * (maximum[i + 1] - maximum[i] - 1)
            for j in range(maximum[i] + 1, maximum[i + 1]):
                if height[j] <= h:
                    water -= height[j]
                else:
                    water -= h
            result += water

        return result


x = Solution().trap([8,8,1,5,6,2,5,3,3,9])
print(x)

