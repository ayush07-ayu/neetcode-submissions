class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water = 0
        n = len(heights)

        # outer loop
        for i in range(n):

            # inner loop
            for j in range(i + 1, n):

                # water calculate
                water = min(heights[i], heights[j]) * (j - i)

                # maximum update
                max_water = max(max_water, water)

        return max_water