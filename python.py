def duplicates(nums):
    sees=set()

    for num in nums:
        if num in sees:
            return True
        sees.add(num)

    return False
nums=[1,2,3,4,5]
print(duplicates(nums))