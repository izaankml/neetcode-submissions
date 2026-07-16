class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            min_bar_height = min(heights[left], heights[right])
            width = right - left
            max_area = max(max_area, min_bar_height * width)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area