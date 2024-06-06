def receber_tipo_de_carro():
    tipo_de_carro = input("Por favor, informe o tipo de carro que você deseja comprar: ")
    return tipo_de_carro


def receber_faixa_de_preco():
    while True:
        try:
            faixa_de_preco = float(input("Por favor, informe a faixa de preço que você pode pagar: "))
            return faixa_de_preco
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

lista_de_carros = [
    "corolla",
    "virtus",
    "gol",
    "golf",
    "polo",
    "jetta",
    "civic",
    "hilux",
    "SW4",
    "ferrari",
    "bugatti",
    "jeep compass",
    "jeep renegade",
    "onix",
    "prisma",
    "etios",
    "uno",
    "ford ka",
    "up",
    "corsa"
]

print(lista_de_carros)

def procurar_carro(nome_carro):
    carro_encontrado = False
    for carro in lista_de_carros:
        if carro.lower() == nome_carro.lower():
            carro_encontrado = True
            break
    if carro_encontrado:
        return "Carro encontrado"
    else:
        return "Carro não encontrado"

def avaliacao_carro(preco):
    if preco < 10000:
        return "mal estado"
    elif preco < 30000:
        return "conservado"
    elif preco < 60000:
        return "seminovo"
    else:
        return "novo"

while True:

    tipo_de_carro = receber_tipo_de_carro()
    faixa_de_preco = receber_faixa_de_preco()

    carro_existe = procurar_carro(tipo_de_carro)

    if carro_existe == "Carro encontrado":
        qualidade_carro = avaliacao_carro(faixa_de_preco)
        print(f"O usuário gostaria de um carro {tipo_de_carro} na qualidade de {qualidade_carro}.")
    else:
        print("Carro não encontrado")

    continuar = input("Deseja continuar? (Digite 'sim' para continuar ou pressione Enter para sair): ")
    if continuar.lower() != 'sim':
        break