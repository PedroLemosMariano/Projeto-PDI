import cv2

def segmentacao_otsu(imagem):
    """Segmenta a imagem usando o método de Otsu."""
    if len(imagem.shape) != 2:
        raise ValueError("A imagem deve estar em escala de cinza.")

    _, binarizada = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binarizada
