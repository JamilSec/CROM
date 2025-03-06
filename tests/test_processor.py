import io
import zipfile
import pytest

from app.processor import extraction_all_zip

def create_test_zip(txt_files):
    """
    Crea un ZIP en memoria a partir de un diccionario donde las claves son
    los nombres de archivo y los valores el contenido del archivo.
    """
    mem_zip = io.BytesIO()
    with zipfile.ZipFile(mem_zip, mode="w") as zf:
        for filename, content in txt_files.items():
            zf.writestr(filename, content)
    mem_zip.seek(0)
    return mem_zip.read()

def test_extraer_txt_single_file():
    contenido = "Este es un archivo de prueba."
    zip_bytes = create_test_zip({"archivo.txt": contenido})
    resultado = extraction_all_zip(zip_bytes)
    assert contenido in resultado

def test_extraer_txt_multiple_files():
    contenido1 = "Contenido del primer archivo."
    contenido2 = "Contenido del segundo archivo."
    zip_bytes = create_test_zip({
        "archivo1.txt": contenido1,
        "archivo2.txt": contenido2,
    })
    resultado = extraction_all_zip(zip_bytes)
    assert contenido1 in resultado
    assert contenido2 in resultado

def test_extraer_txt_sin_archivos_txt():
    zip_bytes = create_test_zip({"archivo.csv": "dato1,dato2"})
    resultado = extraction_all_zip(zip_bytes)
    assert resultado is None
