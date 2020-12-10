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


def contigSum(nums, target):

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == target:
                return min(nums[i:j+1]) + max(nums[i:j+1])


for i in range(pre_len + 1, len(data)):

    if not twoSum(data[i - (pre_len + 1) : i], data[i]):

        print(contigSum(data, data[i]))
        break

else:
    print("all nums satisfy requirements")
