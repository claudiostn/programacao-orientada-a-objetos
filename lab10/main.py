from tkinter import *

class MainFrame:
    def __init__(self, root):
        self.conteudo = Frame(root, width=200, height=200)

        self.rotulo = Label(self.conteudo)
        self.rotulo.configure(text="0")

        self.rotulo_clica = Label(self.conteudo)
        self.rotulo_clica.configure(text="")

        self.botao = Button(self.conteudo)
        self.botao.configure(text="Incrementa", command=self.inc)
        self.botao.configure(background="green")

        self.menu_principal = Menu(root, tearoff=0)

        self.menu_arquivo = Menu(self.menu_principal, tearoff=0)
        self.menu_arquivo.add_command(label="Abrir", command=self.abrir)
        self.menu_arquivo.add_command(label="Salvar", command=self.salvar)

        self.menu_principal.add_cascade(label="Arquivo", menu=self.menu_arquivo)
        self.menu_principal.add_command(label="Ajuda", command=self.ajuda)
        
        self.menu_popup = Menu(root, tearoff=0)
        self.menu_popup.add_command(label="Alo", command=self.alo)
        self.menu_popup.add_command(label="Tchau", command=self.tchau)

        root.configure(menu=self.menu_principal)

        self.rotulo.pack(side="top")
        self.rotulo_clica.pack()
        self.botao.pack(side="bottom")
        self.conteudo.pack(fill="both", expand=True)
        self.conteudo.bind("<Button-3>", self.popup)
        self.conteudo.bind("<Button-1>", self.clica)

    def inc(self):
        n = int(self.rotulo.configure("text")[4]) + 1
        self.rotulo.configure(text=str(n))
    
    def abrir(self):
        print("Arquivo aberto")
    
    def salvar(self):
        print("Arquivo salvo")

    def ajuda(self):
        print("Ajuda")

    def alo(self):
        print("Alo!")

    def tchau(self):
        print("Tchau!")
    
    def popup(self, e):
        self.menu_popup.post(e.x_root, e.y_root)

    def clica(self, e):
        txt = "Mouse clicado em \n%d, %d"%(e.x,e.y)
        self.rotulo_clica.configure(text=txt)

root = Tk()
app = MainFrame(root)
root.mainloop()