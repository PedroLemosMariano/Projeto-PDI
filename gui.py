import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np

from utils.io import carregar_imagem, salvar_imagem

imagem_original = None
imagem_processada = None
painel_imagem = None

def abrir_imagem():
    global imagem_original, imagem_processada, painel_imagem

    caminho = filedialog.askopenfilename()
    if not caminho:
        return

    imagem_original = carregar_imagem(caminho)
    imagem_processada = imagem_original.copy()

    exibir_imagem(imagem_processada)

def salvar_imagem_processada():
    global imagem_processada

    if imagem_processada is None:
        messagebox.showwarning("Aviso", "Nenhuma imagem processada para salvar.")
        return

    caminho = filedialog.asksaveasfilename(defaultextension=".png")
    if caminho:
        salvar_imagem(imagem_processada, caminho)

def exibir_imagem(imagem_cv):
    global painel_imagem

    imagem_rgb = cv2.cvtColor(imagem_cv, cv2.COLOR_BGR2RGB)
    imagem_pil = Image.fromarray(imagem_rgb)
    imagem_tk = ImageTk.PhotoImage(imagem_pil)

    if painel_imagem is None:
        painel_imagem = tk.Label(image=imagem_tk)
        painel_imagem.image = imagem_tk
        painel_imagem.pack()
    else:
        painel_imagem.configure(image=imagem_tk)
        painel_imagem.image = imagem_tk

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Editor de Imagens - PDI")
    janela.geometry("800x600")

    barra_menu = tk.Menu(janela)
    menu_arquivo = tk.Menu(barra_menu, tearoff=0)
    menu_arquivo.add_command(label="Abrir Imagem", command=abrir_imagem)
    menu_arquivo.add_command(label="Salvar Imagem", command=salvar_imagem_processada)
    menu_arquivo.add_separator()
    menu_arquivo.add_command(label="Sair", command=janela.quit)

    barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

    janela.config(menu=barra_menu)
    janela.mainloop()
