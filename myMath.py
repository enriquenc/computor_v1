import math

def myPow(source, power):
    if power > 0:
        power -= 1
        source *= myPow(source, power)
    else:
        return 1
    return source

# Метод Ньютона, алгоритм Ньютона (также известный как метод касательных)
def mySqrt(source):
    halfSource = source / 2
    result = 0

    t = source / 2
    squareRoot = (t + (source / t)) / 2
    while (t - squareRoot) != 0:
        t = squareRoot
        squareRoot = (t + (source / t)) / 2
    return squareRoot
