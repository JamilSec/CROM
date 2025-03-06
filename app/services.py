import json
from .scraper import get_txt_ruc
from .utils import convert_a_json

def consultar_rucs(ruc_list):
    """
    Lógica central para consultar varios RUCs:
      1) Llama a get_txt_ruc(ruc_list)
      2) Convierte el contenido a JSON
      3) Retorna un objeto Python (lista de dicts) listo para usarse.
    """
    contenido_txt = get_txt_ruc(ruc_list)

    if not contenido_txt:
        return []
    json_str = convert_a_json(contenido_txt)
    return json.loads(json_str)