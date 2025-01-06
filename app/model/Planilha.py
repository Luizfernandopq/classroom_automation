from pathlib import Path

import pandas as pd


class Planilha:
    def __init__(self, filename):
        self.str_arquivo = filename
        self.caminho = self.find_relative_path(filename)
        self.dataframe = pd.read_csv(self.caminho)

    # Busca recursivamente no diretório do projeto
    def find_relative_path(self, filename):
        for caminho in Path("../").rglob(filename):
            return str(caminho.relative_to(Path(".")))
        return None
