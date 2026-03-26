from export_file import ExportFile
import json

class StrategyJson(ExportFile):
    
    def exportar(self, data: list[dict[str,any]])->str:
        return json.dumps(data, indent=4)