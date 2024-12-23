(3 + 4e) * (5 + 6e)
3 * 5 # == self.real * other.real
3 * 6e # == self.real * other.epsilon
4e * 5 # == self.epsilon * other.real
4e * 6e # == self.epsilon * other.epsilon (should equal 0?) yes

real = self.real * other.real
epsilon = (self.real * other.epsilon) + (self.epilon * other.real)
15, 38

1 / (1 + 10e)
(1 * (1 - 10e)) / (1 + 10e) * (1 - 10e)

# multiply the numerator by the conjugate (a - be) as well as the denominator
so you get:
(1 - 10e) / ((1 + 10e) * (1 - 10e)) =
(1 - 10e) / 1
so it always equals the conjugate


n / (a + be) =
(n(a - be)) / (a^2) =
(n.__rmul__(a - be)).__truediv__(a*a)











(1 + 10e) / 2
1/2 + 10e/2 
0.5 + 5e











case 1: n / (a + be) where n is a real number and (a + be) is R_e
case 2: (a + be) / n where n is a real number and (a + be) is R_e
case 3: (a + be) / (c + de) where (a + be) and (c + de) are R_e

case 1 is __rtruediv__
case 2 is __truediv__
case 3 is __truediv__

case 1:
First, multiply by the conjugate so you get:
(n * (a - be)) / ((a + be) * (a - be))

First, let's take care of the numerator:
the real part is (n * a), the "dual part" is n * -be
so for the real part save  n*a
for the "dual part" save   -n*b
so we create an instance: R_e(n*a, -n*b)

Now, let's take care of the denominator:
a * a 
so the denominator has just a real part (a^2)

after that we need to call __truediv__ on the following:
R_e(n*a, -n*b) and a * a
i.e. (n*a - n*be) / a*a

simplifying  a bit, we get:
real: n / a
dual: n*b / (a*a)

so we need to return R_e(n/a, (n*b) / (a*a))

1 / (1 + 10)
=>
R_e(1, -10 / 1)
👍

case 2:
seperate the denominator (allowed becuse a is a single number):
real: a / n
dual: b / n
return:
R_e(a / n, b / n)

case 3:
(a + be) / (c + de)
Once again, in order to get rid of the dual part in the denominator,
we need to multiply by the conjugate (of the denominator, that is (c - de))
(a + be) * (c - de) / ((c + de) * (c - de))
Let's look at just the numerator:
Simplifying a bit, we get (for the numerator):
(a * c) - (a * d)e
so for the numerator, we got:
R_e((a * c), -(a * d))

Now for the denominator:
c * c
Finally, we have:
R_e((a * c), -(a * d)) / (c*c)
whice is case 2 so call __truediv__ on the above.

(25 + 50e) / 25

(5 + 10e) / (5 - 10e)
numerator: (5 + 10e) * (5 + 10e) = 25 + 100e
denominator: (5 - 10e) * (5 + 10e) = 25 (real number)
(25 + 100e) / 25
1 + 4e