class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Edge case, return 0 if there is no array
        if not nums:
            return 0

        # Since the array is sorted, we can start at the end
        # Keep an index to our current element
        idx = len(nums) - 1

        # Keep going until index is second element
        while idx > 0:
            current = nums[idx]
            previous = nums[idx - 1]
            # If the current is == the previous, pop off the current
            if current == previous:
                nums.pop(idx)
            # Update the index to be one in
            idx -= 1

        return len(nums)
