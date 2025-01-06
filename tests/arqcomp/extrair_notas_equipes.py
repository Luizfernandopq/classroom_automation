from app.model.Assistant import Assistant

if __name__ == '__main__':
    assistente = Assistant("Alunos-ArqComp - 2024.2.csv")
    # notas = assistente.extrair_equipes("Alunos-ArqComp - Equipe AV2.csv")
    # assistente.publicar_notas_by_pass(notas)
    assistente.publish_notas("Prova")
