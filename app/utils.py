# utils.py
import csv
import io
import json
import re

def to_snake_case(text):
    """
    Convierte un texto a snake_case, eliminando acentos y caracteres especiales.
    """
    text = text.strip()
    replacements = {
        'ó': 'o', 'Ó': 'o',
        'ú': 'u', 'Ú': 'u',
        'á': 'a', 'Á': 'a',
        'é': 'e', 'É': 'e',
        'í': 'i', 'Í': 'i',
        'ñ': 'n', 'Ñ': 'n'
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    text = text.lower()
    text = re.sub(r'\W+', '_', text)
    return text.strip('_')

def convert_a_json(txt_data):
    """
    Convierte el contenido de un TXT separado por '|' a un JSON bien estructurado.
    Se asume que la primera línea contiene los encabezados.
    Los encabezados se convierten a snake_case y se genera una lista de diccionarios.
    """
    f = io.StringIO(txt_data)
    reader = csv.DictReader(f, delimiter='|')
    
    records = []
    for row in reader:
        if '' in row:
            del row['']
        new_row = {}
        for key, value in row.items():
            new_key = to_snake_case(key)
            new_row[new_key] = value.strip() if value else ""
        records.append(new_row)
    
    return json.dumps(records, ensure_ascii=False, indent=2)