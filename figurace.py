import os, sys
import PySimpleGUI as sg

#esto es para añadir core al path y poder llamar al menu principal del juego
carpeta = os.path.join(os.getcwd(), "src", "core")
sys.path.insert(0, carpeta)

win = "win32", "cygwin"

if __name__ == "__main__":
      my_os = sys.platform
      try:
            if my_os in win:
                  from src.core import menu_de_inicio as menu
                  menu.ventana_principal()
            elif my_os == "linux":
                  import menu_de_inicio as menu
                  menu.ventana_principal()
            elif my_os == 'darwin':
                 #falta macOS
                 pass
      except ModuleNotFoundError or ImportError:
            sg.popup_error("Ups!, hay un problemita interno.")
            
      
      