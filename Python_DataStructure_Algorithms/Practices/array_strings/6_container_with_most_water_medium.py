"""
Given n non-negative integers where each integer represent the height of a vertical line on a chart.
Find two lines, which together with x-axis forms a container, that holds the biggest amount of water.
return the area of the water.

"""
from typing import List

# O(n)
def maxArea2(heights:List[int]) -> int:
    i = 0
    j = len(heights) - 1 
    max_area = 0
    while i < j: 
         height = min(heights[i], heights[j])
         width = j - i
         area = height * width
         max_area = max(max_area, area)
         if heights[i] < heights[j]:
             i += 1
         else:
             j -= 1
    return max_area

# bigO = n**2
def maxArea(heights:List[int]) -> int:
    max_area = 0
    for i in range(len(heights)):
        for j in range(i+1,len(heights)):
           height = min(heights[i], heights[j])
           width = j - i
           area = height * width
           max_area = max(max_area, area)
    return max_area

print(maxArea2([5,9,2,4]))
print(maxArea([5,9,2,4]))