import tkinter as tk
from organizador.gui import OrganizadorGUI

def main():
    root = tk.Tk()
    app = OrganizadorGUI(root)

    # Intercepta o fechamento da janela para parar o watchdog
    def on_closing():
        app.fechar_app()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
