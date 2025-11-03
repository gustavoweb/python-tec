# 1. Importar bibliotecas
import requests      # Para fazer requisições web
from bs4 import BeautifulSoup  # Para analisar HTML

# 2. Fazer requisição ao site
resposta = requests.get("URL_DO_SITE")

# 3. Converter HTML para objeto analisável
soup = BeautifulSoup(resposta.content, 'html.parser')

# 4. Buscar elementos na página
nome = soup.find('tag', class_='classe')
preco = soup.find('outra_tag')

# 5. Mostrar resultados
print(nome.text, preco.text)