import io
import csv
from .export_strategy import ExportStrategy

class CsvExportStrategy(ExportStrategy):
    
    def export(self, data:list[dict[str,any]])->str:
        if not data:
            return ""
        
        output = io.StringIO()
        fieldnames = data[0].keys()
        write = csv.DictWriter(output, fieldnames=fieldnames)
        
        write.writeheader()
        write.writerows(data)
        
        return output.getvalue()
