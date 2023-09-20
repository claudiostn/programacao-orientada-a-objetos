from tkinter import *

root = Tk()
conteudo = Frame(root)
rotulo = Label(conteudo)
rotulo.configure(text="Eu sou um rótulo")
botao = Button(conteudo)
botao.configure(text="Hello, World!")
botao.configure(background="green")
rotulo.pack()
botao.pack()
conteudo.pack()

root.mainloop()