def get_median(nums):
    if len(nums) % 2:
        median = nums[len(nums) / 2]
    else:
        median = (nums[len(nums) / 2] + nums[(len(nums) / 2) - 1]) / 2
    return median

def get_mode(nums):
    mode = None
    counts = {}
    max_count = 1
    for num in nums:
        counts.setdefault(num, 0)
        counts[num] += 1
        if counts[num] > max_count:
            mode = num
            max_count = counts[num]
        elif counts[num] == max_count:
            mode = None
    return mode

def count_chars(chars):
    counts = {}
    for char in chars:
        counts.setdefault(char, 0)
        counts[char] += 1
    return counts


last_input = ""
while last_input != "quit":
    last_input = raw_input("Please enter a numerical sequence or literal string: ")
    if not last_input:
        continue
    if last_input[0].isdigit():
        nums = last_input.split()
        nums = sorted([int(num) for num in nums])

        mean = sum(nums) / len(nums)
        median = get_median(nums)
        mode = get_mode(nums)
        range = nums[-1] - nums[0]

        print "mean =", mean
        print "median =", median
        print "mode =", mode
        print "range =", range
    else:
        chars = sorted(filter(lambda char: char.isalpha() or char.isdigit(), last_input))
        counts = count_chars(chars)
        printed = set()
        for char in chars:
            if char not in printed:
                print char + ":", counts[char]
                printed.add(char)
