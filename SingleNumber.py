def singleNumber(nums):
    for number in nums:
        if nums.count(number) == 1:
            return number