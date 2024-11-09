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
        result[i] += poly[i] # term with x
        result[i + 1] += poly[i] * x_0*-1 # term without x
    return result


print(construct_product_polynomial([1, 2, 3,4, 5]))


def lagrange_interpolation(points:list[tuple]):
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
    for i in range(len(nominator)):
        ans[i] = factors[i] * nominator[i]
    return ans


lagrange_interpolation([(0, 1), (1, 6), (2, 17)])






#
#
#
# def get_coefficients_from_roots_vieta(roots: list):
#     n = len(roots)
#     coefficients = [0 for _ in range(n)]
#     coefficients.append(1)
#     sign = -1
#     for j in range(n):
#         ans = 0
#         for i in range(n):
#             term = roots[i]
#             for k in range(i, j):
#                 term *= roots[k+1]
#             ans += term
#         print(ans)
#         ans *= sign
#         sign *= -1
#         coefficients[n - 1 - j] = ans
#
#     return coefficients
#
#
# # Lagrange interpolation (O(n^2)):
#
# def interpolate_lagrange(points: tuple) -> list:
#     n = len(points)
#     if n == 1:
#         return points[0][1]
#
#     # Extract the x value from the point pair (point[0] == x_i & point_i = (x_i, y_i))
#     b_roots = [point[0] for point in points]  # O(n)
#     b_coefficients = [0 for _ in range(n)]
#
#     # This is the simple case of the convolution that we were to calculate naively
#     # (only one way to get the maximum power)
#     b_coefficients[n - 1] = 1
#
#     # Now calculate the rest of b_coefficients using Vieta's formulas:
#     sign = -1
#     for j in range(n):
#         ans = 0 # (n-1) - (j+1)
#         for i in range(n):
#             term = b_roots[i]
#             for k in range(i, j):
#                 term *= b_roots[k]
#             ans += term
#         ans *= sign * b_coefficients[n - 1]
#         sign *= -1
#         b_coefficients[n - 1 - j] = b_coefficients[n - 1]*sign*ans
#
#     for l in range(len(b_coefficients)):
#         print(b_coefficients[l])
#
#     q = [0 for _ in range(n - 1)]  # O(n)
#     h = [0 for _ in range(n - 1)]  # O(n)
#
#     # O(n^2):
#     for k in range(n - 1):  # O(n)
#         for j in range(n):  # O(n)
#             if j != k:
#                 h[k] *= (points[k][0] - points[j][0])
#
#         # Calculate q:
#


# print(eval_by_division([5, 4, -3, 2], -2))
