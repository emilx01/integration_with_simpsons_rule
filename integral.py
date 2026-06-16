import math

def exponential(x):
    return math.exp(x)

def integrate_exponential_rect(a, b, n):
    dx = (b-a)/n
    multiply = dx/3
    sigma = 0
    sigma += exponential(a) + exponential(b)
    for i in range(1, n):
        x = a+i*dx
        if i % 2 == 1:
            sigma += 4*exponential(x)
        else:
            sigma += 2*exponential(x)
    sigma = sigma * multiply
    return sigma

print(integrate_exponential_rect(2, 10, 4))
