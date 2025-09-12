import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from threading import Thread
import time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizador.core import Organizador


class WatcherHandler(FileSystemEventHandler):
    def __init__(self, organizador, log_callback, progress_callback):
        self.organizador = organizador
        self.log_callback = log_callback
        self.progress_callback = progress_callback

    def on_created(self, event):
        if event.is_directory:
            return
        time.sleep(0.5)
        self.organizador._mover_arquivo(event.src_path)
        self.log_callback(f"📂 Novo arquivo movido: {os.path.basename(event.src_path)}")
        total = self.organizador.movidos or 1
        self.progress_callback((self.organizador.movidos / total) * 100)


class OrganizadorGUI:
    def __init__(self, master):
        self.master = master
        master.title("📦 Organizador de Arquivos")
        master.geometry("800x500")
        master.configure(bg="#f7f9fc")
        master.resizable(False, False)
        master.protocol("WM_DELETE_WINDOW", self.fechar_app)

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("TLabel", font=("Segoe UI", 10), background="#f7f9fc")

        # Cabeçalho
        header = tk.Label(
            master,
            text="📂 Organizador de Arquivos",
            font=("Segoe UI", 16, "bold"),
            bg="#f7f9fc",
            fg="#2c3e50",
        )
        header.pack(pady=10)

        # Seletor de pasta
        frame_path = tk.Frame(master, bg="#f7f9fc")
        frame_path.pack(pady=5)
        tk.Label(
            frame_path, text="Diretório alvo:", font=("Segoe UI", 10), bg="#f7f9fc"
        ).pack(side="left", padx=5)
        self.entry_path = tk.Entry(frame_path, width=60, font=("Segoe UI", 10))
        self.entry_path.pack(side="left", padx=5)
        ttk.Button(frame_path, text="📁 Escolher", command=self.escolher_pasta).pack(
            side="left"
        )

        # Botões de ação
        frame_buttons = tk.Frame(master, bg="#f7f9fc")
        frame_buttons.pack(pady=10)
        self.btn_organizar = ttk.Button(
            frame_buttons,
            text="⚡ Organizar (Manual)",
            command=self.iniciar_organizacao,
        )
        self.btn_organizar.grid(row=0, column=0, padx=10)
        self.btn_watch = ttk.Button(
            frame_buttons,
            text="👀 Iniciar Monitoramento",
            command=self.iniciar_monitoramento,
        )
        self.btn_watch.grid(row=0, column=1, padx=10)
        self.btn_stop = ttk.Button(
            frame_buttons,
            text="🛑 Parar Monitoramento",
            command=self.parar_monitoramento,
            state="disabled",
        )
        self.btn_stop.grid(row=0, column=2, padx=10)

        # Barra de progresso
        tk.Label(
            master, text="Progresso:", font=("Segoe UI", 10, "bold"), bg="#f7f9fc"
        ).pack()
        self.progress = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(master, maximum=100, variable=self.progress)
        self.progress_bar.pack(fill="x", padx=20, pady=5)

        # Área de logs
        tk.Label(
            master, text="Atividades:", font=("Segoe UI", 10, "bold"), bg="#f7f9fc"
        ).pack()
        self.log_area = scrolledtext.ScrolledText(
            master, width=90, height=15, state="disabled", font=("Consolas", 9)
        )
        self.log_area.pack(padx=20, pady=10)

        self.observer = None
        self.organizador = None

    # Funções utilitárias
    def escolher_pasta(self):
        path = filedialog.askdirectory()
        if path:
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, path)

    def log(self, msg):
        self.log_area.config(state="normal")
        self.log_area.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {msg}\n")
        self.log_area.see(tk.END)
        self.log_area.config(state="disabled")

    def update_progress(self, value):
        self.progress.set(value)

    # Organização manual
    def iniciar_organizacao(self):
        path = self.entry_path.get()
        if not path:
            messagebox.showwarning("⚠️ Atenção", "Selecione uma pasta primeiro!")
            return
        Thread(target=self.organizar_arquivos, args=(path,), daemon=True).start()

    def organizar_arquivos(self, path):
        self.disable_buttons()
        self.organizador = Organizador(path)

        arquivos = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        total = len(arquivos)
        if total == 0:
            self.log("⚠️ Nenhum arquivo encontrado para organizar.")
            messagebox.showinfo("Aviso", "Nenhum arquivo encontrado na pasta selecionada.")
            self.enable_buttons()
            return

        movidos_local = 0
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(path, arquivo)
            self.organizador._mover_arquivo(caminho_arquivo)
            movidos_local += 1
            self.log(f"✅ Movido: {arquivo}")
            self.update_progress((movidos_local / total) * 100)

        self.log(f"🎉 Organização concluída! {movidos_local} arquivo(s) movido(s).")
        messagebox.showinfo(
        "Concluído", f"Organização finalizada.\nArquivos movidos: {movidos_local}"
        )
        self.enable_buttons()
        self.progress.set(0)

    # Monitoramento
    def iniciar_monitoramento(self):
        path = self.entry_path.get()
        if not path:
            messagebox.showwarning("⚠️ Atenção", "Selecione uma pasta primeiro!")
            return

        self.disable_buttons()
        self.btn_stop.config(state="normal")
        self.organizador = Organizador(path)

        # Scan inicial
        self.organizar_arquivos(path)

        # Watchdog
        event_handler = WatcherHandler(self.organizador, self.log, self.update_progress)
        self.observer = Observer()
        self.observer.schedule(event_handler, path, recursive=False)
        self.observer.start()
        self.log(f"👀 Monitorando a pasta: {path}")

    def parar_monitoramento(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
            self.observer = None
            total_movidos = self.organizador.movidos if self.organizador else 0
            self.log(
                f"🛑 Monitoramento parado. Total de arquivos movidos: {total_movidos}"
            )
            messagebox.showinfo(
                "Parado",
                f"Monitoramento interrompido.\nArquivos movidos: {total_movidos}",
            )
            self.btn_stop.config(state="disabled")
            self.enable_buttons()

    # Controle de botões
    def disable_buttons(self):
        self.btn_organizar.config(state="disabled")
        self.btn_watch.config(state="disabled")

    def enable_buttons(self):
        self.btn_organizar.config(state="normal")
        self.btn_watch.config(state="normal")

    def fechar_app(self):
        if self.observer:
            self.observer.stop
            self.observer.join
        self.master.destroy()
