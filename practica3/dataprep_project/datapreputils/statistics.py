import math


def mean(data):
    
    if not data:
        print("No se puede calcular la media de una lista vacía")
    return sum(data) / len(data)


def median(data):
    
    if not data:
        print("No se puede calcular la mediana de una lista vacía")

    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


def std_dev(data):
    
    if not data or len(data) < 2:
        print("Se necesitan al menos 2 datos para calcular la desviación estándar")

    m = mean(data)
    variance = sum((x - m) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)


def mode(data):
    
    if not data:
        print("No se puede calcular la moda de una lista vacía")

    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    return max(frequency, key=frequency.get)


def harmonic_mean(data):
    
    if not data:
        print("No se puede calcular la media armónica de una lista vacía")

    if any(x == 0 for x in data):
        print("No se puede calcular la media armónica si hay valores cero")

    n = len(data)
    return n / sum(1 / x for x in data)


def geometric_mean(data):
    
    if not data:
        print("No se puede calcular la media geométrica de una lista vacía")

    if any(x <= 0 for x in data):
        print("Todos los valores deben ser positivos para calcular la media geométrica")

    product = 1
    for x in data:
        product *= x

    return product ** (1 / len(data))
