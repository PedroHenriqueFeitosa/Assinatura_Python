import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageFont, ImageDraw
import os
import re

# Coordenadas para colocar na imagem da assinatura os textos.
coord_pessoa1 = (165, 7)
coord_ramal = (220, 29)
coord_ramal_label = (165, 26)
coord_mail = (220, 46)
coord_mail_label = (165, 43)
coord_unidade = (235, 62)
coord_unidade_label = (165, 59)
coord_site = (205, 79)
coord_site_label = (165, 76)

# Função para validar e-mail
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

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
        imagem = Image.open(r"ModeloJPEG.png")
        font1 = ImageFont.truetype(r"C:\Windows\Fonts\Arialbd.TTF", 16)
        font2 = ImageFont.truetype(r"C:\Windows\Fonts\Arial.TTF", 13)
        font3 = ImageFont.truetype(r"C:\Windows\Fonts\Ariblk.TTF", 13)
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

def escolher_diretorio():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    entrada_saida.delete(0, tk.END)
    entrada_saida.insert(0, file_path)

# Criação da janela principal
root = tk.Tk()
root.title("Gerador de Assinaturas")
root.geometry("800x850")
root.configure(bg="#e0e0e0")

# Definindo fontes
font_label = ("Arial", 12, "bold")
font_entry = ("Arial", 12)

# Campos de entrada
tk.Label(root, text="Registro:", font=font_label, bg="#e0e0e0").grid(row=0, column=0, pady=10, sticky='w')
entrada_registro = tk.Entry(root, width=50, font=font_entry, bd=2, bg="#f0f0f0")
entrada_registro.grid(row=0, column=1, pady=10)

tk.Label(root, text="Nome:", font=font_label, bg="#e0e0e0").grid(row=1, column=0, pady=10, sticky='w')
entrada_nome = tk.Entry(root, width=50, font=font_entry, bd=2, bg="#f0f0f0")
entrada_nome.grid(row=1, column=1, pady=10)

tk.Label(root, text="E-mail:", font=font_label, bg="#e0e0e0").grid(row=2, column=0, pady=10, sticky='w')
entrada_email = tk.Entry(root, width=50, font=font_entry, bd=2, bg="#f0f0f0")
entrada_email.grid(row=2, column=1, pady=10)

tk.Label(root, text="Lotação:", font=font_label, bg="#e0e0e0").grid(row=3, column=0, pady=10, sticky='w')
entrada_unidade = tk.Entry(root, width=50, font=font_entry, bd=2, bg="#f0f0f0")
entrada_unidade.grid(row=3, column=1, pady=10)

tk.Label(root, text="Ramal:", font=font_label, bg="#e0e0e0").grid(row=4, column=0, pady=10, sticky='w')
entrada_ramal = tk.Entry(root, width=50, font=font_entry, bd=2, bg="#f0f0f0")
entrada_ramal.grid(row=4, column=1, pady=10)

tk.Label(root, text="Salvar Assinatura Como:", font=font_label, bg="#e0e0e0").grid(row=5, column=0, pady=10, sticky='w')
entrada_saida = tk.Entry(root, width=50, font=font_entry, bd=2, bg="#f0f0f0")
entrada_saida.grid(row=5, column=1, pady=10)

# Botões
botao_escolher = tk.Button(root, text="Escolher Diretório", command=escolher_diretorio, bg="#4CAF50", fg="white", font=font_entry)
botao_escolher.grid(row=6, column=0, columnspan=2, pady=10)

botao_gerar = tk.Button(root, text="Gerar Assinatura", command=gerar_assinaturas, bg="#4CAF50", fg="white", font=font_entry)
botao_gerar.grid(row=7, column=0, columnspan=2, pady=20)

# Iniciar o loop da interface
root.mainloop()
