from interface import tela_inicial, menu_principal, menu_personagens
from personagens import get_personagens
from batalha import iniciar_batalha

tela_inicial()

personagens = get_personagens()
personagem_escolhido = None

while True:

    menu_principal()
    op = input('Escolha: ')

    if op == '1':
        menu_personagens()
        char = input('Selecione o personagem: ')

        if char in personagens:
            personagem_escolhido = personagens[char]
            p = personagem_escolhido

            print(f'''
{p["nome"]}
{p["descricao"]}

Vida: {p["vida"]}
Ataque: {p["ataque"]}
Defesa: {p["defesa"]}
            ''')

            input('Pressione ENTER para continuar...')

        else:
            print('Opção inválida')

    elif op == '2':
        print('Sobre...')

    elif op == '3':
        if personagem_escolhido:
            iniciar_batalha(personagem_escolhido)
        else:
            print('Escolha um personagem primeiro!')

    elif op == '4':
        print('Saindo...')
        break

    else:
        print('Opção inválida')