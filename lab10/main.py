from tkinter import *

class MainFrame:
    def __init__(self, root):
        self.conteudo = Frame(root)

        self.rotulo = Label(self.conteudo)
        self.rotulo.configure(text="Eu sou um rótulo")

        self.botao = Button(self.conteudo)
        self.botao.configure(text="Hello, World!")
        self.botao.configure(background="green")

        self.rotulo.pack()
        self.botao.pack()
        self.conteudo.pack()

root = Tk()
app = MainFrame(root)
root.mainloop()