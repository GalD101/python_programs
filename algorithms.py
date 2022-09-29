def square_and_multiply(b: int, e: int, m: int) -> int:
    """
    finds the solution to the equation b^e mod(m) fast
    using the square and multiply algorithm
    checkout https://youtu.be/cbGB__V8MNk 
    (does the same as pow with 3 parameters)
    """
    binary_exponent = str(bin(e))[2::]
    final_result = 1
    for bit in binary_exponent:
        final_result **= 2
        final_result %= m
        if bit == '1':
            final_result *= b
            final_result %= m
    return final_result

def lfsr():
    state = (1 << 127 ) | 1
    while True:
        print(state & 1, end='', flush=True)
        newbit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7))
        state = (state >> 1) | (newbit << 127)



def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(l: list, r: list):
    merged_list = []
    while len(l) or len(r):
        if len(l) and len(r):
            if l[0] < r[0]:
                merged_list.append(l.pop(0))
            else:
                merged_list.append(r.pop(0))
        elif len(l):
            merged_list.append(l.pop(0))
        elif len(r):
            merged_list.append(r.pop(0))
    return merged_list



print(merge_sort([2, 4, 1, 7, 5, 3, 6, 8]))
# lfsr()
# print(square_and_multiply(23, 373, 747))
# print(square_and_multiply(3, 45, 7))
