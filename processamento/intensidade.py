import cv2
import numpy as np

def alargamento_contraste(imagem):
    """Aplica alargamento de contraste com base nos valores mínimo e máximo."""
    minimo = np.min(imagem)
    maximo = np.max(imagem)

    if maximo - minimo == 0:
        return imagem.copy()  # evita divisão por zero

    imagem_norm = (imagem - minimo) * (255.0 / (maximo - minimo))
    imagem_norm = np.clip(imagem_norm, 0, 255).astype(np.uint8)
    return imagem_norm

def negativo(imagem):
    """Gera o negativo da imagem."""
    return 255 - imagem
