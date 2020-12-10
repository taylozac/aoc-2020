f = open("input.txt", "r")
raw = f.read().splitlines()
f.close()

data = [int(i) for i in raw]


pre_len = 25


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return True
    return False


for i in range(pre_len + 1, len(data)):

    if not twoSum(data[i - (pre_len + 1) : i], data[i]):
        print(data[i])
        break

else:
    print("all nums satisfy requirements")
