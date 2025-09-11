import argparse
from organizador.core import Organizador
from organizador.watcher import Monitor


def main():
    parser = argparse.ArgumentParser(description="Organizador Automático de Arquivos")
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        required=True,
        help="Caminho da pasta a ser organizada",
    )
    parser.add_argument(
        "-w", "--watch", action="store_true", help="Ativar monitoramento em tempo real"
    )

    args = parser.parse_args()

    if args.watch:
        monitor = Monitor(args.path)
        monitor.start()
    else:
        organizador = Organizador(args.path)
        organizador.organizar()


if __name__ == "__main__":
    main()
