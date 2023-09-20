from tkinter import *

class MainFrame:
    def __init__(self, root):
        self.conteudo = Frame(root)

        self.rotulo = Label(self.conteudo)
        self.rotulo.configure(text="0")

        self.botao = Button(self.conteudo)
        self.botao.configure(text="Incrementa", command=self.inc)
        self.botao.configure(background="green")

        self.menu_principal = Menu(root)

        self.menu_arquivo = Menu(self.menu_principal)
        self.menu_arquivo.add_command(label="Abrir")
        self.menu_arquivo.add_command(label="Salvar")

        self.menu_principal.add_cascade(label="Arquivo", menu=self.menu_arquivo)
        self.menu_principal.add_command(label="Ajuda")
        
        root.configure(menu=self.menu_principal)

        self.rotulo.pack(side="top", fill="both", expand=True)
        self.botao.pack(side="bottom", fill="both", expand=True)
        self.conteudo.pack(fill="both", expand=True)

    def inc(self):
        n = int(self.rotulo.configure("text")[4]) + 1
        self.rotulo.configure(text=str(n))

root = Tk()
app = MainFrame(root)
root.mainloop()