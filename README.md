# Editor de Imagens - Projeto PDI

Este é um sistema interativo desenvolvido para a disciplina **SIN392 - Introdução ao Processamento Digital de Imagens** da Universidade Federal de Viçosa – Campus Rio Paranaíba.

## 🎯 Objetivo
Permitir a edição e análise de imagens através de uma interface gráfica intuitiva com múltiplas funcionalidades de processamento digital de imagens.

---

## 📦 Funcionalidades

### 📁 Arquivo
- Abrir imagem (JPG, PNG, etc.)
- Salvar imagem

### 📊 Histograma
- Exibição do histograma
- Equalização de histograma

### 🌈 Intensidade
- Alargamento de contraste
- Negativo

### 🔽 Filtros Passa-Baixa
- Média
- Mediana
- Gaussiano
- Máximo
- Mínimo

### 🔼 Filtros Passa-Alta
- Laplaciano
- Roberts
- Prewitt
- Sobel

### 🔃 Fourier
- Visualizar espectro
- Filtros no domínio da frequência (passa-alta/baixa)

### ⚙️ Morfologia
- Erosão
- Dilatação

### 🧠 Segmentação
- Limiarização com método de Otsu

---

## 🖥️ Tecnologias utilizadas
- Python 3
- OpenCV
- Tkinter
- NumPy
- Matplotlib
- Pillow

---

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/PedroLemosMariano/Projeto-PDI.git
   cd editor-pdi

2. Crie um ambiente virtual (opcional):
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3. Instale as dependências:
    pip install -r requirements.txt

4. Execute o sistema:
    python main.py

👩‍🏫 Desenvolvido por: Pedro Lemos Mariano
