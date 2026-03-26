import math

def mean(data):
    return sum(data) / len(data)

def median(data):
    data_sorted = sorted(data)
    n = len(data_sorted)
    mid = n // 2
    if n % 2 == 0:
        return (data_sorted[mid - 1] + data_sorted[mid]) / 2
    else:
        return data_sorted[mid]

def std_dev(data):
    m = mean(data)
    variance = sum((x - m) ** 2 for x in data) / len(data)
    return math.sqrt(variance)


