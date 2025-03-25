"""
Binary search Algorithm. t.c. = O(log n)+ n for sorting== O(n log n), linear t.c.
"""


# binary search algo:

from typing import List
def binary_search(arr: List[int], target: int) -> int:
    arr.sort()  # Ensure the array is sorted
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2  # Midpoint calculation

        if arr[mid] == target:
            return mid  # Target found at index `mid`
        elif arr[mid] < target:
            start = mid + 1  # Search in the right half
        else:
            end = mid - 1  # Search in the left half

    return -1  # Target not found
# Example Usage
arr = [9, 1, 7, 5, 3, 11, 15]
target = 7
print(binary_search(arr, target))


# leetcode-34. Find First and Last Position of Element in Sorted Array
# using 2 binary searches:
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums = [5,7,7,8,8,10]
        target = 8

        # Find First Occurrence
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    # from index 0 to mid-1 check on rhs of array:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    right = mid - 1  # Continue searching on the left side <--

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # last target
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:

                    # from index n-1 to mid+1 check on lhs of array
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    left = mid + 1  # Continue searching on the right side -->

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # eg:
        nums = [5,7,7,8,8,10]
        target = 8
        # function call
        first = findFirst(nums, target)
        last = findLast(nums, target)

        # return result
        return [first, last]

# answer print:
solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))



# gfg -Number of occurrence
# Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 
from typing import List
class Solution:
    def countOccurrences(self, nums: List[int], target: int) -> List[int]:

        # Find First Occurrence
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    # from index 0 to mid-1 check on rhs of array:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    right = mid - 1  # Continue searching on the left side <--

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # last target
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:

                    # from index n-1 to mid+1 check on lhs of array
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    left = mid + 1  # Continue searching on the right side -->

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # function call
        first = findFirst(nums, target)
        last = findLast(nums, target)

        # if target not found
        if first==-1 or last==-1:
            return 0

        # return total number of occurences of target from given array
        return (last-first)+1


# Example test case
solution = Solution()
print("Max occurent element is:",solution.countOccurrences([5, 7, 7, 8, 8, 8, 10], 8))  



# Leetcode 852: peak index in a mountin array
# usinf bianry search
"""
Conditions for traversal:
If arr[mid] < arr[mid + 1] → Move right (ascending part).
If arr[mid] > arr[mid + 1] → Move left (descending part).
If arr[mid - 1] < arr[mid] > arr[mid + 1] → Found the peak.
"""
from typing import List
class solution:
    def index_of_peak_element(self, arr:[List[int]])->int:
        # initializing start and end with 0 and n-1 index position
        s,e=0,len(arr)-1

        # implementing binary search
        while s<=e:
            mid=s+(e-s)//2

            # question specific condition;check if mid is peak, this 'if' checks for mountain peak array
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            # checking from ascendin part of the mountain
            if arr[mid]<arr[mid+1]:
                s=mid+1 #move mid to right position
            # checking from decending part of the mountain
            if arr[mid]<arr[mid-1]:
                e=mid-1 #move mid to left position 
        #if peak not found  ; its an edge case        
        return -1           
#class call
sol=solution() 
print("peak elemrent is:",sol.index_of_peak_element([0,1,3,4,5,7,10,8,6,4,2]))