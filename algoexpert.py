def largestRange(array):
    currentDiff = 0
    maxDiff = 0
    minimum = min(array)
    currentLargest = [minimum, minimum]
    maxLargest = [minimum, minimum]
    while len(array):
        minimum = (min(array))
        while minimum in array:
            array.remove(minimum)
        if not len(array):
            break
        if (minimum + 1) in array:
            currentLargest[1] = minimum + 1
            currentDiff = currentLargest[1] - currentLargest[0]
        else:
            if (currentDiff > maxDiff):
                maxDiff = currentDiff
                maxLargest = currentLargest[:]
            currentDiff = 0
            if len(array):
                currentLargest[0] = min(array)
                currentLargest[1] = min(array)
    if currentDiff < maxDiff:
        return maxLargest
    return currentLargest

def isValidSubsequence(array, sequence):
    array_after_change = array
    prev_num = sequence[0]
    for i, num in enumerate(sequence):
        flag = False
		# if the number is not in the array
		# then there is no way it can be a sequence
        if not num in array_after_change:
            return False
        
        # cut the array so that the first element will be the corresponding number in the sequence (num)
        # NOTE: should probably just use the index and not actually delete all the previous elements but that was my intuition for some reason
        array_after_change = array[array.index(num):]

        # NOTE: the following lines are for edge cases where there are two tracking (I think)
        # if two identical number are adjascent (the i !=0 is to make sure we dont compare prev_num and num on the first iteration because they WILL be equal)
        if prev_num == num and i != 0:
            # then check if this is the last item we have
            if len(array_after_change) == 1:
                # if this is the last item in the array, idk wtf
                return False
            flag = True
        if flag:
            array_after_change = array[array.index(num) + 1:]
        if num != array_after_change[0]:
            return False
        prev_num = num
        
    return True

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],
      [10]))


# print(largestRange([
#     19,
#     -1,
#     18,
#     17,
#     2,
#     10,
#     3,
#     12,
#     5,
#     16,
#     4,
#     11,
#     8,
#     7,
#     6,
#     15,
#     12,
#     12,
#     2,
#     1,
#     6,
#     13,
#     14
# ]))