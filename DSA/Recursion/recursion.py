# Recursion is a technique where a function calls itself directly or indirectly to solve a problem.
# Each time the function calls itself, it works on a smaller subproblem,
# until it reaches a base case — a condition that stops further recursion.


def fabb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabb(n-1) + fabb(n-2)
    
    
print(fabb(6))