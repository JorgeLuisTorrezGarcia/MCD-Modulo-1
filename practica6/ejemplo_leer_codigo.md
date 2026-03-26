
```python
import io
import csv
import json
from abc import ABC, abstractmethod
```

👉 En las primeras líneas se importan módulos:

* `io` para manejar flujos de texto en memoria.
* `csv` para trabajar con archivos CSV.
* `json` para convertir datos a formato JSON.
* `ABC` y `abstractmethod` desde `abc` para crear clases abstractas.

---

```python
class Estrategia(ABC):
```

👉 En esta línea se define una clase llamada `Estrategia` que hereda de `ABC`, lo que indica que es una clase abstracta.

---

```python
    @abstractmethod
    def mostrar_contenido(self, data:list[dict])->str:
        ...
```

👉 Aquí se declara un método abstracto llamado `mostrar_contenido`.

* Recibe un parámetro `data` que es una lista de diccionarios.
* Retorna un string.
* Al ser abstracto, obliga a las clases hijas a implementar este método.

---

```python
class EstrategiaJson(Estrategia):
```

👉 Se define una clase `EstrategiaJson` que hereda de `Estrategia`.

---

```python
    def mostrar_contenido(self, data:list[dict])->str:
        return json.dumps(data)
```

👉 En esta clase se implementa el método `mostrar_contenido`:

* Recibe la lista de diccionarios.
* Usa `json.dumps` para convertir los datos a formato JSON.
* Retorna ese resultado como string.

---

```python
class EstrategiaCsv(Estrategia):
```

👉 Se define otra clase llamada `EstrategiaCsv`, que también hereda de `Estrategia`.

---

```python
    def mostrar_contenido(self, data:list[dict])->str:
```

👉 Se implementa el método obligatorio `mostrar_contenido`.

---

```python
        if not data:
            ""
```

👉 Se evalúa si `data` está vacío.
⚠️ Sin embargo, aquí no se retorna nada, solo se escribe una cadena vacía, por lo que esta línea no tiene efecto.

---

```python
        output = io.StringIO()
```

👉 Se crea un objeto `StringIO` para manejar texto en memoria como si fuera un archivo.

---

```python
        fieldname = data[0].keys()
```

👉 Se obtienen las claves del primer diccionario de la lista para usarlas como encabezados del CSV.

---

```python
        write = csv.DictWriter(output, fieldnames=fieldname)
```

👉 Se crea un `DictWriter` que permitirá escribir diccionarios en formato CSV dentro de `output`.

---

```python
        write.writeheader()
```

👉 Se escribe la fila de encabezados en el CSV.

---

```python
        write.writerows(data)
```

👉 Se escriben todas las filas usando los diccionarios de la lista `data`.

---

```python
        return output.getvalue()
```

👉 Finalmente, se obtiene todo el contenido generado en `output` como un string y se retorna.

---

💡 Resumen general:
Se implementa el patrón de diseño *Strategy*, donde:

* `Estrategia` define una interfaz común.
* `EstrategiaJson` convierte datos a JSON.
* `EstrategiaCsv` convierte datos a CSV.
