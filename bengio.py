def resumo():
    mensagem = "Yoshua Bengio é um cientista da computação canadense, conhecido por seu trabalho sobre redes neurais artificiais e aprendizagem profunda."
    return mensagem


def doutorado():
    mensagem = "Bengio obteve seu doutorado da universidade McGill, desenvolvendo sua tese sobre um modelo de treinamento de redes neurais usando alinhamento probabilístico, aplicado no reconhecimento de voz"
    return mensagem


def contribuicoes():
    mensagem = "Principalmente machine learning (especificamente o método deep learning, que o levou a ganhar o Prêmio Turing em 2018)\nEm 2022, ele se tornou o cientista da computação com o maior índice h no mundo, ou seja, o mais citado em trabalhos acadêmicos"
    return mensagem


def artigos():
    mensagem = "Alguns de seus principais artigos são: Deep Learning, publicado em 2015; Generative Adversarial Networks, de 2020; e Gradient-based learning applied to document recognition, sua tese de doutorado, de 1998."
    return mensagem


def citacoes():
    mensagem = "Bengio já foi citado em 623054 artigos acadêmicos e científicos."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
