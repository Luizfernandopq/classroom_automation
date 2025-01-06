import time

from app.model.Assistant import Assistant
from app.model.Exporter import Exporter
from app.model.Planilha import Planilha

if __name__ == '__main__':
    # exporter = Exporter("Laboratório_4.csv", "Alunos-LabProg - 2024.2.csv")
    # exporter.print_scores()
    assistant = Assistant("Alunos-LabProg - 2024.2.csv")
    print("tudo pronto?")
    input()
    time.sleep(5)
    assistant.publish_notas("P2")
