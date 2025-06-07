import cv2
import numpy as np

def erosao(imagem, tamanho_kernel=3):
    """Aplica erosão à imagem."""
    kernel = np.ones((tamanho_kernel, tamanho_kernel), np.uint8)
    return cv2.erode(imagem, kernel, iterations=1)

def dilatacao(imagem, tamanho_kernel=3):
    """Aplica dilatação à imagem."""
    kernel = np.ones((tamanho_kernel, tamanho_kernel), np.uint8)
    return cv2.dilate(imagem, kernel, iterations=1)
