import os, sys

#esto es para añadir core al path y poder llamar al menu principal del juego
carpeta = os.path.join(os.getcwd(), "src", "core")
sys.path.insert(0, carpeta)

import menu_de_inicio as menu

if __name__ == "__main__":
    menu.ventana_principal()