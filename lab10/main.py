from tkinter import *

root = Tk()
conteudo = Frame(root)
botao = Button(conteudo)
botao.configure(text="Hello, World!")
botao.configure(background="green")
botao.pack()
conteudo.pack()

root.mainloop()