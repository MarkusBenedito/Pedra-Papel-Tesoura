import random

def jogada():
    # Função que pega os valores do usuário e do computador e determina quem ganhou ou perdeu
        opcoes = ["Pedra", "Papel", "Tesoura"]
        usua = input("Pedra \n"
            "Papel \n"
            "Tesoura \n"
            "Escolha sua jogada:")
        compu = random.choice(opcoes)
        print("O computador escolheu:", random.choice(opcoes))
        if (usua == compu):
            return "EMPATE"

        if vitoria(usua, compu):
            return "O usuário ganhou"

        return "O computador ganhou"
def vitoria(Jogador, Computador):
    # retorna True se o jogador vencer
    if (Jogador == "Pedra" and Computador == "Tesoura") or (Jogador == "Tesoura" and Computador == "Pedra") or (Jogador == "Papel" and Computador == "Pedra"):
        return True
while True:
    # Chamando a função
    print(jogada())
    # Caso o usuário queira continuar jogando ou caso ele queira parar.
    res = input("Você que continuar?")
    if (res == "Sim"):
        continue
    else:
        break

