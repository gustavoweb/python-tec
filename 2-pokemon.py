#pip install requests
import requests

def buscar_pokemon(nome):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            nome_pokemon = dados["name"].capitalize()
            altura = dados["height"] / 10
            peso = dados["weight"] / 10
            tipos = [t["type"]["name"] for t in dados["types"]]
            tipos_formatados = ", ".joins(tipos)

            return (f"Nome: {nome_pokemon}\n"
                    f"Altura: {altura} m\n"
                    f"Peso: {peso} kg\n"
                    f"Tipo(s): {tipos_formatados}")
        else:
            return "Pokémon não encontrado! Tente outro nome."
    except:
        return "Erro ao conectar a API PokeAPI."

def responder(mensagem):
    mensagem = mensagem.lower()
    if "oi" in mensagem or "olá" in mensagem:
        return "Olá! Digite o nome de um Pokémon: "
    elif mensagem == "sair":
        return "Até mais!"
    else:
        return buscar_pokemon(mensagem)

#Corpo do programa
print("Bot Pokémon (digite 'sair' para encerrar)\n")

while True:
    user_input = input("Pokémon: ")
    resposta = responder(user_input)

    print(f"Bot: {resposta}")

    if user_input.lower() == "sair":
        break