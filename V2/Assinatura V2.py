import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageFont, ImageDraw
import os
import re


coord_pessoa1 = (165,7)
coord_ramal = (220,26)
coord_ramal_label=(165,26)
coord_mail = (220,42)
coord_mail_label= (165,42)
coord_unidade=(230,58)
coord_unidade_label=(165,58)
coord_site=(205,74)
coord_site_label=(165,74)


# Função para validar e-mail
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Função para gerar assinaturas
def gerar_assinaturas():
    try:
        # Obter os dados inseridos pelo usuário
        registro = entrada_registro.get()
        nome = entrada_nome.get()
        email = entrada_email.get()
        unidade = entrada_unidade.get()
        ramal = entrada_ramal.get()
        output_path = entrada_saida.get()

        # Verificar se os campos obrigatórios estão preenchidos
        if not all([registro, nome, email, unidade, ramal]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        if not is_valid_email(email):
            messagebox.showerror("Erro", "Por favor, insira um e-mail válido.")
            return

        # Abrir a imagem e definir as fontes
        imagem = Image.open(r"Modelo JPEG .png")
        font1 = ImageFont.truetype(r"C:\Windows\Fonts\Arialbd.TTF", 16)
        font2 = ImageFont.truetype(r"C:\Windows\Fonts\Arial.TTF", 13)
        font3 = ImageFont.truetype(r"C:\Windows\Fonts\Ariblk.TTF",13)
        rgb_preto = (0, 0, 0)
        desenho = ImageDraw.Draw(imagem)

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

        messagebox.showinfo("Sucesso", "Assinatura gerada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função para escolher onde salvar a assinatura
def escolher_diretorio():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                           filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    entrada_saida.delete(0, tk.END)
    entrada_saida.insert(0, file_path)

# Criação da janela principal
root = tk.Tk()
root.title("Gerador de Assinaturas")
root.geometry("800x850")

# Campos de entrada
tk.Label(root, text="Registro:").pack(pady=5)
entrada_registro = tk.Entry(root, width=50)
entrada_registro.pack(pady=5)

tk.Label(root, text="Nome:").pack(pady=5)
entrada_nome = tk.Entry(root, width=50)
entrada_nome.pack(pady=5)

tk.Label(root, text="E-mail:").pack(pady=5)
entrada_email = tk.Entry(root, width=50)
entrada_email.pack(pady=5)

tk.Label(root, text="Lotação:").pack(pady=5)
entrada_unidade = tk.Entry(root, width=50)
entrada_unidade.pack(pady=5)

tk.Label(root, text="Ramal:").pack(pady=5)
entrada_ramal = tk.Entry(root, width=50)
entrada_ramal.pack(pady=5)

tk.Label(root, text="Salvar Assinatura Como:").pack(pady=5)
entrada_saida = tk.Entry(root, width=50)
entrada_saida.pack(pady=5)

# Botão para escolher o diretório
botao_escolher = tk.Button(root, text="Escolher Diretório", command=escolher_diretorio)
botao_escolher.pack(pady=5)

# Botão para gerar assinaturas
botao_gerar = tk.Button(root, text="Gerar Assinatura", command=gerar_assinaturas)
botao_gerar.pack(pady=20)

# Iniciar o loop da interface
root.mainloop()
