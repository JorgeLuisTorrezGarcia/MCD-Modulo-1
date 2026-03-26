import numpy as np

def calculate_statistics(data):
    """
    Calculate basic statistics for a given dataset.

    Parameters:
    data (list or np.array): The input dataset.

    Returns:
    dict: A dictionary containing mean, median, variance, and standard deviation.
    """
    
    data = np.array(data)
    
    statistics = {
        'mean': np.mean(data),
        'median': np.median(data),
        'variance': np.var(data, ddof=1),  # Sample variance
        'std_dev': np.std(data, ddof=1)     # Sample standard deviation
    }
    
    return statistics
