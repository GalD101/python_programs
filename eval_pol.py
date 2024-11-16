def horner(a, x):
    n = len(a)
    p = 0
    for i in reversed(range(n)):
        p = a[i] + x * p
    return p


# evaluate by dividing by x-x_0 and calculating the remainder (30.1-2 in the book):


def divide_polynomial_by_linear(poly, root):
    # Divides `poly` by (x - root) and returns the quotient polynomial and remainder
    n = len(poly)
    quotient = [0] * (n - 1)
    remainder = poly[0]

    for i in range(1, n):
        quotient[i - 1] = remainder
        remainder = poly[i] + remainder * root

    return quotient  # Only the quotient is needed for Lagrange interpolation


def construct_product_polynomial(x_values):
    # Start with the constant polynomial "1", represented as [1]
    product_poly = [1]

    for x in x_values:
        # Multiply the current product by (x - x_j)
        product_poly = multiply_polynomial_by_linear(product_poly, -x)

    return product_poly


def multiply_polynomial_by_linear(poly, x_0):
    n = len(poly)
    result = [0] * (n + 1)

    # Example to understand:
    # poly = 5x^3 + 2x^2 + 3x + 4
    # x_0 = 4
    # result = poly * (x + x_0)

    # result = [5x^4] + [50x^3 + 2x^3] + [20x^2 + 3x^2] + [30x + 4x] + 40
    # so in every loop, I need to *add* to the current item (with x) and also *add* to the next item (i + 1)
    # This is why the += is important
    # i takes care of the term wih x and i+1 the term without x

    for i in range(n):
        result[i] += poly[i]  # term with x
        result[i + 1] += poly[i] * x_0 * -1  # term without x
    return result


def lagrange_interpolation(points: list[tuple]):
    n = len(points)

    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    big_pi = construct_product_polynomial([-x_value for x_value in x_values])

    nominator = [[] for _ in range(n)]
    sum_nominator = [0] * (n + 1)

    # divide by the matching x_k
    for k in range(n):
        nominator[k] = divide_polynomial_by_linear(big_pi, x_values[k])

    factors = y_values
    for k in range(n):
        for j in range(n):
            if j != k:
                factors[k] /= (x_values[k] - x_values[j])

    ans = [0] * n
    new_nominator = [[] for _ in range(n)]
    for i in range(n):
        new_nominator[i] = [nominator[i][k] * factors[i] for k in range(n)]

    ans = [0] * n
    for i in range(len(new_nominator)):
        for j in range(len(new_nominator[i])):
            ans[i] += new_nominator[j][i]
    return ans


import cmath


def dft(vec: list):
    n = len(vec)
    ans = [0] * n
    for k in range(n):
        y = 0
        for i in range(n):
            w = cmath.exp((k) * (i) * (2 * cmath.pi * 1j) / n)
            y += vec[i] * w
        ans[k] = (complex(round(y.real), round(y.imag)))
    return ans


def before_fft(vec: list):
    n = len(vec)
    # make the vector a length of a power of 2
    while n & (n - 1) != 0:
        vec.append(0)
        n += 1
    return vec


def fft(vec: list):
    n = len(vec)
    if n == 1: return vec
    vec = before_fft(vec)
    w_n = cmath.exp(2 * cmath.pi * 1j / n)
    w = 1
    vec_even = vec[0::2]
    vec_odd = vec[1::2]

    y_even = fft(vec_even)
    y_odd = fft(vec_odd)
    y = [0] * (n)

    for k in range(n // 2):
        y[k] = y_even[k] + w * y_odd[k]
        y[k + (n // 2)] = y_even[k] - w * y_odd[k]
        w = w * w_n

    y = [complex(round(y_val.real), round(y_val.imag)) for y_val in y]
    return y


def inverse_fft(vec: list):
    n = len(vec)
    if n == 1: return vec
    w_n = cmath.exp(-2 * cmath.pi * 1j / n)
    w = 1
    vec_even = vec[0::2]
    vec_odd = vec[1::2]

    y_even = inverse_fft(vec_even)
    y_odd = inverse_fft(vec_odd)
    y = [0] * (n)

    for k in range(n // 2):
        y[k] = y_even[k] + w * y_odd[k]
        y[k + (n // 2)] = y_even[k] - w * y_odd[k]
        w = w * w_n

    y = [complex(round(y_val.real), round(y_val.imag)) for y_val in y]
    return y


# def find_coefficients_from_roots(roots: list):
#     n = len(roots)
#     if n == 1:
#         return [1, -roots[0]]
#     # Divide
#     half1 = roots[0:n//2]
#     half2 = roots[n//2:]
#
#     # Solve
#     sol1 = find_coefficients_from_roots(half1)
#     sol2 = find_coefficients_from_roots(half2)
#
#     return fft_pol_mul(sol1, sol2)

import math


def get_num_of_special_triplets(s):
    n = len(s)
    num_of_special_pairs = 0
    for i in range(n - 2):
        for d in range(1, math.ceil((n - i) / 2)):
            num_of_special_pairs += int(s[i]) * int(s[i + d]) * int(s[i + 2 * d])
    return num_of_special_pairs


import numpy as np


def get_num_of_special_triplets_using_fft(s):
    n = len(s)

    # Convert the string into a list of integers
    s = [int(x) for x in s]

    # Pad to the next power of 2 greater than or equal to 2n-1
    padded_length = 2 ** (math.ceil(math.log2(2 * n - 1)))
    s += [0] * (padded_length - n)

    # Compute FFT of the input polynomial
    fft_s = np.fft.fft(s)

    # Square the FFT-transformed array
    fft_s_squared = [x * x for x in fft_s]

    # Compute the inverse FFT to get coefficients
    s_squared = np.fft.ifft(fft_s_squared)

    # Extract real parts, round them to integers
    s_squared = [round(x.real) for x in s_squared]

    # Initialize counter
    counter = 0

    # Count special triplets based on the odd coefficients
    for i in range(2 * n - 1):  # Only iterate over the original valid range
        if s_squared[i] > 1 and s_squared[i] % 2 == 1:
            counter += (s_squared[i] - 1) // 2

    return counter


def test_special_triplets():
    test_cases = [
        "10101",  # Example with overlapping triplets
        "10011110",  # Example with known output
        "111111",  # All ones
        "000000",  # All zeros
        "101010",  # Alternating ones and zeros
        "1100110011",  # Pattern with many triplets
        "1",  # Single element
        "101"  # Smallest input size with a valid triplet
    ]

    for s in test_cases:
        naive_result = get_num_of_special_triplets([int(c) for c in s])
        fft_result = get_num_of_special_triplets_using_fft(s)

        print(f"Testing: {s}")
        print(f"Naive Result: {naive_result}, FFT Result: {fft_result}")
        assert naive_result == fft_result, f"Mismatch for input {s}"

    print("All tests passed!")


# Run the test
test_special_triplets()
