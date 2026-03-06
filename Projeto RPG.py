from time import sleep
from random import randint

#ef only_personagem():  Essa Funçao Será Adicionada Em Breve!!!
#return {
#       "1": { "nome": "Mago Negro", "vida": 80, "ataque": 20, "defesa": 5},
#      "2": { "nome": "Ninja", "vida": 90, "ataque": 15, "defesa": 7},
#      "3": { "nome": "Guerreiro", "vida": 110, "ataque": 15, "defesa": 12},

 #  }

#personagens = only_personagem()

def aviso():
    print('''==============================================================
AVISO DE DESENVOLVIMENTO
========================

O sistema de batalha do RPG-ARENA foi temporariamente
simplificado para apenas duas ações:

[1] Atacar
[2] Curar

Durante o desenvolvimento, percebi que a versão anterior
do sistema de combate estava ficando complexa demais para
o estágio atual do projeto, o que acabou gerando algumas
dificuldades na implementação.

Para manter o jogo funcional e continuar evoluindo no
aprendizado de programação, a batalha foi simplificada
temporariamente.

Em futuras atualizações o sistema de combate será otimizado
e novas mecânicas serão adicionadas, como:

* Defesa
* Habilidades especiais
* Sistema de combate mais estratégico

Obrigado por testar o RPG-ARENA!
Este projeto continuará evoluindo conforme meu aprendizado
em Python avança.
=================
''')


def menu1():
    return('''
    [1] PERSONAGENS
    [2] SOBRE
    [3] BATALHAS
    [4] SAIR 
    ''')



def menu_char():
    return('''
    [1] Mago Negro
    [2] Ninja
    [3] Guerreiro
    ''')


def menu_batalhas():

    while True:
        print('''\n[1] Mago Negro
        [2] Ninja
        [3] Guerreiro''')
        try:
            user = int(input('Escolha um Personagem: '))
            match user:
                case 1:
                    print('Ótima Opção, escolheu o Mago Negro.')
                    break
                case 2:
                    print('Nossa escolha magnifica, escolheu o Ninja.')
                    break
                case 3:
                    print('Você é corajoso, escolheu o Guerreiro.')
                    break
                case _:
                    print('Escolha Personagens Válidos')
        except ValueError:
            print('Escolha uma opção válida: ')



def batalhas_menu():
    return print('''[1] Atacar
    [2] Curar
    ''')


def batalhas_1():
    print(f'\n{"1 ROUND":=^20}')
    efeito_2 = '= = = = = YOU vs CPU= = = = ='
    for letra in efeito_2:
        sleep(1)
        print(letra, end=' ')
    print()


def ataque_jogador(a, b):
    return a - b



print(f'{"RPG-ARENA":=^20}')
print(f'{"R":_^5}')
sleep(1)
print(f'{"P":_^11}')
sleep(1)
print(f'{"G":_^17}')
sleep(1)
print(f'{"RPG-ARENA":=^32}')
print('AGUARDE...')
r1 = '='
for w in range(1, 19):
    sleep(0.2)
    print(r1, end=' ')
