from random import randint, choice
from colorama import Fore, Style, init
from inimigos import get_inimigos

init(autoreset=True)

def iniciar_batalha(personagem):
    eu = personagem["vida"]
    ataque = personagem["ataque"]
    defesa = personagem["defesa"]

    inimigos = get_inimigos()
    inimigo = choice(inimigos)

    vida_inimigo = inimigo["vida"]
    ataque_inimigo = inimigo["ataque"]
    defesa_inimigo = inimigo["defesa"]

    print(Fore.YELLOW + Style.BRIGHT + '⚔️ BATALHA INICIADA ⚔️')
    print(Fore.YELLOW + f'Você encontrou um {inimigo["nome"]}!')
    print()

    while eu > 0 and vida_inimigo > 0:
        print(Fore.GREEN + f'Sua Vida: {eu}')
        print(Fore.RED + f'{inimigo["nome"]}: {vida_inimigo}')

        print()
        print(Fore.CYAN + '[1] Atacar')
        print(Fore.BLUE + '[2] Curar')

        acao = input('Escolha: ')
        print()

        if acao == '1':
            dano = randint(5, ataque) - defesa_inimigo
            dano = max(0, dano)
            vida_inimigo -= dano
            print(Fore.RED + f'💥 Você causou {dano} de dano!')

        elif acao == '2':
            cura = randint(5, 20)
            eu += cura
            print(Fore.GREEN + f'✨ Você recuperou {cura} de vida!')

        else:
            print(Fore.YELLOW + 'Opção inválida')
            continue

        if vida_inimigo <= 0:
            print()
            print(Fore.GREEN + Style.BRIGHT + '🏆 Você venceu!')
            break

        dano_inimigo = randint(5, ataque_inimigo) - defesa
        dano_inimigo = max(0, dano_inimigo)

        eu -= dano_inimigo
        print(Fore.RED + f'⚠️ {inimigo["nome"]} causou {dano_inimigo} de dano!')

        if eu <= 0:
            print()
            print(Fore.RED + Style.BRIGHT + '💀 Você foi derrotado!')