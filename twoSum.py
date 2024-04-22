nums = [12,2,11,7,15]
target = 9
answer = [0,1]
seen = {}

def twoSum(nums, target):
    seen = {}

    for i, value in enumerate(nums):
        diff = target - value

        if diff in seen:
            print([seen[diff], i])
            return [seen[diff], i]

        seen[value] = i
        print (seen[value])

twoSum(nums, target)