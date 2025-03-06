from io import BytesIO
import zipfile

def extraction_all_zip(zip_content):
    """
    Recibe el contenido del ZIP como bytes y extrae el contenido de todos los 
    archivos .txt que encuentre. Retorna un string con la concatenación de 
    todos los TXT encontrados, o None si no encuentra ninguno.
    """
    textos = []
    with zipfile.ZipFile(BytesIO(zip_content)) as zip_file:
        for nombre_archivo in zip_file.namelist():
            if nombre_archivo.lower().endswith('.txt'):
                with zip_file.open(nombre_archivo) as txt_file:
                    data = txt_file.read()
                    # Intentamos decodificar con utf-8 y, si falla, probamos latin-1
                    try:
                        texto = data.decode('utf-8')
                    except UnicodeDecodeError:
                        texto = data.decode('latin-1', errors='ignore')
                    textos.append(texto)
    return "\n".join(textos) if textos else None