# def insertionSort(array):
#     for i in range(len(array)):
#         j = i
#
#         while j > 0 and array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#             j -= 1
#
#     return array
#
# nums = [5,8,3,1,2,6]
# print(insertionSort(nums))

nums = [int(x) for x in input().split()]

for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
        else:
            break
print(nums)