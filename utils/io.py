import cv2

def carregar_imagem(caminho):
    """Carrega a imagem em RGB e converte para escala de cinza."""
    imagem = cv2.imread(caminho)
    if imagem is None:
        raise ValueError("Erro ao carregar a imagem.")

    if len(imagem.shape) == 3 and imagem.shape[2] == 3:
        # Imagem em RGB → converter para cinza
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    return imagem

def salvar_imagem(imagem, caminho):
    """Salva a imagem no caminho especificado."""
    cv2.imwrite(caminho, imagem)
