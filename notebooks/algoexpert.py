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


print(largestRange([
    19,
    -1,
    18,
    17,
    2,
    10,
    3,
    12,
    5,
    16,
    4,
    11,
    8,
    7,
    6,
    15,
    12,
    12,
    2,
    1,
    6,
    13,
    14
]))