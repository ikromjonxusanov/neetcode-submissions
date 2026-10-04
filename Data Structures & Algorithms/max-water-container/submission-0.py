class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            distance = r - l
            l_h = heights[l]
            r_h = heights[r]
            area = distance * min(l_h, r_h)
            max_area = max(max_area, area)
            
            if l_h > r_h:
                r -= 1
            else:
                l += 1
        return max_area