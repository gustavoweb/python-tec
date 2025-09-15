# Primeiro instale a biblioteca:
# pip install qrcode[pil]

import qrcode

# Entrada do usuário
link = input("Digite o link ou texto para gerar o QR Code: ")

# Criando o QR Code
qr = qrcode.QRCode(
    version=1,  # controla o tamanho do QR (1 é o menor)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # tamanho de cada quadradinho
    border=4,     # espessura da borda
)

qr.add_data(link)
qr.make(fit=True)

# Criar imagem
img = qr.make_image(fill_color="black", back_color="white")

# Salvar como arquivo
img.save("qrcode.png")

print("✅ QR Code gerado com sucesso! Arquivo salvo como 'qrcode.png'")