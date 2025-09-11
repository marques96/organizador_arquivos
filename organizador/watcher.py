from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from .core import Organizador


class Handler(FileSystemEventHandler):
    def __init__(self, path):
        self.organizador = Organizador(path)

    def on_created(self, event):
        if not event.is_directory:
            self.organizador.organizar()


class Monitor:
    def __init__(self, path):
        self.path = path
        self.observer = Observer()

    def start(self):
        event_handler = Handler(self.path)
        self.observer.schedule(event_handler, self.path, recursive=False)
        self.observer.start()
        print(f"Monitorando a pasta: {self.path}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
