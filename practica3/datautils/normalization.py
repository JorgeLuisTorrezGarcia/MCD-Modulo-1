def min_max(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def z_score(data, mean, std):
    return [(x - mean) / std for x in data]