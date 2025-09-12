import argparse
from organizador.core import Organizador
from organizador.watcher import iniciar_watcher

def main():
    parser = argparse.ArgumentParser(description="Organizador de arquivos")
    parser.add_argument("-p", "--path", required=True, help="Caminho da pasta a organizar")
    parser.add_argument("-w", "--watch", action="store_true", help="Monitorar a pasta em tempo real")
    args = parser.parse_args()

    if args.watch:
        # Organiza arquivos existentes + monitora novos
        iniciar_watcher(args.path)
    else:
        # Apenas organiza arquivos existentes uma vez
        organizador = Organizador(args.path)
        organizador.organizar()

if __name__ == "__main__":
    main()
