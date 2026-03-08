import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    y=np.array(x)
    y_exp=np.exp(-y)
    op=1/(1+y_exp)
    return op
    