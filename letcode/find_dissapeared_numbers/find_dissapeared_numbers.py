from typing import List


def findDissapearedNumbers(self, nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        pos = nums[i] - 1
        if nums[i] != nums[pos]:
            nums[i], nums[pos] = nums[pos], nums[i]
        else:
            i += 1
    
    missingNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)

    return missingNumbers