import time

from app.model.Planilha import Planilha

import keyboard

""" Classe para extrair dados de alunos da planilha do gsheets
"""
class Assistant:
    """
    Lembre de baixar a versão mais recente da planilha ALUNOS
    """
    def __init__(self, csv_gsheet):
        self.planilha = Planilha(csv_gsheet)

    def publish_notas(self, column):
        time.sleep(5)
        for nota in self.planilha.dataframe[column]:
            keyboard.write(str(nota).replace("nan", "0"))
            time.sleep(0.2)
            keyboard.press_and_release('tab')
            time.sleep(0.2)

    def publish_notas_by_pass(self, notas, tab_key='enter'):
        print("Imprimindo notas...")
        time.sleep(5)
        for nota in notas:
            keyboard.write(str(nota).replace("nan", "0"))
            time.sleep(0.2)
            keyboard.press_and_release(tab_key)
            time.sleep(0.2)

    def extract_equipes(self, equipes_csv_filename, columns=None):
        gsheet = Planilha(equipes_csv_filename)
        df = gsheet.dataframe

        if columns is None:
            columns = ['Representante', 'Integrante 1', 'Integerante 2', 'Integrante 3']
        notas = []
        for nome in self.planilha.dataframe["ALUNOS"]:
            nota = df.loc[df[columns].eq(nome).any(axis=1), 'Nota']
            notas.append(nota.item())
        return notas
