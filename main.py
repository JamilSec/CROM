import argparse
import sys
import os

# Asegúrate de poder importar tus módulos de src
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import uvicorn
from app.cli import run_cli_mode
from app.api import app as fastapi_app

def run_api_mode(port):
    """
    Inicia la API de FastAPI en el puerto indicado.
    """
    print(f"Iniciando API local en el puerto {port}...")
    uvicorn.run("app.api:app", host="0.0.0.0", port=port, reload=True)

def main():
    parser = argparse.ArgumentParser(
        description="Aplicación para consultar múltiples RUCs: modo CLI o API local."
    )
    parser.add_argument(
        "--mode", choices=["cli", "api"],
        help="Modo de ejecución: 'cli' para procesar archivo TXT o 'api' para iniciar la API."
    )
    parser.add_argument(
        "--file", help="Ruta al archivo TXT con los RUCs (modo CLI)."
    )
    parser.add_argument(
        "--output", help="Ruta para guardar el resultado (modo CLI)."
    )
    parser.add_argument(
        "--port", type=int, default=8000,
        help="Puerto para iniciar la API (modo API). Por defecto es 8000."
    )
    args = parser.parse_args()

    if args.mode:
        if args.mode == "cli":
            run_cli_mode(file_path=args.file, output_path=args.output)
        elif args.mode == "api":
            run_api_mode(args.port)
    else:
        print("Seleccione el modo de ejecución:")
        print("1. Modo CLI (procesar archivo TXT y guardar o mostrar el resultado)")
        print("2. Iniciar API local")
        opcion = input("Ingrese 1 o 2: ").strip()

        if opcion == "1":
            file_path = input("Ingrese la ruta del archivo TXT con RUCs (deje vacío para usar valores por defecto): ").strip()
            output_path = input("Ingrese la ruta de salida para guardar el resultado (deje vacío para generar en 'results'): ").strip()
            run_cli_mode(file_path=file_path if file_path else None,
                         output_path=output_path if output_path else None)
        elif opcion == "2":
            puerto = input("Ingrese el puerto para la API (deje vacío para usar 8000): ").strip()
            run_api_mode(int(puerto) if puerto else 8000)
        else:
            print("Opción inválida. Saliendo.")

if __name__ == "__main__":
    main()