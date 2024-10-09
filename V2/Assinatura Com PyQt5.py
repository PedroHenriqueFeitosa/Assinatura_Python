import sys
import re
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QMessageBox
)
from PIL import Image, ImageFont, ImageDraw

# Função para validar e-mail
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Função para gerar assinaturas
def gerar_assinaturas():
    try:
        registro = entrada_registro.text()
        nome = entrada_nome.text()
        email = entrada_email.text()
        unidade = entrada_unidade.text()
        ramal = entrada_ramal.text()
        output_path = entrada_saida.text()

        if not all([registro, nome, email, unidade, ramal]):
            QMessageBox.critical(window, "Erro", "Por favor, preencha todos os campos.")
            return

        if not is_valid_email(email):
            QMessageBox.critical(window, "Erro", "Por favor, insira um e-mail válido.")
            return

        # Abrir a imagem e definir as fontes
        imagem = Image.open("ModeloJPEG.png")
        font1 = ImageFont.truetype("C:\\Windows\\Fonts\\Arialbd.TTF", 16)
        font2 = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.TTF", 13)
        font3 = ImageFont.truetype("C:\\Windows\\Fonts\\Ariblk.TTF", 13)
        rgb_preto = (0, 0, 0)
        desenho = ImageDraw.Draw(imagem)

        # Coordenadas para o texto
        coord_pessoa1 = (165, 7)
        coord_ramal = (220, 29)
        coord_ramal_label = (165, 26)
        coord_mail = (220, 46)
        coord_mail_label = (165, 43)
        coord_unidade = (235, 62)
        coord_unidade_label = (165, 59)
        coord_site = (205, 79)
        coord_site_label = (165, 76)

        # Desenhar o texto
        desenho.text(coord_pessoa1, nome, font=font1, fill=rgb_preto)
        desenho.text(coord_ramal_label, 'Ramal:', font=font3, fill=rgb_preto)
        desenho.text(coord_ramal, ramal, font=font2, fill=rgb_preto)
        desenho.text(coord_mail_label, 'E-mail:', font=font3, fill=rgb_preto)
        desenho.text(coord_mail, email, font=font2, fill=rgb_preto)
        desenho.text(coord_unidade, unidade, font=font2, fill=rgb_preto)
        desenho.text(coord_unidade_label, 'Lotação:', font=font3, fill=rgb_preto)
        desenho.text(coord_site_label, 'Site:', font=font3, fill=rgb_preto)
        desenho.text(coord_site, 'https://cetsantos.com.br/', font=font2, fill=rgb_preto)

        # Salvar a imagem com o nome do registro
        output_file_path = os.path.join(os.path.dirname(output_path), f'{registro}.png')
        imagem.save(output_file_path)

        QMessageBox.information(window, "Sucesso", "Assinatura gerada com sucesso!")
    except Exception as e:
        QMessageBox.critical(window, "Erro", str(e))

# Função para escolher onde salvar a assinatura
def escolher_diretorio():
    file_path, _ = QFileDialog.getSaveFileName(window, "Salvar Assinatura Como", "", "PNG files (*.png);;JPEG files (*.jpg)")
    if file_path:  # Verifica se o usuário realmente escolheu um arquivo
        entrada_saida.setText(file_path)

# Criação da janela principal
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Gerador de Assinaturas")
window.setGeometry(100, 100, 800, 350)

layout = QVBoxLayout()

# Campos de entrada
labels = ["Registro:", "Nome:", "E-mail:", "Lotação:", "Ramal:", "Salvar Assinatura Como:"]
entradas = {}

for label_text in labels:
    label = QLabel(label_text)
    layout.addWidget(label)
    
    entrada = QLineEdit()
    layout.addWidget(entrada)
    entradas[label_text] = entrada

# Referenciar as entradas
entrada_registro = entradas["Registro:"]
entrada_nome = entradas["Nome:"]
entrada_email = entradas["E-mail:"]
entrada_unidade = entradas["Lotação:"]
entrada_ramal = entradas["Ramal:"]
entrada_saida = entradas["Salvar Assinatura Como:"]

# Botão para escolher o diretório
botao_escolher = QPushButton("Escolher Diretório")
botao_escolher.clicked.connect(escolher_diretorio)
layout.addWidget(botao_escolher)

# Botão para gerar assinaturas
botao_gerar = QPushButton("Gerar Assinatura")
botao_gerar.clicked.connect(gerar_assinaturas)
layout.addWidget(botao_gerar)

# Configurar o layout
window.setLayout(layout)
window.show()

# Iniciar o loop da aplicação
sys.exit(app.exec_())
