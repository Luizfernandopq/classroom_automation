
import pyperclip

# Pega o conteúdo da área de transferência
if __name__ == '__main__':

    clipboard_content = pyperclip.paste()
    # Exibe o conteúdo
    print("Conteúdo copiado:", clipboard_content)
