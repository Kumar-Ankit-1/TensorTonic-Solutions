import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    
    # Use np.isclose to handle floating-point precision issues
    if not np.isclose(np.sum(p), 1.0):
        # We raise the exception directly instead of catching it immediately
        raise ValueError("The probabilities in 'p' must sum to 1.")
        
    expected_value = np.sum(x * p)
    return expected_value
