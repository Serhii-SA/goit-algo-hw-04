
# Не звертати увагу ,поки не встиг зробити ,нажаль

from colorama import Fore, Back, Style

import sys
from pathlib import Path 

path = Path("")
print(f'Route is - {path}')
def main():
    if len(sys.argv) > 1:
        print(Back.CYAN + sys.argv[1])

if __name__ == "__main__":
    main()
    
print(Fore.RED + 'Це червоний текст')
print(Back.GREEN + 'Це текст на зеленому фоні')
print(Style.RESET_ALL)
print('Це звичайний текст після скидання стилю')

print(__name__)

