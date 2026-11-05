class Solution:
    def merge_sortArray(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        left = self.merge_sortArray(left)
        right = self.merge_sortArray(right)

        def merge(arr, left, right):
            i, j, k = 0, 0, 0

            #merge 2 sorted arrays
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            #remaining on left
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        merge(ans, left, right)
        return ans

    def insertion_sortArray(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            l = i - 1

            while l >= 0 and nums[l] > key:
                #shift one place right
                nums[l + 1] = nums[l]
                l -= 1
            nums[l + 1] = key
        return nums
    def bubble_sortArray(self, nums: list[int]) -> list[int]:
        while True:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
            if not swapped:
                break
        return nums
        
    def insertion_sortArray(self, nums: list[int]) -> list[int]:
        #selection
        for i in range(len(nums) - 1):
            smallest = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[smallest]:
                    smallest = j
            nums[i], nums[smallest] = nums[smallest], nums[i]

        return nums