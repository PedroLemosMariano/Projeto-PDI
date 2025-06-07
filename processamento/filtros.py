import cv2
import numpy as np

# -------------------- Filtros Passa-Baixa --------------------

def filtro_media(imagem, tamanho=3):
    return cv2.blur(imagem, (tamanho, tamanho))

def filtro_mediana(imagem, tamanho=3):
    return cv2.medianBlur(imagem, tamanho)

def filtro_gaussiano(imagem, tamanho=3):
    return cv2.GaussianBlur(imagem, (tamanho, tamanho), 0)

def filtro_maximo(imagem, tamanho=3):
    return cv2.dilate(imagem, np.ones((tamanho, tamanho), np.uint8))

def filtro_minimo(imagem, tamanho=3):
    return cv2.erode(imagem, np.ones((tamanho, tamanho), np.uint8))

# -------------------- Filtros Passa-Alta --------------------

def filtro_laplaciano(imagem):
    return cv2.Laplacian(imagem, cv2.CV_64F).astype(np.uint8)

def filtro_roberts(imagem):
    kernelx = np.array([[1, 0], [0, -1]], dtype=np.float32)
    kernely = np.array([[0, 1], [-1, 0]], dtype=np.float32)
    grad_x = cv2.filter2D(imagem, -1, kernelx)
    grad_y = cv2.filter2D(imagem, -1, kernely)
    return cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

def filtro_prewitt(imagem):
    kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
    kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
    grad_x = cv2.filter2D(imagem, -1, kernelx)
    grad_y = cv2.filter2D(imagem, -1, kernely)
    return cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

def filtro_sobel(imagem):
    grad_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)
    grad = cv2.magnitude(grad_x, grad_y)
    return np.clip(grad, 0, 255).astype(np.uint8)
