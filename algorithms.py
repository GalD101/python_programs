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

lfsr()
# print(square_and_multiply(23, 373, 747))
# print(square_and_multiply(3, 45, 7))
