from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from .services import consultar_rucs

app = FastAPI(
    title="API de Consulta Múltiple RUC",
    description="Expone un endpoint para consultar varios RUC y devolver la información en JSON.",
    version="1.0.0",
)

class RucsPayload(BaseModel):
    rucs: List[str]

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Consulta Múltiple RUC"}

@app.post("/consultar-rucs")
def consultar_rucs_endpoint(payload: RucsPayload):
    """
    Endpoint para consultar múltiples RUC.
    Envía un POST con un JSON así:
    {
        "rucs": ["20552103816", "20538856674", ...]
    }
    """
    try:
        resultado = consultar_rucs(payload.rucs)
        if not resultado:
            raise HTTPException(
                status_code=404, 
                detail="No se encontró contenido en el ZIP o no se halló link de descarga."
            )
        return {"data": resultado}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))