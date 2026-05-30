class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1. find max height O(n)
        # 2. find max possible area (assume both ends have max)
        # 3. start actually calculating
        #  a. small = min(left-most pointer, right-most pointer)
        #  b. max_area = small * (len(heights) - 2)
        #  c. if max_area = max_possible_area, return max_area
        #  d. calculate max possible area if we subtract 1 from the heights length

        max_height = max(heights)
        front_index = 0
        back_index = len(heights) - 1
        max_area_seen = 0

        index_diff = back_index - front_index

        while index_diff > 0:
            smaller = min(heights[front_index], heights[back_index])
            area_seen = smaller * index_diff
            if area_seen > max_area_seen:
                max_area_seen = area_seen
            if heights[front_index] <= heights[back_index]:
                front_index += 1
            else:
                back_index -= 1
            index_diff = back_index - front_index
            
        return max_area_seen