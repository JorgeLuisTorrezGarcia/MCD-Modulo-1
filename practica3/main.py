from datautils import mean, median, std_dev, min_max, z_score

data = [10, 20, 28, 40, 50]
print("Datos:", data)

m = mean(data)
med = median(data)
std = std_dev(data)

print("Media:", m)
print("Mediana:", med)  
print("Desviación estándar:", std)

print("Normalización Min-Max:", min_max(data))
print("Normalización Z-Score:", z_score(data, m, std))

