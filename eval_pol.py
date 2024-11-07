# Horner's method:
def horner(a, x):
    n = len(a)
    p = 0
    for i in reversed(range(n)):
        p = a[i] + x * p
    return p


# evaluate by dividing by x-x_0 and calculating the remainder (30.1-2 in the book):

def eval_by_division(a, x):
    n = len(a)
    q = [0 for _ in range(n - 1)]
    q[n - 2] = a[n - 1]
    for i in reversed(range(n - 2)):
        q[i] = a[i + 1] + x * q[i + 1]
    return a[0] + x * q[0]


# Lagrange interpolation (O(n^2)):

def interpolate_lagrange(points: tuple) -> list:
    n = len(points)
    if n == 1:
        return points[0][1]

    # Extract the x value from the point pair (point[0] == x_i & point_i = (x_i, y_i))
    b_roots = [point[0] for point in points]  # O(n)
    b_coefficients = [0 for _ in range(n)]

    # This is the simple case of the convolution that we were to calculate naively
    # (only one way to get the maximum power)
    b_coefficients[n - 1] = 1

    # Now calculate the rest of b_coefficients using Vieta's formulas:
    sign = -1
    for j in range(n):
        ans = 0 # (n-1) - (j+1)
        for i in range(n):
            term = b_roots[i]
            for k in range(i, j):
                term *= b_roots[k]
            ans += term
        ans *= sign * b_coefficients[n - 1]
        sign *= -1


    b_coefficients[n - 1 - j] = b_coefficients[n - 1]*sign*()

    q = [0 for _ in range(n - 1)]  # O(n)
    h = [0 for _ in range(n - 1)]  # O(n)

    # O(n^2):
    for k in range(n - 1):  # O(n)
        for j in range(n):  # O(n)
            if j != k:
                h[k] *= (points[k] - points[j])
        # Calculate q:
