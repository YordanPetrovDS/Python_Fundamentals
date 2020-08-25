import math

nums = list(map(int, input().split(", ")))
max_num = max(nums)
groups_count = math.ceil(max_num / 10)

for group in range(1, groups_count + 1):
    # groups_num = []
    # min = 10 * (group - 1)
    # max = group * 10
    # for num in nums:
    #     if min < num <= max:
    #         groups_num.append(num)
    groups_num = [num for num in nums if 10 * (group - 1) < num <= group * 10]
    print(f"Group of {group * 10}'s: {groups_num}")


