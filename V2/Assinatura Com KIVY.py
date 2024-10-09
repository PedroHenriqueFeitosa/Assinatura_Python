import os
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from PIL import Image, ImageFont, ImageDraw

# Função para validar e-mail
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Função para gerar assinaturas
def gerar_assinaturas(registro, nome, email, unidade, ramal, output_path):
    if not all([registro, nome, email, unidade, ramal]):
        show_popup("Erro", "Por favor, preencha todos os campos.")
        return

    if not is_valid_email(email):
        show_popup("Erro", "Por favor, insira um e-mail válido.")
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

    show_popup("Sucesso", "Assinatura gerada com sucesso!")

# Função para mostrar pop-ups
def show_popup(title, message):
    popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
    popup.open()

# Classe principal da aplicação
class GeradorAssinaturasApp(App):
    def build(self):
        self.title = "Gerador de Assinaturas"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Entradas
        self.entrada_registro = TextInput(hint_text="Registro", multiline=False)
        self.entrada_nome = TextInput(hint_text="Nome", multiline=False)
        self.entrada_email = TextInput(hint_text="E-mail", multiline=False)
        self.entrada_unidade = TextInput(hint_text="Lotação", multiline=False)
        self.entrada_ramal = TextInput(hint_text="Ramal", multiline=False)
        self.entrada_saida = TextInput(hint_text="Salvar Assinatura Como", multiline=False)

        # Adicionando os widgets ao layout
        layout.add_widget(self.entrada_registro)
        layout.add_widget(self.entrada_nome)
        layout.add_widget(self.entrada_email)
        layout.add_widget(self.entrada_unidade)
        layout.add_widget(self.entrada_ramal)
        layout.add_widget(self.entrada_saida)

        # Botão para escolher o diretório
        btn_escolher = Button(text="Escolher Diretório")
        btn_escolher.bind(on_release=self.escolher_diretorio)
        layout.add_widget(btn_escolher)

        # Botão para gerar assinaturas
        btn_gerar = Button(text="Gerar Assinatura")
        btn_gerar.bind(on_release=self.gerar_assinatura)
        layout.add_widget(btn_gerar)

        return layout

    def escolher_diretorio(self, instance):
        filechooser = FileChooserIconView()
        popup = Popup(title="Escolher Diretório", content=filechooser, size_hint=(0.9, 0.9))
        filechooser.bind(on_submit=lambda instance, selection, touch: self.set_output_path(selection, popup))
        popup.open()

    def set_output_path(self, selection, popup):
        if selection:
            self.entrada_saida.text = selection[0] + "/assinatura.png"
        popup.dismiss()

    def gerar_assinatura(self, instance):
        gerar_assinaturas(
            self.entrada_registro.text,
            self.entrada_nome.text,
            self.entrada_email.text,
            self.entrada_unidade.text,
            self.entrada_ramal.text,
            self.entrada_saida.text
        )

if __name__ == "__main__":
    GeradorAssinaturasApp().run()
