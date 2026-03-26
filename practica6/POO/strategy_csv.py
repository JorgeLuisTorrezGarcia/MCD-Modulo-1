from export_file import ExportFile
import csv
import io

class StrategyCsv(ExportFile):
    
    def exportar(self, data: list[dict[str, Any]]) -> str:
        
        if not data:
            return ""
        
        output = io.StringIO()
        fieldnames = data[0].keys()
        
        write = csv.DictWriter(output, fieldnames=fieldnames)
        write.writeheader()
        write.writerows(data)
        
        return output.getvalue()