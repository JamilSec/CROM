import io
import zipfile
import pytest

from app import scraper

class DummyResponse:
    def __init__(self, text="", content=b""):
        self.text = text
        self.content = content

    def raise_for_status(self):
        pass

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

def dummy_get(url, **kwargs):
    """
    Función dummy para simular HttpClient.get.
    Si se solicita el ZIP (dummy_zip_url), retorna un DummyResponse con un ZIP válido.
    """
    if "dummy_zip_url" in url:
        zip_content = create_test_zip({"test.txt": "Contenido de prueba."})
        return DummyResponse(content=zip_content)
    return DummyResponse(text="Dummy response")

def dummy_post(url, data=None, **kwargs):
    """
    Función dummy para simular HttpClient.post.
    Retorna un DummyResponse con un HTML que contiene el enlace de descarga.
    """
    dummy_html = '<html><body><a href="http://dummy_zip_url/archivo.zip">descargar</a></body></html>'
    return DummyResponse(text=dummy_html)

class DummyHttpClient:
    def get(self, url, **kwargs):
        return dummy_get(url, **kwargs)
    
    def post(self, url, data=None, **kwargs):
        return dummy_post(url, data=data, **kwargs)

def test_obtener_txt_multiples_ruc(monkeypatch):
    """
    Test para la función obtener_txt_multiples_ruc del scraper.
    Se reemplaza HttpClient por una versión dummy para simular la respuesta.
    """
    # Patch al constructor de HttpClient para que retorne nuestra versión dummy
    monkeypatch.setattr(scraper, "HttpClient", lambda: DummyHttpClient())
    
    resultado = scraper.get_txt_ruc(["20552103816"])
    assert "Contenido de prueba." in resultado