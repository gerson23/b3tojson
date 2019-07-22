from b3tojson import processor

def main():
    obj = processor.FileHandle("TITULOS_NEGOCIAVEIS_UTF8.TXT", 'stocks_data.json')
    obj.analyze_file()
    obj.save_json()