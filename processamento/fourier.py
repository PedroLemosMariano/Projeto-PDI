import cv2
import numpy as np
import matplotlib.pyplot as plt

def espectro_fourier(imagem):
    """Exibe o espectro de magnitude da Transformada de Fourier."""
    f = np.fft.fft2(imagem)
    fshift = np.fft.fftshift(f)
    magnitude = 20 * np.log(np.abs(fshift) + 1)

    plt.figure(figsize=(6, 4))
    plt.title("Espectro de Fourier")
    plt.imshow(magnitude, cmap='gray')
    plt.colorbar()
    plt.show()

def filtro_freq(imagem, tipo="passa-baixa", raio=30):
    """Aplica filtro passa-baixa ou passa-alta no domínio da frequência."""
    linhas, colunas = imagem.shape
    crow, ccol = linhas // 2 , colunas // 2

    # FFT e centralização
    f = np.fft.fft2(imagem)
    fshift = np.fft.fftshift(f)

    # Criação da máscara
    mascara = np.zeros((linhas, colunas), np.uint8)
    if tipo == "passa-baixa":
        cv2.circle(mascara, (ccol, crow), raio, 1, -1)
    elif tipo == "passa-alta":
        cv2.circle(mascara, (ccol, crow), raio, 0, -1)
        mascara = 1 - mascara

    # Aplicação do filtro
    fshift_filtrado = fshift * mascara
    f_ishift = np.fft.ifftshift(fshift_filtrado)
    imagem_filtrada = np.fft.ifft2(f_ishift)
    imagem_filtrada = np.abs(imagem_filtrada)
    imagem_filtrada = np.clip(imagem_filtrada, 0, 255).astype(np.uint8)

    return imagem_filtrada
