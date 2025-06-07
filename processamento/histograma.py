import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcular_histograma(imagem):
    """Calcula e exibe o histograma de uma imagem em tons de cinza."""
    if len(imagem.shape) != 2:
        raise ValueError("A imagem precisa estar em escala de cinza.")

    hist = cv2.calcHist([imagem], [0], None, [256], [0, 256])
    hist = hist.flatten()

    plt.figure(figsize=(6, 4))
    plt.title("Histograma da Imagem")
    plt.xlabel("Intensidade de pixel")
    plt.ylabel("Frequência")
    plt.plot(hist, color='black')
    plt.grid(True)
    plt.show()

def equalizar_histograma(imagem):
    """Equaliza o histograma da imagem para melhorar contraste."""
    if len(imagem.shape) != 2:
        raise ValueError("A imagem precisa estar em escala de cinza.")
    
    imagem_eq = cv2.equalizeHist(imagem)
    return imagem_eq
