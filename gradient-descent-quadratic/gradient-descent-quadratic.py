def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x=x0
    # Write code here
    for i in range(steps):
        f_x=(a*(x**2)) + (b*x) + c
        fd_x=2*a*x + b
        x=x - (lr*fd_x)
    return x
    