def square_and_multiply(b: int, e: int, m: int) -> int:
    """
    finds the solution to the equation b^e mod(m) fast
    using the square and multiply algorithm
    checkout https://youtu.be/cbGB__V8MNk 
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

print(square_and_multiply(23, 373, 747))
print(square_and_multiply(3, 45, 7))
