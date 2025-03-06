from bs4 import BeautifulSoup

from .http_client import HttpClient
from .processor import extraction_all_zip
from .config import SUNAT_URL_INICIAL, SUNAT_TOKEN

def get_txt_ruc(ruc_list):
    """
    - Crea la sesión (HttpClient).
    - Hace la primera petición para cookies/tokens.
    - Envía el POST con la lista de RUCs.
    - Parsea el HTML para obtener la URL del ZIP.
    - Descarga el ZIP y extrae el contenido TXT usando la función de processor.
    Retorna el contenido de todos los .txt concatenados.
    """
    client = HttpClient()
    client.get(SUNAT_URL_INICIAL)

    data_payload = [
        ('accion', 'consManual'),
        ('token', SUNAT_TOKEN),
        ('txtRuc', ''),
    ]
    for ruc in ruc_list:
        data_payload.append(('selRuc', ruc))

    resp_post = client.post(SUNAT_URL_INICIAL, data=data_payload)

    soup = BeautifulSoup(resp_post.text, "html.parser")
    link_descarga = soup.find("a", href=lambda h: h and "descargaArchivoAlias" in h)
    if not link_descarga:
        raise ValueError("No se encontró enlace de descarga en la respuesta.")

    url_zip = link_descarga['href']
    resp_zip = client.get(url_zip)
    contenido_txt = extraction_all_zip(resp_zip.content)
    return contenido_txt