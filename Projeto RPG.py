from time import sleep
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


def ataque(a, b):
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
    sleep(0.3)
    print(r1, end=' ')
while True:
    print(menu1())
    op1 = (input('Selecione a opção: '))

    if op1 == '1':
        print(menu_char())
        char = (input('Selecione o personagem: '))
        if char == '1':
            print(f'SUPER MAGO NEGRO...')
            sleep(2)
            print('''
            Mago Negro – Mestre das artes sombrias, usa feitiços poderosos para atacar à distância.
            Frágil no corpo, mas mortal com sua magia.
            Atributo	Valor	Observação
            Vida	80	Frágil no corpo, fácil de ser atingido
            Ataque	20	Poderoso com magia à distância
            Defesa	5	Baixa resistência física
            ''')
        elif char == '2':
            print(f'NINJA...')
            sleep(2)
            print('''
            Ninja – Mestre da furtividade e agilidade.
            Ataques rápidos e esquiva alta, ideal para jogadores que preferem movimentação estratégica.
            Ninja — Atributos iniciais
            Atributo	Valor	Observação
            Vida	90	Média, mais resistente que o mago
            Ataque	15	Ataque rápido, não tão forte quanto o mago
            Defesa	7	Média, consegue suportar alguns ataques
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
    elif op1 == '2':
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
    elif op1 == '3':
        print('Saindo do jogo...')
        sleep(2)
        break
    else:
        print('Opção invalida')
        


        
