# Consulta Múltiple RUC

Proyecto que implementa una API con FastAPI y un modo CLI para consultar múltiples RUCs.  
Incluye módulos para scraping, procesamiento de archivos ZIP y conversión de datos a JSON, con tests unitarios usando pytest.

## Tabla de Contenidos

- [Características](#caracter%C3%ADsticas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalaci%C3%B3n)
- [Uso](#uso)
  - [Modo API](#modo-api)
  - [Modo CLI](#modo-cli)
- [Tests](#tests)
- [Dependencias](#dependencias)
- [.gitignore](#gitignore)

## Características

- **API REST:** Permite consultar múltiples RUCs a través de un endpoint `/consultar-rucs`.
- **Modo CLI:** Proporciona una interfaz de línea de comandos para procesar un archivo de texto con RUCs y obtener resultados en formato TXT y JSON.
- **Scraping y Procesamiento:** Realiza peticiones a SUNAT, descarga un archivo ZIP y extrae los datos de archivos `.txt`.
- **Pruebas Unitarias:** Tests implementados con pytest para validar el funcionamiento de módulos clave como el scraping y el procesamiento.

## Estructura del Proyecto

```scss
consulta-multiple-ruc/
├── .gitignore
├── README.md
├── main.py
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── api.py
│   ├── cli.py
│   ├── config.py
│   ├── http_client.py
│   ├── processor.py
│   ├── scraper.py
│   ├── services.py
│   └── utils.py
└── tests
    ├── test_processor.py
    └── test_scraper.py
```

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/JamilSec/CROM.git
   cd CROM
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Modo API

Para iniciar la API localmente en el puerto 8000 (por defecto):

   ```bash
   python main.py --mode api --port 8000
   ```
> La API estará disponible en `http://localhost:8000` y puedes acceder a la documentación automática en `http://localhost:8000/docs`.

### Modo CLI

Para usar el modo CLI y procesar un archivo de texto con RUCs:

   ```bash
   python main.py --mode cli --file ruta_al_archivo.txt --output ruta_de_salida.txt
   ```

> Si no se indica un archivo, se utilizará una lista de RUCs por defecto. El resultado se mostrará en consola y se guardará en la carpeta `results` con un nombre basado en la fecha y hora actual si no se especifica la ruta de salida.

## Tests

Para ejecutar los tests unitarios, asegúrate de tener instalado `pytest` y luego corre:

   ```bash
   pytest
   ```

> Esto ejecutará los tests para el módulo `scraper` y `processor`, entre otros, verificando el correcto funcionamiento del proyecto.

## Dependencias

Las principales dependencias del proyecto son:

- `fastapi`: Para la definición de la API.
- `uvicorn`: Servidor ASGI para ejecutar FastAPI.
- `requests`: Para realizar peticiones HTTP.
- `beautifulsoup4`: Para parsear HTML y extraer enlaces.
- `pytest`: Para ejecutar pruebas unitarias.

Puedes instalar todas con:

   ```bash
   pip install fastapi uvicorn requests beautifulsoup4 pytest
   ```

## .gitignore

El repositorio incluye un archivo `.gitignore` para excluir archivos y carpetas innecesarias (entornos virtuales, archivos compilados, etc.). Consulta el archivo `.gitignore` para más detalles.