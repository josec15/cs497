import bisect

nums = [5,7,7,8,8,10]
target = 8

left = bisect.bisect_left(nums, target)
right = bisect.bisect_right(nums, target)

if left > right - 1:
    print([-1,-1])
else:
    print([left, right-1])
