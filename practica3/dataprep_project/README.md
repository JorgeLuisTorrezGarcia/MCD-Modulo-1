# DataPrepUtils - Paquete de Preparación de Datos

# Integrantes:
- Porfirio Yupanqui Mamani
- Andrea Elizabeth Arana Ore
- Jorge Luis Torrez Garcia
- Bruno Alex Mendoza Teodovich
- Johann Quispe

## Descripción del Proyecto

**DataPrepUtils** es un paquete de Python reutilizable diseñado para facilitar las tareas más comunes en la preparación y transformación de datos para proyectos de Ciencia de Datos. El paquete proporciona funciones optimizadas y bien documentadas para limpieza, normalización y análisis estadístico de datos.

## Objetivo

El objetivo de este proyecto es proporcionar a los científicos de datos y desarrolladores una librería modular y fácil de usar que contenga funcionalidades esenciales para la etapa de preparación de datos, que es una de las más críticas en cualquier proyecto de análisis o machine learning.

## Características Principales

### 1. **Módulo de Estadística** (`statistics.py`)
Cálculo de métricas estadísticas comunes:
- **Media aritmética**: Promedio simple de los datos
- **Mediana**: Valor central del conjunto ordenado
- **Desviación estándar**: Medida de dispersión de los datos
- **Moda**: Valor más frecuente en los datos
- **Media armónica**: Promedio adecuado para datos de tasas
- **Media geométrica**: Promedio para datos con crecimiento exponencial

### 2. **Módulo de Normalización** (`normalization.py`)
Escalado y normalización de datos:
- **Min-Max**: Escala los datos al rango [0, 1]
- **Z-Score**: Estandariza los datos alrededor de 0 con desviación estándar 1

### 3. **Módulo de Limpieza** (`cleaning.py`)
Preparación y limpieza de datos:
- **Eliminar valores nulos**: Remueve los valores None
- **Reemplazar valores faltantes**: Sustituye None con un valor específico
- **Reemplazar con media**: Llena valores nulos con la media de los datos
- **Eliminar duplicados**: Remueve valores repetidos manteniendo el orden

## Estructura del Proyecto

```
dataprep_project/
│
├── main.py                          # Script de demostración
├── requirements.txt                 # Dependencias del proyecto
├── README.md                        # Este archivo
│
└── datapreputils/                   # Paquete principal
    ├── __init__.py                  # Inicializador del paquete
    ├── cleaning.py                  # Funciones de limpieza
    ├── normalization.py             # Funciones de normalización
    └── statistics.py                # Funciones estadísticas
```

## Requisitos del Sistema

- **Python**: 3.7 o superior
- **Dependencias**: Ninguna dependencia externa requerida (solo librerías estándar de Python)

## Instalación

### Opción 1: Usar el paquete desde el proyecto actual

1. Clona o descarga el proyecto
2. Navega a la carpeta del proyecto:
```bash
cd dataprep_project
```

### Opción 2: Instalar como paquete

Si deseas instalar el paquete de manera global:
```bash
pip install -e .
```

## Uso

### Uso Básico

```python
from datapreputils import mean, median, std_dev, min_max, remove_nulls

# Datos de ejemplo
data = [10, 20, 30, 40, 50]

# Estadísticas
promedio = mean(data)
mediana = median(data)
desv_estandar = std_dev(data)

# Normalización
datos_normalizados = min_max(data)

# Limpieza
datos_con_nulos = [10, None, 30, None, 50]
datos_limpios = remove_nulls(datos_con_nulos)
```

### Ejemplo Completo

Para ver un ejemplo completo de uso del paquete, ejecuta:

```bash
python main.py
```

Este script demuestra:
1. Cálculo de estadísticas
2. Normalización de datos
3. Limpieza de datos
4. Un pipeline integrado de preparación de datos

### Funciones Disponibles

#### Estadísticas
- `mean(data)` - Media aritmética
- `median(data)` - Mediana
- `std_dev(data)` - Desviación estándar
- `mode(data)` - Moda
- `harmonic_mean(data)` - Media armónica
- `geometric_mean(data)` - Media geométrica

#### Normalización
- `min_max(data)` - Normalización Min-Max a [0, 1]
- `z_score(data, mean=None, std=None)` - Estandarización Z-Score

#### Limpieza
- `remove_nulls(data)` - Elimina valores None
- `replace_missing_values(data, valor)` - Reemplaza None con un valor
- `replace_missing_with_mean(data)` - Reemplaza None con la media
- `remove_duplicates(data, keep_order=True)` - Elimina duplicados

### Ejemplos de Uso por Funcionalidad

#### Estadísticas
```python
from datapreputils import mean, harmonic_mean, geometric_mean

datos = [2, 4, 6, 8, 10]

print(mean(datos))              # 6.0
print(harmonic_mean(datos))     # 4.32...
print(geometric_mean(datos))    # 5.17...
```

#### Normalización
```python
from datapreputils import min_max, z_score

datos = [10, 20, 30, 40]

# Min-Max: escalado a [0, 1]
normalizados = min_max(datos)
print(normalizados)  # [0.0, 0.333..., 0.666..., 1.0]

# Z-Score: estandarización
estandarizados = z_score(datos)
print(estandarizados)  # [-1.161..., -0.387..., 0.387..., 1.161...]
```

#### Limpieza
```python
from datapreputils import remove_nulls, replace_missing_with_mean

datos_incompletos = [10, None, 30, None, 50]

# Opción 1: Eliminar nulos
limpios = remove_nulls(datos_incompletos)
print(limpios)  # [10, 30, 50]

# Opción 2: Llenar con la media
completados = replace_missing_with_mean(datos_incompletos)
print(completados)  # [10, 30.0, 30, 30.0, 50]
```

## Documentación de Funciones

Todas las funciones incluyen docstrings detallados. Para más información sobre una función específica:

```python
from datapreputils import mean
help(mean)
```

## Pipeline de Datos Recomendado

1. **Exploración Inicial**: Examina tus datos
2. **Limpieza**: Elimina duplicados y maneja valores faltantes
3. **Transformación**: Normaliza o estandariza según sea necesario
4. **Análisis**: Calcula estadísticas descriptivas
5. **Modelado**: Usa los datos preparados en tu modelo

## Contribuciones

Este proyecto fue desarrollado como parte de un ejercicio académico. Las sugerencias y mejoras son bienvenidas.

### Procesamiento de Conjunto de Datos Completo

```python
from datapreputils import *

# Datos crudos con problemas comunes
datos_crudos = [100, None, 150, 150, 200, None, 250, 300]

# Paso 1: Llenar valores nulos
datos = replace_missing_with_mean(datos_crudos)

# Paso 2: Eliminar duplicados
datos = remove_duplicates(datos)

# Paso 3: Analizar
print(f"Media: {mean(datos):.2f}")
print(f"Mediana: {median(datos):.2f}")

# Paso 4: Normalizar
datos_normalizados = z_score(datos)
print(f"Datos normalizados: {datos_normalizados}")
```

