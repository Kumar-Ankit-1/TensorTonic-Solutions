import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x=np.array(x)
    neg=np.exp(-x)
    sig=1/(1+neg)
    swis=x*sig
    return swis