from abc import ABC, abstractmethod

class ExportStrategy(ABC):
    """
    La interfaz de Estrategia declara operaciones comunes a todas las versiones
    soportadas de algún algoritmo. El Contexto utiliza esta interfaz para llamar
    al algoritmo definido por las Estrategias Concretas.
    """

    @abstractmethod
    def export(self, data: list[dict]) -> str:
        ... ## Implementar 
