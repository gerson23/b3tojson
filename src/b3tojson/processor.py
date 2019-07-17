from b3tojson.data import Company, Stock
from typing import Dict

class FileHandle():
    filename = ""
    companies: {Company}

    def __init__(self, filename):
        self.filename = filename
        self.companies = {}
    
    def _process_raw_data(self, lines):
        lines = [line.strip() for line in lines]
        for line in lines:
            # HEADER -- just skipping it
            if line.startswith('00'):
                continue
            # COMPANY DATA
            elif line.startswith('01'):
                code = line[2:6]
                self.companies[code] = Company(code, line[6:66], line[66:78])
            # STOCK DATA
            elif line.startswith('02'):
                code = line[14:18]
                self.companies[code].add_stock(Stock(line[2:14], line[18:21], line[21:81]))
        
        print(self.companies['BIDI'])
    
    def analyze_file(self):
        try:
            with open(self.filename, "r", encoding="latin-1") as fd:
                lines = fd.readlines()
        except FileNotFoundError:
            print(f"Could not open file {self.filename}")
        except Exception:
            raise
        else:
            self._process_raw_data(lines)