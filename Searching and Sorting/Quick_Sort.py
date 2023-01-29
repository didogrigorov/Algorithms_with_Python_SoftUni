def quickSort(array):
    quicksorthelper(0, len(array) - 1, array)
    return array

def quicksorthelper(start, end, nums):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]

    quicksorthelper(start, right - 1, nums)
    quicksorthelper(left, end, nums)

    return nums

nums = [2,5,3,1,6,5,7,9]
print(quickSort(nums))