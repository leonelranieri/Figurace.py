import os, sys

#esto es para añadir core al path y poder llamar al menu principal del juego
carpeta = os.path.join(os.getcwd(), "src", "core")
sys.path.insert(0, carpeta)

win = "win32", "cygwin"
"darwin"

if __name__ == "__main__":
      my_os = sys.platform
      if my_os in win:
            from src.core import menu_de_inicio as menu
            menu.ventana_principal()
      elif my_os == "linux":
            import menu_de_inicio as menu
            menu.ventana_principal()
      elif my_os == 'darwin':
            #falta 
      