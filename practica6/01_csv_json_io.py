import io
import csv
import json
from abc import ABC, abstractmethod

class Estrategia(ABC):
    
    @abstractmethod
    def mostrar_contenido(self, data:list[dict])->str:
        ...
        
class EstrategiaJson(Estrategia):
    
    def mostrar_contenido(self, data:list[dict])->str:
        return json.dumps(data, indent=4)
    
    
class EstrategiaCsv(Estrategia):
    
    def mostrar_contenido(self, data:list[dict])->str:
        
        if not data:
            return ""
        
        output = io.StringIO()
        fieldname = data[0].keys()
        
        write = csv.DictWriter(output, fieldnames=fieldname)
        write.writeheader()
        write.writerows(data)
        
        return output.getvalue()