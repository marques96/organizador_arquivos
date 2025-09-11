import os
import shutil
import json
import logging


class Organizador:
    def __init__(self, path: str, config_file="config.json"):
        self.path = path
        self.config = self._carregar_config(config_file)
        self._setup_logger()

    def _carregar_config(self, config_file: str) -> dict:
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _setup_logger(self):
        logging.basicConfig(
            filename="logs/app.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def organizar(self):
        for arquivo in os.listdir(self.path):
            caminho_arquivo = os.path.join(self.path, arquivo)
            if os.path.isfile(caminho_arquivo):
                self._mover_arquivo(caminho_arquivo)

    def _mover_arquivo(self, caminho_arquivo: str):
        _, ext = os.path.splitext(caminho_arquivo)
        ext = ext.lower()

        destino = None
        for pasta, extensoes in self.config["rules"].items():
            if ext in extensoes:
                destino = os.path.join(self.path, pasta)
                break

        if not destino:
            destino = os.path.join(self.path, self.config["default_folder"])

        os.makedirs(destino, exist_ok=True)
        novo_caminho = os.path.join(destino, os.path.basename(caminho_arquivo))

        shutil.move(caminho_arquivo, novo_caminho)
        logging.info(f"Movido: {caminho_arquivo} -> {novo_caminho}")
