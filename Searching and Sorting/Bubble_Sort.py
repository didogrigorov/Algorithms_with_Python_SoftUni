nums = [5,4,3,2,1]

is_sorted = False
counter = 0

while not is_sorted:
    is_sorted = True

    for idx in range(1, len(nums) - counter):
        if nums[idx] < nums[idx - 1]:
            nums[idx], nums[idx - 1] = nums[idx -1], nums[idx]
            is_sorted = False

    counter += 1

print(*nums, sep=" ")

# def bubbleSort(array):
#     for i in range(0, len(array) - 1):
#         for j in range(0, len(array)-1-i):
#             if array[j] > array[j + 1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array