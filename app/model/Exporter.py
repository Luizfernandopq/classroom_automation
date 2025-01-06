from unidecode import unidecode

from app.model.Planilha import Planilha

""" Classe para pegar uma planilha do classroom com notas e escrever no googlesheets
    Por enquanto utilizo print_scores para inserir manualmente
"""

class Exporter:
    def __init__(self, csv_class, csv_gsheet):
        self.classroom = Planilha(csv_class)
        self.gsheets = Planilha(csv_gsheet)

    """Esta função está ajustada para a turma de labprog, talvez precise de atualizações em outras turmas
    """
    def print_scores(self):
        df_class = self.classroom.dataframe
        alunos = self.gsheets.dataframe["ALUNOS"]
        df_class["Nome"] = df_class["Nome"].apply(lambda x: unidecode(x)).astype(str)

        df_class["Sobrenome"] = df_class["Sobrenome"].apply(lambda x: '' if isinstance(x, float) else unidecode(x))
        for index in range(len(alunos)):
            match = self.match_names(alunos.iloc[index], df_class)
            if match == -1:
                # print("Aluno não encontrado: ", alunos.iloc[index])
                print("0")
                continue
            print(str(df_class["Nota"][match]).replace("nan", "").replace(".", ","))


    def match_names(self, aluno, df_class):
        count_match = 0
        indexes = []
        for index in range(len(df_class)):
            match = False
            names = []
            names.extend(df_class.iloc[index]["Nome"].upper().split(" "))
            names.extend(df_class.iloc[index]["Sobrenome"].upper().split(" "))
            for name in names:
                if name in aluno:
                    match = True
                else:
                    match = False
                    break
            if match:
                count_match += 1
                indexes.append(index)

        return self.choose_index(indexes)

    def choose_index(self, indexes):
        if not indexes:
            return -1
        elif len(indexes) > 1:
            # indexes[input()]
            return indexes[0]
        else:
            return indexes[0]