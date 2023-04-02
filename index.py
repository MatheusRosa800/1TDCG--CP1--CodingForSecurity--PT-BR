"""
Integrantes
- Pedro Augusto
- Matheus Rosa
- Eduardo dos Santos
- Henrique Lorenzetti
- Jorge Gabriel
"""

import time

# Apresentação
print("-=" * 20)
print("\t\tSequência de Fibonacci")
print("-=" * 20)

# Inicialização de variáveis
valor1 = 0
valor2 = 1
proximo = 0
resultado = f"{valor1} - {valor2}"
quantidadeexibidas = 2


# Função para apresentar a sequência de fibonacci
def exibirsequenciafibonacci(quantidadeexibicao):

    # Variáveis globais
    global resultado, valor1, valor2, proximo, quantidadeexibidas

    for _i in range(quantidadeexibicao):
        # Próximo valor da sequência
        proximo = valor1 + valor2

        # Adicionando o novo valor no resultado
        resultado += f" - {proximo}"

        # Progredindo os valores das variáveis
        valor1 = valor2
        valor2 = proximo

    linha()
    print("Carregando números...")
    linha()
    time.sleep(1)

    quantidadeexibidas += quantidadeexibicao
    print(f"Os {quantidadeexibidas} primeiros números da sequência são:\n{resultado}")


# Função recursiva para perguntar ao usuário se deseja ver mais números da sequência de fibonacci
def sugerirmaisnumeros():

    global quantidade

    while True:
        linha()
        ver_mais = input("Deseja ver mais números? [ S / N ]\nResposta: ").upper().strip()

        match ver_mais:
            case "S":
                linha()
                quantidade = int(input("Quantos números a mais devem ser exibidos?\nQuantidade: "))
                exibirsequenciafibonacci(quantidade)
                sugerirmaisnumeros()
                break

            case "N":
                linha()
                print("Obrigado por utilizar nosso programa e volte sempre. :)")
                break

            case _:
                print("[ERRO] Escreva S ou N apenas")


def linha():
    print("-" * 48)


while True:
    try:
        quantidade = int(input("Quantos números devem ser exibidos?\nQuantidade: "))

        if quantidade < 2:
            while quantidade < 2:
                linha()
                quantidade = int(input("[ERRO] Por favor digite uma quantidade maior que 2\nQuantidade: "))

        # Redução na quantidade por já existir o 0 e 1 na lista
        quantidade -= 2
        exibirsequenciafibonacci(quantidade)
        sugerirmaisnumeros()
        break

    except ValueError:
        print("[ERRO] Digite apenas números inteiros.")
        linha()

