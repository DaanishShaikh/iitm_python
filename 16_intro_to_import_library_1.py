import math  # Importing the math module to use mathematical functions and constants.


def demo_math_library():
    # Constants
    print("math.pi:", math.pi)  # The mathematical constant pi (π), approximately 3.141592653589793
    print("math.e:", math.e)  # Euler's number (e), approximately 2.718281828459045
    print("math.tau:", math.tau)  # Tau (τ), which is 2π, approximately 6.283185307179586
    print("math.inf:", math.inf)  # Represents positive infinity
    print("math.nan:", math.nan)  # Represents 'Not a Number' (NaN), used for undefined values
    
    # Trigonometric Functions
    print("math.sin(0):", math.sin(0))  # Sine of 0 radians, result is 0.0
    print("math.cos(0):", math.cos(0))  # Cosine of 0 radians, result is 1.0
    print("math.tan(0):", math.tan(0))  # Tangent of 0 radians, result is 0.0
    print("math.asin(1):", math.asin(1))  # Inverse sine (arcsin) of 1, result is π/2 radians
    print("math.acos(1):", math.acos(1))  # Inverse cosine (arccos) of 1, result is 0 radians
    print("math.atan(1):", math.atan(1))  # Inverse tangent (arctan) of 1, result is π/4 radians
    print("math.atan2(1, 1):", math.atan2(1, 1))  # Computes arctan(y/x) while considering quadrants
    print("math.hypot(3, 4):", math.hypot(3, 4))  # Computes the hypotenuse of a right triangle with sides 3 and 4
    
    # Hyperbolic Functions
    print("math.sinh(0):", math.sinh(0))  # Hyperbolic sine of 0, result is 0.0
    print("math.cosh(0):", math.cosh(0))  # Hyperbolic cosine of 0, result is 1.0
    print("math.tanh(0):", math.tanh(0))  # Hyperbolic tangent of 0, result is 0.0
    print("math.asinh(0):", math.asinh(0))  # Inverse hyperbolic sine of 0, result is 0.0
    print("math.acosh(1):", math.acosh(1))  # Inverse hyperbolic cosine of 1, result is 0.0
    print("math.atanh(0):", math.atanh(0))  # Inverse hyperbolic tangent of 0, result is 0.0
    
    # Power and Logarithmic Functions
    print("math.exp(1):", math.exp(1))  # Computes e^1, result is Euler's number
    print("math.expm1(1):", math.expm1(1))  # Computes e^x - 1 more accurately for small x
    print("math.log(10):", math.log(10))  # Natural logarithm (base e) of 10
    print("math.log1p(1):", math.log1p(1))  # Computes log(1 + x) accurately for small x
    print("math.log2(8):", math.log2(8))  # Logarithm of 8 base 2, result is 3
    print("math.log10(100):", math.log10(100))  # Logarithm of 100 base 10, result is 2
    print("math.pow(2, 3):", math.pow(2, 3))  # Computes 2^3, result is 8
    print("math.sqrt(16):", math.sqrt(16))  # Square root of 16, result is 4
    
    # Number Theory and Rounding
    print("math.gcd(48, 18):", math.gcd(48, 18))  # Greatest common divisor (GCD) of 48 and 18, result is 6
    print("math.lcm(12, 15):", math.lcm(12, 15))  # Least common multiple (LCM) of 12 and 15, result is 60
    print("math.factorial(5):", math.factorial(5))  # Computes 5!, result is 120
    print("math.ceil(4.3):", math.ceil(4.3))  # Rounds 4.3 up to nearest integer, result is 5
    print("math.floor(4.7):", math.floor(4.7))  # Rounds 4.7 down to nearest integer, result is 4
    print("math.trunc(4.7):", math.trunc(4.7))  # Truncates 4.7 to an integer, result is 4
    print("math.fmod(10, 3):", math.fmod(10, 3))  # Computes remainder of 10/3 using floating-point division
    print("math.remainder(10, 3):", math.remainder(10, 3))  # Computes IEEE remainder of 10/3
    print("math.modf(4.7):", math.modf(4.7))  # Splits 4.7 into fractional and integer parts
    print("math.copysign(2, -3):", math.copysign(2, -3))  # Copies sign of -3 to 2, result is -2.0
    
    # Angle Conversion
    print("math.degrees(math.pi):", math.degrees(math.pi))  # Converts π radians to degrees, result is 180
    print("math.radians(180):", math.radians(180))  # Converts 180 degrees to radians, result is π
    
    # Special Functions
    print("math.erf(1):", math.erf(1))  # Error function value for 1
    print("math.erfc(1):", math.erfc(1))  # Complementary error function value for 1
    print("math.gamma(5):", math.gamma(5))  # Gamma function of 5 (equivalent to (5-1)!)
    print("math.lgamma(5):", math.lgamma(5))  # Logarithm of gamma function of 5
    
    # Checking Types
    print("math.isfinite(10):", math.isfinite(10))  # Checks if 10 is a finite number, result is True
    print("math.isinf(math.inf):", math.isinf(math.inf))  # Checks if value is infinity, result is True
    print("math.isnan(math.nan):", math.isnan(math.nan))  # Checks if value is NaN, result is True
    print("math.isclose(1.0001, 1.0002, rel_tol=1e-4):", math.isclose(1.0001, 1.0002, rel_tol=1e-4))  # Checks if numbers are close considering relative tolerance

# Call the function to see the output
demo_math_library()
