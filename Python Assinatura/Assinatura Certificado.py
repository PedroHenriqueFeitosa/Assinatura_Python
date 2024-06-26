
from PIL import Image, ImageFont, ImageDraw

coord_pessoa1 = (150,4)
coord_mail = (192,17)
coord_mail_label= (150,17)
coord_ramal = (200,31)
coord_ramal_label=(150,31)
coord_unidade=(210,60)
coord_unidade_label=(150,60)
coord_site=(183,46)
coord_site_label=(150,46)

with open(r'nomes_certificados.txt', 'r') as f:
    arquivo = f.read()
    for linha in arquivo.split('\n'):
       

        dados = linha.strip().split(';')
        print(dados)
        registro, nome, email, unidade, ramal = dados


        imagem = Image.open(r'Modelo.PNG')
        caminho_fonte1 = r"C:\Windows\Fonts\Arialbd.TTF"
        caminho_fonte2 =r"C:\Windows\Fonts\Verdana.TTF"
        caminho_fonte3 =r"C:\Windows\Fonts\Verdanab.TTF"
        caminho_fonte4=r"C:\Windows\Fonts\DejaVuSans.TTF"

        font1 =ImageFont.truetype(caminho_fonte1,12)
        font2 =ImageFont.truetype(caminho_fonte2,12)
        font3 =ImageFont.truetype(caminho_fonte3,12)
        font4=ImageFont.truetype(caminho_fonte4,18)
        rgb_preto = (0,0,0)
        desenho = ImageDraw.Draw(imagem)


        desenho.text(coord_pessoa1, nome , font=font1, fill=rgb_preto)
        desenho.text(coord_ramal_label, u'\u260f', font=font4, fill=rgb_preto)
        #desenho.text(coord_ramal_label, '    Ramal:(13) 3228-9300', font=font3, fill=rgb_preto)
        #desenho.text(coord_ramal, ramal, font=font2, fill=rgb_preto)
        desenho.text(coord_mail_label, u'\u2709', font=font4, fill=rgb_preto)
        desenho.text(coord_mail, email, font=font2, fill=rgb_preto)
        desenho.text(coord_unidade, unidade, font=font2, fill=rgb_preto)
        desenho.text(coord_unidade_label, 'Lotação:', font=font3, fill=rgb_preto)
        desenho.text(coord_site_label, 'Site:', font=font3, fill=rgb_preto)
        desenho.text(coord_site, ':https://cetsantos.com.br/', font=font2, fill=rgb_preto)
        imagem.save(f'{registro}.png')