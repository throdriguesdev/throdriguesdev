import tkinter as tk
from tkinter import ttk, filedialog
import threading

class AplicativoEmail(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Envio Automatizado de E-mails")
        self.geometry("500x400")

        # Estilo temático
        style = ttk.Style()
        style.theme_use("clam")  # Você pode experimentar outros temas como "vista" ou "xpnative"

        # Diretório
        self.label_dir = ttk.Label(self, text="Selecione o diretório das planilhas:")
        self.label_dir.pack(pady=10)

        self.button_dir = ttk.Button(self, text="Selecionar Diretório", command=self.selecionar_diretorio)
        self.button_dir.pack(pady=10)

        # E-mails
        self.label_email = ttk.Label(self, text="Informe os e-mails dos destinatários (separados por vírgula):")
        self.label_email.pack(pady=10)

        self.entry_email = ttk.Entry(self)
        self.entry_email.pack(pady=10)

        # Botão para enviar e-mails
        self.button_enviar = ttk.Button(self, text="Enviar E-mails", command=self.enviar_emails_thread)
        self.button_enviar.pack(pady=20)

    def selecionar_diretorio(self):
        self.diretorio = filedialog.askdirectory()
        print(f"Diretório selecionado: {self.diretorio}")

    def enviar_emails(self):
        destinatarios = [email.strip() for email in self.entry_email.get().split(',')]
        print(f"E-mails dos destinatários: {destinatarios}")

        # Lógica para enviar e-mails aos destinatários
        for destinatario in destinatarios:
            print(f"Enviando e-mail para {destinatario}...")

    def enviar_emails_thread(self):
        # Utilizando threading para evitar que a interface congele durante o envio de e-mails
        thread = threading.Thread(target=self.enviar_emails)
        thread.start()

if __name__ == "__main__":
    app = AplicativoEmail()
    app.mainloop()
