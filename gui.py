import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

from utils.io import carregar_imagem, salvar_imagem
from processamento import histograma, intensidade, filtros, fourier, morfologia, segmentacao

imagem_original = None
imagem_processada = None
painel_imagem = None

def abrir_imagem():
    global imagem_original, imagem_processada
    caminho = filedialog.askopenfilename()
    if caminho:
        imagem_original = carregar_imagem(caminho)
        imagem_processada = imagem_original.copy()
        exibir_imagem(imagem_processada)

def salvar_imagem_processada():
    if imagem_processada is None:
        messagebox.showwarning("Aviso", "Nenhuma imagem processada.")
        return
    caminho = filedialog.asksaveasfilename(defaultextension=".png")
    if caminho:
        salvar_imagem(imagem_processada, caminho)

def exibir_imagem(imagem_cv):
    global painel_imagem
    imagem_rgb = cv2.cvtColor(imagem_cv, cv2.COLOR_GRAY2RGB)
    imagem_pil = Image.fromarray(imagem_rgb)
    imagem_tk = ImageTk.PhotoImage(imagem_pil)

    if painel_imagem is None:
        painel_imagem = tk.Label(image=imagem_tk)
        painel_imagem.image = imagem_tk
        painel_imagem.pack()
    else:
        painel_imagem.configure(image=imagem_tk)
        painel_imagem.image = imagem_tk

# -------------------- Funções de Processamento --------------------

def aplicar(func):
    global imagem_processada
    if imagem_processada is None:
        messagebox.showwarning("Aviso", "Abra uma imagem primeiro.")
        return
    imagem_processada = func(imagem_processada)
    exibir_imagem(imagem_processada)

def mostrar_histograma():
    if imagem_processada is None:
        messagebox.showwarning("Aviso", "Abra uma imagem primeiro.")
        return
    histograma.calcular_histograma(imagem_processada)

def mostrar_fourier():
    if imagem_processada is None:
        messagebox.showwarning("Aviso", "Abra uma imagem primeiro.")
        return
    fourier.espectro_fourier(imagem_processada)

# -------------------- Interface --------------------

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Editor de Imagens - PDI")
    janela.geometry("800x600")

    menu = tk.Menu(janela)

    # Menu Arquivo
    menu_arquivo = tk.Menu(menu, tearoff=0)
    menu_arquivo.add_command(label="Abrir Imagem", command=abrir_imagem)
    menu_arquivo.add_command(label="Salvar Imagem", command=salvar_imagem_processada)
    menu_arquivo.add_separator()
    menu_arquivo.add_command(label="Sair", command=janela.quit)
    menu.add_cascade(label="Arquivo", menu=menu_arquivo)

    # Menu Histograma
    menu_hist = tk.Menu(menu, tearoff=0)
    menu_hist.add_command(label="Exibir Histograma", command=mostrar_histograma)
    menu_hist.add_command(label="Equalização de Histograma", command=lambda: aplicar(histograma.equalizar_histograma))
    menu.add_cascade(label="Histograma", menu=menu_hist)

    # Menu Intensidade
    menu_intensidade = tk.Menu(menu, tearoff=0)
    menu_intensidade.add_command(label="Alargamento de Contraste", command=lambda: aplicar(intensidade.alargamento_contraste))
    menu_intensidade.add_command(label="Negativo", command=lambda: aplicar(intensidade.negativo))
    menu.add_cascade(label="Intensidade", menu=menu_intensidade)

    # Menu Filtros
    menu_filtros = tk.Menu(menu, tearoff=0)
    menu_filtros.add_command(label="Média", command=lambda: aplicar(filtros.filtro_media))
    menu_filtros.add_command(label="Mediana", command=lambda: aplicar(filtros.filtro_mediana))
    menu_filtros.add_command(label="Gaussiano", command=lambda: aplicar(filtros.filtro_gaussiano))
    menu_filtros.add_command(label="Máximo", command=lambda: aplicar(filtros.filtro_maximo))
    menu_filtros.add_command(label="Mínimo", command=lambda: aplicar(filtros.filtro_minimo))
    menu_filtros.add_separator()
    menu_filtros.add_command(label="Laplaciano", command=lambda: aplicar(filtros.filtro_laplaciano))
    menu_filtros.add_command(label="Roberts", command=lambda: aplicar(filtros.filtro_roberts))
    menu_filtros.add_command(label="Prewitt", command=lambda: aplicar(filtros.filtro_prewitt))
    menu_filtros.add_command(label="Sobel", command=lambda: aplicar(filtros.filtro_sobel))
    menu.add_cascade(label="Filtros", menu=menu_filtros)

    # Menu Fourier
    menu_fourier = tk.Menu(menu, tearoff=0)
    menu_fourier.add_command(label="Ver Espectro de Fourier", command=mostrar_fourier)
    menu_fourier.add_command(label="Filtro Passa-Baixa", command=lambda: aplicar(lambda img: fourier.filtro_freq(img, tipo="passa-baixa", raio=30)))
    menu_fourier.add_command(label="Filtro Passa-Alta", command=lambda: aplicar(lambda img: fourier.filtro_freq(img, tipo="passa-alta", raio=30)))
    menu.add_cascade(label="Fourier", menu=menu_fourier)

    # Menu Morfologia
    menu_morf = tk.Menu(menu, tearoff=0)
    menu_morf.add_command(label="Erosão", command=lambda: aplicar(morfologia.erosao))
    menu_morf.add_command(label="Dilatação", command=lambda: aplicar(morfologia.dilatacao))
    menu.add_cascade(label="Morfologia", menu=menu_morf)

    # Menu Segmentação
    menu_seg = tk.Menu(menu, tearoff=0)
    menu_seg.add_command(label="Segmentação por Otsu", command=lambda: aplicar(segmentacao.segmentacao_otsu))
    menu.add_cascade(label="Segmentação", menu=menu_seg)

    janela.config(menu=menu)
    janela.mainloop()
