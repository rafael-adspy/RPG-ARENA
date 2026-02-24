print(f'{"RPG-ARENA":=^20}')
from random import randint
from time import sleep
print(f'{"R":_^5}')
sleep(1)
print(f'{"P":_^11}')
sleep(1)
print(f'{"G":_^17}')
sleep(1)
print('CARREGANDO...')
sleep(2)
print(f'{"RPG-ARENA":=^34}')
print('AGUARDE...')
r1 = '='
for w in range(1, 19):
    sleep(0.3)
    print(r1, end=' ')
menu = input('''
[1] PERSONAGENS
[2] BATALHAS
[3] SOBRE
[4] SAIR
Selecione a opção: ''')
if menu == '1':
    char = input('''
    [1] Mago Negro
    [2] Ninja
    [3] Guerreiro
    Selecione o personagem: ''')
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
    if char == '2':
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
    if char == '3':
        print('GUERREIRO')
        print('''Atributo	Valor	Observação
        Vida	110	Maior resistência, suporta mais ataques
        Ataque	15	Dano médio, confiável em combates diretos
        Defesa	12	Forte, reduz consideravelmente o dano recebido
        ''')

        
