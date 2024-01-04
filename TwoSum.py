def num1(n):
    for i in range(0, n):
        x = int(input())
        lst.append(x)
    return lst


def two_sum(nums, target):
    sum1 = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                sum1.append(i)
                sum1.append(j)
                return sum1


lst = []
target = int(input("target = "))
n = int(input("No. of elements: "))
nums = num1(n)
print(f"Input: nums = {nums}, target = {target}")
two_sum1 = two_sum(nums, target)
print(f"Output: {two_sum1}")

