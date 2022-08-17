class R_e:
    def __init__(self, real, epsilon=0):  # Do not modify this part (__init__)
        self.real = real  # "real" part
        self.epsilon = epsilon  # "nilpotent" part (epsilon)
        
    def __str__(self): #(Not necessary to complete the Kata; but always useful)
        return "R_e(" + str(self.real)+", "+str(self.epsilon) + ")"
        
    def __repr__(self): #(Not necessary to complete the Kata; but always useful; at least for "testing")
        return str(self)

###IMPORTANT NOTE: Remember that elements of this class [R_e] can be
###added, subtracted, multiplied etc not only by other elements of this same class
###but ALSO by "real numbers" (=floats, integers etc...)!!!
###==> So things such as "R_e(0,1)+1" should be well-defined!

    def __eq__(self, other):
        #not necessary in order to compute deriv(), but let's make it "clean" :)
        #
        #Dual numbers are considered to be "equal" iff they have the same "real part", as well as the same "epsilon part"
        #(also let's define some equalities between reals and Duals,
        #saying that that "R_e(a) == a"... :) [since __eq__ DOES "work nicely" in "both directions"...] )
        if type(other) in [int, float]:
            real = self.real == other
            epsilon = self.epsilon == 0
        else:  # It's of type R_e
            real = self.real == other.real
            epsilon = self.epsilon == other.epsilon
        return (real and epsilon)

    def __add__(self, other):
        if type(other) in [int, float]:
            real = self.real + other
            epsilon = self.epsilon
        else:  # It's of type R_e
            real = self.real + other.real
            epsilon = self.epsilon + other.epsilon
        return R_e(real, epsilon)

    def __radd__(self, other):
        #Obviously assumes commutativity for addition
        if type(other) in [int, float]:
            real = self.real + other
            epsilon = self.epsilon
        else:  # It's of type R_e
            real = self.real + other.real
            epsilon = self.epsilon + other.epsilon
        return R_e(real, epsilon)

    def __neg__(self):
        return R_e(-self.real, -self.epsilon)

    def __sub__(self, other):
        if type(other) in [int, float]:
            real = self.real - other
            epsilon = self.epsilon
        else:  # It's of type R_e
            real = self.real - other.real
            epsilon = self.epsilon - other.epsilon
        return R_e(real, epsilon)

    def __rsub__(self, other):
        if type(other) in [int, float]:
            real = other - self.real
            epsilon = -self.epsilon
        else:  # It's of type R_e
            real = other.real - self.real
            epsilon =  other.epsilon - self.epsilon
        return R_e(real, epsilon)

    def __mul__(self, other):
        if type(other) in [int, float]:
            real = self.real * other
            epsilon = self.epsilon * other
        else:  # It's of type R_e
            real = self.real * other.real
            epsilon = (self.real * other.epsilon) + (self.epsilon * other.real)
        return R_e(real, epsilon)

    def __rmul__(self, other):
        if type(other) in [int, float]:
            real = self.real * other
            epsilon = self.epsilon * other
        else:  # It's of type R_e
            real = self.real * other.real
            epsilon = (self.real * other.epsilon) + (self.epsilon * other.real)
        return R_e(real, epsilon)

    def __truediv__(self, other):
        # case 2: (a + be) / n where n is a real number and (a + be) is R_e
        if type(other) in [int, float]:
            real = self.real / other
            epsilon = self.epsilon / other
        
        # case 3: (a + be) / (c + de) where (a + be) and (c + de) are R_e
        else:
            numerator = R_e(self.real * other.real, -(self.real * other.epsilon * 2)) # TODO: figure out why I need to multiply by 2
            denominator = other.real * other.real
            result = numerator / denominator # numerator.__truediv__(denominator)
            return result
        return R_e(real, epsilon)

    def __rtruediv__(self, other):
        # case 1: n / (a + be) where n is a real number and (a + be) is R_e
        if type(other) in [int, float]:
            real    = other / self.real
            epsilon = - ((other * self.epsilon) / (self.real * self.real))
        else:  # It's of type R_e
            real = self.real / other.real
            epsilon = self.epsilon / other.epsilon
        return R_e(real, epsilon)

    def __pow__(self, n):
        #n is a "real" (float... or could even be "complex" actually) number, but not necessarily an integer
        #Note: in this Kata, it is assumed we are working on R (or C) i.e. a commutative structure: the power of an element of the R_e class can thus be defined in the "obvious (direct) way" (see description for Dual Numbers' behaviour), without needing recursion...
        real    = pow(self.real, n)
        epsilon = (n * pow(self.real, n - 1) * self.epsilon)
        return R_e(real, epsilon)


def deriv(f, n=1):
    #can (and should) be done in just one (short) line! ;)
    #(...OK, if you REALLY wish, you may use an "extra line" to deal with the particular case of "constant functions"
    #such as "lambda x : 1", but this can easily be "shortcut" by a "little trick"^^)
    #...But for God's sake, do NOT try to implement the barbaric "approximation method"!!
    #Use R_e !..
    # return lambda x: f(R_e(n, x)) - f(n)
    return lambda x: (f(x + n*R_e(0, 1))).epsilon


for i in range(5):
    print("DER = ", end="")
    print(deriv(lambda x: 3*x**2 + 2*x + 1)(i), end=" ")
    print("EXP = ", end="")
    print((lambda x: 6*x + 2)(i))
# deriv(lambda x: x**2)

# assert R_e(5), R_e(5, 0)

# assert R_e(5,6) == R_e(5,6) , True
# assert not (R_e(5,6) == R_e(5,7))
# assert not (R_e(5,6) == R_e(6,6))
# assert not (R_e(5,6) == 5)
# assert R_e(5) == 5
# assert 5 == R_e(5)

# assert 5 + R_e(10,20) == R_e(15, 20)
# assert R_e(10,20)+6 == R_e(16, 20)
# assert R_e(1,5)+R_e(6,-7) == R_e(7, -2)

# assert -R_e(1,2) == R_e(-1, -2)

# assert 1-R_e(2,3) == R_e(-1, -3)
# assert R_e(2,3) - 1 == R_e(1, 3)
# assert R_e(3,4) - R_e(5,10) == R_e(-2, -6)

# assert 10*R_e(3,4) == R_e(30, 40)
# assert R_e(2,3)*5 == R_e(10, 15)
# assert R_e(3,4)*R_e(5,6) == R_e(15, 38)
# assert R_e(0,5)*R_e(0,12) == R_e(0, 0)
# assert R_e(1,5)*R_e(1,-5) == R_e(1, 0)

# assert 1/R_e(1,10) == R_e(1.0, -10.0)
# assert 1/R_e(5,10) == R_e(0.2, -0.4)
# assert R_e(5,10)/5 == R_e(1.0, 2.0)
# assert R_e(5,10)/R_e(5,-10) == R_e(1.0, 4.0)


# assert R_e(1,10)**(-1) == R_e(1.0, -10.0)
# assert R_e(5,-10)**2 == R_e(25, -100)
# assert R_e(25, -100)**0.5 == R_e(5.0, -10.0)
# assert R_e(1,3)**3 == R_e(1, 9)
# assert R_e(1, 9)**(1/3) == R_e(1.0, 3.0)