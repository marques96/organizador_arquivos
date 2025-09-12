import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizador.core import Organizador


class WatcherHandler(FileSystemEventHandler):
    def __init__(self, organizador: Organizador):
        self.organizador = organizador

    def on_created(self, event):
        # Ignora diretórios
        if event.is_directory:
            return
        # Pequeno delay para garantir que o arquivo começou a ser copiado
        time.sleep(0.5)
        self.organizador._mover_arquivo(event.src_path)


def iniciar_watcher(path: str):
    organizador = Organizador(path)

    # 1️⃣ Scan inicial para organizar arquivos já existentes
    organizador.organizar()

    # 2️⃣ Inicia monitoramento
    event_handler = WatcherHandler(organizador)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print(f"\n👀 Monitorando a pasta: {path}\nPressione Ctrl+C para parar.\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Monitoramento interrompido pelo usuário.")
    observer.join()
