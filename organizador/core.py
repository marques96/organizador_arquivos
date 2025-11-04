import os
import shutil
import logging
import json
import time
from pathlib import Path


class Organizador:
    def __init__(self, path: str, config_file: str = "config.json"):
        self.path = path
        self.movidos = 0
        self.config = self._carregar_config(config_file)
        self._setup_logger()

    def _setup_logger(self):
        logging.basicConfig(
            filename="logs/app.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def _carregar_config(self, config_file: str):
        if os.path.exists(config_file):
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logging.error(f"Erro ao carregar config.json: {e}")
        return {"rules": {}, "default_folder": "Outros"}

    def organizar(self):
        arquivos = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

        if not arquivos:
            print("Nenhum arquivo encontrado no diretório.")
            logging.info("Nenhum arquivo encontrado no diretório.")
            return

        print(f"Encontrados {len(arquivos)} arquivo(s) no diretório. Iniciando organização...\n")
        logging.info(f"{len(arquivos)} arquivo(s) encontrados no diretório {self.path}.")

        for arquivo in arquivos:
            caminho_arquivo = os.path.join(self.path, arquivo)
            self._mover_arquivo(caminho_arquivo)

        print(f"\nOrganização concluída! {self.movidos} arquivo(s) movido(s).")
        logging.info(f"Organização concluída! {self.movidos} arquivo(s) movido(s).")

    def _arquivo_pronto(self, caminho_arquivo: str, tentativas=3, intervalo=1) -> bool:
        """Verifica se o arquivo terminou de ser copiado verificando se o tamanho não muda."""
        for _ in range(tentativas):
            tamanho1 = os.path.getsize(caminho_arquivo)
            time.sleep(intervalo)
            tamanho2 = os.path.getsize(caminho_arquivo)
            if tamanho1 == tamanho2:
                return True
        return False

    def _mover_arquivo(self, caminho_arquivo: str):
        extensao = Path(caminho_arquivo).suffix.lower()
        pasta_destino = self._definir_pasta(extensao)
        pasta_completa = os.path.join(self.path, pasta_destino)
        os.makedirs(pasta_completa, exist_ok=True)
        nome_arquivo = os.path.basename(caminho_arquivo)

        # Verifica se o arquivo está pronto
        if not self._arquivo_pronto(caminho_arquivo):
            print(f"Arquivo ainda está sendo transferido: {nome_arquivo}")
            logging.warning(f"Arquivo ainda está sendo transferido: {caminho_arquivo}")
            return

        # Retry loop para mover
        tentativas = 5
        for i in range(tentativas):
            try:
                print(f"Movendo arquivo: {nome_arquivo} -> {pasta_completa}")
                shutil.move(caminho_arquivo, pasta_completa)
                self.movidos += 1
                logging.info(f"Arquivo movido: {caminho_arquivo} -> {pasta_completa}")
                break
            except PermissionError:
                time.sleep(5)  # espera 5 segundos e tenta de novo
            except Exception as e:
                logging.error(f"Erro ao mover arquivo {caminho_arquivo}: {e}")
                print(f"Erro ao mover {nome_arquivo}: {e}")
                break
        else:
            print(f"Não foi possível mover {nome_arquivo} após {tentativas} tentativas.")
            logging.warning(f"Não foi possível mover {caminho_arquivo} após {tentativas} tentativas.")

    def _definir_pasta(self, extensao: str) -> str:
        for pasta, extensoes in self.config.get("rules", {}).items():
            if extensao in extensoes:
                return pasta
        return self.config.get("default_folder", "Outros")