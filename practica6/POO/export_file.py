from abc import ABC, abstractmethod

class ExportFile(ABC):
    
    @abstractmethod
    def exportar(self, data:list[dict[str,any]])->str:
        ...