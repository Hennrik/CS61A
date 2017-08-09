from operator import add, sub

# Question 01
def a_plus_abs_b(a, b):
    """Return a + abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

# Question 02
def two_of_three(a, b, c):
    """
    Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a ** 2 + b ** 2 + c ** 2 - min(a, b, c) ** 2

# Question 03
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    factor = n - 1
    while factor > 0:
        if n % factor == 0:
            return factor
        factor -= 1

# Question 04
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return False

def t():
    "*** YOUR CODE HERE ***"
    return 1 / 0

def f():
    "*** YOUR CODE HERE ***"
    return 1

# Question 05
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 1
    print(n)
    while(n != 1):
        if n % 2 == 0:
            n /= 2
            print(int(n))
        else:
            n = n * 3 + 1
            print(int(n))
        count += 1
    return count

# Question 06
def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    # lcm(a, b) = a * b / gcd(a, b)
    return int(a * b / gcd(a, b))

def gcd(a, b):
    """Returns the largest k that divides both m and n
    k, m, n are all positive integers.
    """
    if a % b == 0:
        return b
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(a - b, b)

# Question 07
def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    return len(set(str(n)))

# 
# def unique_digits(n):
#     """Return the number of unique digits in positive integer n
#
#     >>> unique_digits(8675309) # All are unique
#     7
#     >>> unique_digits(1313131) # 1 and 3
#     2
#     >>> unique_digits(13173131) # 1, 3, and 7
#     3
#     >>> unique_digits(10000) # 0 and 1
#     2
#     >>> unique_digits(101) # 0 and 1
#     2
#     >>> unique_digits(10) # 0 and 1
#     2
#     """
#     "*** YOUR CODE HERE ***"
#     count = 0
#     for i in range(10):
#         if has_digit(n, i):
#             count += 1
#     return count
#
#
#
# def has_digit(n, k):
#     """
#     Check whether number k is a digit of n.
#     >>> has_digit(1000, 0)
#     True
#     >>> has_digit(12345, 5)
#     True
#     >>> has_digit(244545, 1)
#     False
#     """
#     if n < 10:
#         return n == k
#     while n > 0:
#         n, last = n // 10, n % 10
#         if k == last:
#             return True
#     return False
