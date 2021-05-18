class alunos_inscritos():

    Numero_aluno = 0
    Nome_Disciplina = ""   

    def __init__(self, Numero_Aluno, Nome_Disciplina):
        self.Numero_aluno = Numero_Aluno
        self.Nome_Disciplina = Nome_Disciplina
        pass
    
    def mostrar_alunos_inscritos(self,disciplina):
        if self.Nome_Disciplina == disciplina:
            print(self.Numero_aluno)
        pass
