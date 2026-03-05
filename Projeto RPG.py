from time import sleep
from random import randint
def menu1():
    return('''
    [1] PERSONAGENS
    [2] SOBRE
    [3] SAIR 
    ''')



def menu_char():
    return('''
    [1] Mago Negro
    [2] Ninja
    [3] Guerreiro
    ''')


def ataque_jogador(a, b):
    return a - b


def ataque_maquina():
    return randint(1, 2)


def vida_jogador(a, b):
    return a - b


def vida_maquina(a, b):
    return a - b


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



def only_personagem():
    return {
        "1": { "nome": "Mago Negro", "vida": 80, "ataque": 20, "defesa": 5},
        "2": { "nome": "Ninja", "vida": 90, "ataque": 15, "defesa": 7},
        "3": { "nome": "Guerreiro", "vida": 110, "ataque": 15, "defesa": 12},

    }
personagem = only_personagem()



def batalhas_menu():
    print('''[1] Atacar
    [2] Defender
    [3] Surrender ''')


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

    if op_menu == '3':
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
    
        RPG-ARENA é um jogo desenvolvido em Python com foco em
        lógica de programação e evolução contínua.
    
        O projeto foi criado com o objetivo de praticar conceitos
        fundamentais como:
        - Estruturas condicionais
        - Loops
        - Listas
        - Funções
        - Organização de código
        O jogo será modificado sempre que eu evoluir meu aprendizado,
        e assim irei adicionar novas funções ao jogo.
    
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

    else:
        print('Opção invalida')