while True:
    print(menu1())
    op_menu = (input('Selecione a opção: '))

    if op_menu == '4':
        print('Saindo do jogo...')
        sleep(1)
        break

    if op_menu == '1':
        print(menu_char())
        char = (input('Selecione o personagem: '))
        if char == '1':
            print(f'SUPER MAGO NEGRO...')
            sleep(2)
            print('''
            Mago Negro – Mestre das artes sombrias, usa feitiços poderosos para atacar à distância.
            Frágil no corpo, mas mortal com sua magia.
            Atributo     | Valor    | Observação
            Vida         | 80	    | Frágil no corpo, fácil de ser atingido
            Ataque       | 20	    | Poderoso com magia à distância
            Defesa       | 5	    | Baixa resistência física
            ''')

        elif char == '2':
            print(f'NINJA...')
            sleep(2)
            print('''
            Ninja – Mestre da furtividade e agilidade.
            Ataques rápidos e esquiva alta, ideal para jogadores que preferem movimentação estratégica.
            Ninja — Atributos iniciais
            Atributo	 | Valor   | Observação
            Vida         | 90	   | Média, mais resistente que o mago
            Ataque       | 15	   | Ataque rápido, não tão forte quanto o mago
            Defesa       | 7	   | Média, consegue suportar alguns ataques
            ''')

        elif char == '3':
            print('GUERREIRO')
            print(f'''
            Atributo      | Valor | Observação
            {"="*70}             
            Vida          | 110   | Maior resistência, suporta mais ataques
            Ataque        | 15    | Dano médio, confiável em combates diretos
            Defesa        | 12    | Forte, reduz consideravelmente o dano recebido
           ''')


        else:
            print('Opção Invalida')
    elif op_menu == '2':
        print('CARREGANDO...')
        sleep(2)
        print(f'''
        {"=" * 70}
        {"SOBRE O JOGO - RPG ARENA":^70}
        {"=" * 70}
    
        RPG-ARENA é um jogo desenvolvido em Python com foco em lógica de
programação e evolução contínua.

O projeto foi criado com o objetivo de praticar conceitos
fundamentais como:

Estruturas condicionais

Loops

Listas e dicionários

Funções

Organização de código

O jogo será modificado sempre que eu evoluir meu aprendizado,
e assim novas funcionalidades serão adicionadas ao projeto.

Durante o desenvolvimento percebi que algumas ideias iniciais
estavam deixando o sistema de batalha mais complexo do que o
necessário para o estágio atual do projeto.

Por esse motivo, decidi simplificar temporariamente o sistema
de combate, utilizando uma mecânica básica de ataque e cura,
para garantir que o jogo funcione corretamente enquanto continuo
evoluindo meus conhecimentos em programação.

No futuro, pretendo adicionar novamente mecânicas mais avançadas
como defesa, habilidades especiais e melhorias no sistema de
batalha.

🧙‍♂️ MAGO NEGRO
Alto poder mágico e grande capacidade ofensiva, porém com
menor resistência física.

🥷 NINJA
Especialista em agilidade e ataques rápidos.

⚔️ GUERREIRO
Grande resistência e equilíbrio entre ataque e sobrevivência.

Cada personagem possui atributos próprios de vida e ataque,
proporcionando diferentes estilos de jogo.
    
        {"PERSONAGENS INICIAIS":^70}
        {"-" * 70}
    
        🧙‍♂️  MAGO NEGRO
           Alto poder mágico, ataque intenso e estratégia.
        {"-" * 70}
        🥷  NINJA
           Agilidade extrema e alta chance de esquiva.
        {"-" * 70}
        ⚔️  GUERREIRO
           Força e resistência equilibradas para combate direto.
        {"=" * 70}
        Cada personagem possui atributos próprios de vida,
        ataque, defesa e habilidades especiais,
        proporcionando diferentes estilos de jogo.
        {"=" * 70}
        ''')


    elif op_menu == '3':
        eu = 100
        inimigo = 100

        while eu > 0 and inimigo > 0:
            print(f'Minha Vida {eu}')
            print(f'Vida do Inimigo {inimigo}')

            print('''
            [1] Atacar
            [2] Curar''')

            acao = str(input('Selecione uma opção:'))
            if acao == '1':
                dano = randint(10, 20)
                inimigo -= dano
                print(f'Você Causou {dano} no Inimigo')

            elif acao == '2':
                cura = randint(7, 25)
                eu += cura
                print(f'Você Recuperou {cura} de Vida')

            else:
                print('Opção Invalida')
                continue

            if inimigo <=0:
                print('Parabéns Você Ganhou')
                break

            dano_inimigo = randint(10, 20)
            eu -= dano_inimigo
            print(f'Inimigo Causou {dano_inimigo} em Você!')

            if eu <= 0:
                    print('Você Perdeu kkk Tente Outra Vez!!!')

