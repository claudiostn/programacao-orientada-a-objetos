from tkinter import *

class MainFrame:
    def __init__(self, root):
        self.conteudo = Frame(root)

        self.rotulo = Label(self.conteudo)
        self.rotulo.configure(text="Eu sou um rótulo")

        self.botao = Button(self.conteudo)
        self.botao.configure(text="Hello, World!")
        self.botao.configure(background="green")

        self.menu_principal = Menu(root)

        self.menu_arquivo = Menu(self.menu_principal)
        self.menu_arquivo.add_command(label="Abrir")
        self.menu_arquivo.add_command(label="Salvar")
        
        self.menu_principal.add_cascade(label="Arquivo", menu=self.menu_arquivo)
        self.menu_principal.add_command(label="Ajuda")
        
        root.configure(menu=self.menu_principal)

        self.rotulo.pack()
        self.botao.pack()
        self.conteudo.pack()

root = Tk()
app = MainFrame(root)
root.mainloop()