# Sistema de Consulta de Autos

## Descripción General

Herramienta de consola para que el gerente de la empresa de alquiler de autos pueda consultar información sobre el inventario, precios y disponibilidad de vehículos.

## Características

La aplicación permite realizar las siguientes consultas:

1. **Autos disponibles**: Visualizar todos los modelos de autos con sus unidades disponibles
2. **Costo de alquiler**: Obtener el costo diario de alquiler de un modelo específico
3. **Verificar existencia**: Consultar si un modelo de auto existe en la empresa
4. **Cantidad total**: Conocer el número total de autos que posee la empresa

## Funciones Principales

### `obtener_autos_disponibles()`
Retorna la lista de todos los modelos de autos disponibles.

```python
autos = obtener_autos_disponibles()
# Retorna: ['Toyota Corolla', 'Hyundai Tucson', 'Kia Rio', 'Nissan Versa', 'Suzuki Swift']
```

### `obtener_costo_alquiler(modelo_auto)`
Obtiene el costo diario de alquiler para un modelo específico.

**Parámetros:**
- `modelo_auto` (str): Nombre del modelo de auto

**Retorna:**
- `int`: Costo diario si existe el auto
- `None`: Si el auto no existe

```python
costo = obtener_costo_alquiler("Toyota Corolla")
# Retorna: 45
```

### `auto_existe(modelo_auto)`
Verifica si un modelo existe en el inventario.

**Parámetros:**
- `modelo_auto` (str): Nombre del modelo de auto

**Retorna:**
- `bool`: True si existe, False en caso contrario

```python
existe = auto_existe("Honda Civic")
# Retorna: False
```

### `obtener_cantidad_total_autos()`
Calcula la cantidad total de autos en la empresa.

**Retorna:**
- `int`: Suma total de todas las unidades

```python
total = obtener_cantidad_total_autos()
# Retorna: 25
```

## Cómo Usar

### Ejecución de la Aplicación

Desde la terminal, en el directorio raíz del proyecto:

```bash
python -m src.main
```

### Interfaz de Consola

Una vez iniciada, la aplicación mostrará un menú interactivo:

```
============================================================
SISTEMA DE CONSULTA DE AUTOS - GERENCIA DE ALQUILERES
============================================================
1. Ver autos disponibles para alquilar
2. Consultar costo de alquiler de un auto
3. Verificar si un auto existe
4. Ver cantidad total de autos
5. Salir
============================================================

Ingrese una opción (1-5):
```

Seleccione la opción con el número correspondiente y siga las instrucciones.

## Inventario de Autos

### Modelos Disponibles

| Modelo | Unidades | Costo Diario |
|--------|----------|-------------|
| Toyota Corolla | 5 | $45 |
| Hyundai Tucson | 3 | $70 |
| Kia Rio | 7 | $40 |
| Nissan Versa | 4 | $42 |
| Suzuki Swift | 6 | $38 |

**Total de autos:** 25 unidades

## Requisitos

- Python 3.6 o superior
- No requiere librerías externas

