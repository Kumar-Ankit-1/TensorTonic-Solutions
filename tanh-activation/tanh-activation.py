import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    y=np.array(x)
    y_pos=np.exp(y)
    y_neg=np.exp(-y)
    tanhh=(y_pos-y_neg) / (y_pos+y_neg)
    return tanhh