from PIL import Image, ImageFilter

# primeira imagem selecionada do slide
imagem = Image.open('images/burj-kalifa.png')
imagem_borrada = imagem.filter(ImageFilter.GaussianBlur(2))

# primeira variavel de vende ou aluga casa/apartamento
imagem_inserir = Image.open('images/assets-de-imagem/vende-se_terreno.png')
largura_inserir, altura_inserir = imagem_inserir.size
imagem_inserir = imagem_inserir.resize(
    (int(largura_inserir * 0.4), int(altura_inserir * 0.4)))

largura_imagem = imagem.width
altura_imagem = imagem.height
largura_inserir = imagem_inserir.width
altura_inserir = imagem_inserir.height
posicao = ((largura_imagem - largura_inserir) // 2, (altura_imagem // 2) - 165)

imagem_borrada.paste(imagem_inserir, posicao, imagem_inserir)
imagem_borrada.save("slide-1.png")
imagem_borrada.show()
