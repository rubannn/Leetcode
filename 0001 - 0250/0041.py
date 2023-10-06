def firstMissingPositive(nums: list[int]) -> int:
    nums.sort(key=lambda x: x if x > 0 else 2**32)
    k = 0
    for i, x in enumerate(nums):
        if i+1 < len(nums) and nums[i] == nums[i+1]:
            k += 1
            continue
        if nums[i] != i + 1 - k:
            return i + 1 - k
    return len(nums) + 1 - k


nums, ans = [1,2,0], 3
print(firstMissingPositive(nums) == ans)

nums, ans = [3,4,-1,1], 2
print(firstMissingPositive(nums) == ans)

nums, ans = [7,8,9,11,12], 1
print(firstMissingPositive(nums) == ans)

nums, ans = [-5], 1
print(firstMissingPositive(nums) == ans)

nums, ans = [1, 1], 2
print(firstMissingPositive(nums) == ans)

nums, ans = [-1,-2,-60,40,43], 1
print(firstMissingPositive(nums) == ans)

nums, ans = [1000,-1], 1
print(firstMissingPositive(nums) == ans)

nums, ans = [0,2,2,1,1], 3
print(firstMissingPositive(nums) == ans)
