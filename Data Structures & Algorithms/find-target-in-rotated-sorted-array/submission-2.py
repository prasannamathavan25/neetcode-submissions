class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lp = 0
        rp = len(nums) - 1

        while lp < rp:
            mid = lp + (rp - lp) // 2

            if nums[mid] > nums[rp]:
                lp = mid + 1          # Min is in right half
            else:
                rp = mid              # Keep mid since it may be the minimum

        pivot = lp

        if nums[pivot] == target:
            return pivot              # Target is the minimum

        if pivot == 0:
            lp = 0                    # Array is not rotated
            rp = len(nums) - 1
        elif nums[0] <= target <= nums[pivot - 1]:
            lp = 0                    # Target lies in left sorted half
            rp = pivot - 1
        else:
            lp = pivot                # Target lies in right sorted half
            rp = len(nums) - 1

        # Standard Binary Search
        while lp <= rp:
            mid = lp + (rp - lp) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                rp = mid - 1          # Search left half

            else:
                lp = mid + 1          # Search right half

        return -1