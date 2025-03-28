import math
import math

def demo_math_library():
    # Constants
    print("math.pi:", math.pi)  # 3.141592653589793
    print("math.e:", math.e)  # 2.718281828459045
    print("math.tau:", math.tau)  # 6.283185307179586
    print("math.inf:", math.inf)  # inf
    print("math.nan:", math.nan)  # nan
    
    # Trigonometric Functions
    print("math.sin(0):", math.sin(0))  # 0.0
    print("math.cos(0):", math.cos(0))  # 1.0
    print("math.tan(0):", math.tan(0))  # 0.0
    print("math.asin(1):", math.asin(1))  # 1.5707963267948966
    print("math.acos(1):", math.acos(1))  # 0.0
    print("math.atan(1):", math.atan(1))  # 0.7853981633974483
    print("math.atan2(1, 1):", math.atan2(1, 1))  # 0.7853981633974483
    print("math.hypot(3, 4):", math.hypot(3, 4))  # 5.0
    
    # Hyperbolic Functions
    print("math.sinh(0):", math.sinh(0))  # 0.0
    print("math.cosh(0):", math.cosh(0))  # 1.0
    print("math.tanh(0):", math.tanh(0))  # 0.0
    print("math.asinh(0):", math.asinh(0))  # 0.0
    print("math.acosh(1):", math.acosh(1))  # 0.0
    print("math.atanh(0):", math.atanh(0))  # 0.0
    
    # Power and Logarithmic Functions
    print("math.exp(1):", math.exp(1))  # 2.718281828459045
    print("math.expm1(1):", math.expm1(1))  # 1.718281828459045
    print("math.log(10):", math.log(10))  # 2.302585092994046
    print("math.log1p(1):", math.log1p(1))  # 0.6931471805599453
    print("math.log2(8):", math.log2(8))  # 3.0
    print("math.log10(100):", math.log10(100))  # 2.0
    print("math.pow(2, 3):", math.pow(2, 3))  # 8.0
    print("math.sqrt(16):", math.sqrt(16))  # 4.0
    
    # Number Theory and Rounding
    print("math.gcd(48, 18):", math.gcd(48, 18))  # 6
    print("math.lcm(12, 15):", math.lcm(12, 15))  # 60
    print("math.factorial(5):", math.factorial(5))  # 120
    print("math.ceil(4.3):", math.ceil(4.3))  # 5
    print("math.floor(4.7):", math.floor(4.7))  # 4
    print("math.trunc(4.7):", math.trunc(4.7))  # 4
    print("math.fmod(10, 3):", math.fmod(10, 3))  # 1.0
    print("math.remainder(10, 3):", math.remainder(10, 3))  # -1.0
    print("math.modf(4.7):", math.modf(4.7))  # (0.7000000000000002, 4.0)
    print("math.copysign(2, -3):", math.copysign(2, -3))  # -2.0
    
    # Angle Conversion
    print("math.degrees(math.pi):", math.degrees(math.pi))  # 180.0
    print("math.radians(180):", math.radians(180))  # 3.141592653589793
    
    # Special Functions
    print("math.erf(1):", math.erf(1))  # 0.8427007929497149
    print("math.erfc(1):", math.erfc(1))  # 0.15729920705028513
    print("math.gamma(5):", math.gamma(5))  # 24.0
    print("math.lgamma(5):", math.lgamma(5))  # 3.1780538303479458
    
    # Checking Types
    print("math.isfinite(10):", math.isfinite(10))  # True
    print("math.isinf(math.inf):", math.isinf(math.inf))  # True
    print("math.isnan(math.nan):", math.isnan(math.nan))  # True
    print("math.isclose(1.0001, 1.0002, rel_tol=1e-4):", math.isclose(1.0001, 1.0002, rel_tol=1e-4))  # True