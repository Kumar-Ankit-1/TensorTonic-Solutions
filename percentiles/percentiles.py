import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    quan=[]
    x.sort()
    for i in range(len(q)):
        index=(len(x)-1)*(q[i]/100)
        lower=np.floor(index).astype('int')
        upper=np.ceil(index).astype('int')
        weight=index-lower
        quan.append(x[lower]+((x[upper]-x[lower])*weight))
    return np.array(quan)