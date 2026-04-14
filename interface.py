from colorama import Fore, Style, init
from time import sleep

init(autoreset=True)


def tela_inicial():
    print(Fore.CYAN + '=' * 30)
    print(Fore.MAGENTA + Style.BRIGHT + 'RPG-ARENA'.center(30))
    print(Fore.CYAN + '=' * 30)

    sleep(0.5)

    print(Fore.BLUE + 'R'.center(5, '_'))
    sleep(0.5)
    print(Fore.BLUE + 'P'.center(11, '_'))
    sleep(0.5)
    print(Fore.BLUE + 'G'.center(17, '_'))
    sleep(0.5)

    print(Fore.MAGENTA + Style.BRIGHT + 'RPG-ARENA'.center(32, '='))

    print()
    print(Fore.YELLOW + 'Carregando o mundo...')

    print()
    for _ in range(18):
        print(Fore.GREEN + '█', end='')
        sleep(0.1)

    print()




def menu_principal():
    print(Fore.CYAN + '=' * 30)
    print(Fore.MAGENTA + Style.BRIGHT + 'MENU'.center(30))
    print(Fore.CYAN + '=' * 30)

    print(Fore.GREEN + '[1] PERSONAGENS')
    print(Fore.YELLOW + '[2] SOBRE')
    print(Fore.RED + '[3] BATALHAS')
    print('[4] SAIR')

    print()



def menu_personagens():
    print(Fore.CYAN + '=' * 30)
    print(Fore.BLUE + Style.BRIGHT + 'PERSONAGENS'.center(30))
    print(Fore.CYAN + '=' * 30)

    print('[1] Mago Negro')
    print('[2] Ninja')
    print('[3] Guerreiro')

    print()