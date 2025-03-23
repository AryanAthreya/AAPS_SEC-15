"""
leetcode:33. Search in Rotated Sorted Array
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i  # Return index of the target
        return -1  # Return -1 if not found
    




"""
leetcode:167. Two Sum II - Input Array Is Sorted
"""
# using 2 pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        right,left=0,n-1
        # iterate right from 0 to n-1
        for right in range(n):
            while right < left and numbers[right]+numbers[left]>target:
                left-=1
            if right < left and numbers[right]+numbers[left]==target:
                return [right+1,left+1] #2 numbers return
        return []   # Return empty if no solution is found 
    



"""
leetcode:2149. Rearrange Array Elements by Sign
"""    
# Two pointers solution 
# positive initially at start and neg at 1,
# increment by 2 to keep left the space for -ive pointer
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n, pos, neg = len(nums), 0, 1
        arr = [0] * n 
        for i in nums:
            if i >= 0:
                arr[pos] = i
                pos += 2
            else:
                arr[neg] = i
                neg += 2
        return arr