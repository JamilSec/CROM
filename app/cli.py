import os
import re
import datetime

from .scraper import extraction_all_zip
from .utils import convert_a_json

def leer_rucs_de_txt(ruta_txt):
    """
    Lee un archivo de texto donde cada línea es un RUC 
    y retorna una lista de strings (los RUCs).
    """
    rucs = []
    try:
        with open(ruta_txt, 'r', encoding='utf-8') as f:
            for linea in f:
                ruc = linea.strip()
                if ruc:
                    rucs.append(ruc)
    except Exception as e:
        print(f"Error al leer el archivo {ruta_txt}: {e}")
    return rucs

def run_cli_mode(file_path=None, output_path=None):
    """
    Modo CLI: Consulta los RUCs (desde archivo o lista por defecto),
    muestra en consola el contenido TXT original (con saltos de línea normalizados)
    y su conversión a JSON, y guarda el contenido TXT original normalizado
    en un archivo si se requiere.
    """
    if file_path:
        rucs = leer_rucs_de_txt(file_path)
        if not rucs:
            print("No se encontraron RUCs en el archivo. Abortando.")
            return
    else:
        rucs = [
            "20552103816", "20538856674", "20553856451", "20480316259",
            "20547825781", "20606106883", "20606422793", "20605100016",
            "20525994741", "20494156211", "20603049684", "20494074169",
            "20494100186", "20525926665", "20542259117", "20542245671",
        ]

    try:
        contenido_txt = extraction_all_zip(rucs)
        if not contenido_txt:
            print("No se encontró ningún archivo TXT en el ZIP.")
            return
    except Exception as e:
        print(f"Error durante la consulta de RUCs: {e}")
        return

    contenido_normalizado = re.sub(r'\n\s*\n+', '\n', contenido_txt)

    print("Contenido completo del TXT:")
    print(contenido_normalizado)
    resultado_json = convert_a_json(contenido_normalizado)
    print("\nResultado JSON:")
    print(resultado_json)

    if output_path:
        try:
            with open(output_path, "w", encoding="utf-8") as out:
                out.write(contenido_normalizado)
            print(f"\nResultado guardado en {output_path}")
        except Exception as e:
            print(f"Error al escribir el archivo {output_path}: {e}")
    else:
        results_dir = "results"
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        output_file = os.path.join(results_dir, file_name)
        try:
            with open(output_file, "w", encoding="utf-8") as out:
                out.write(contenido_normalizado)
            print(f"\nResultado guardado en {output_file}")
        except Exception as e:
            print(f"Error al escribir el archivo {output_file}: {e}")