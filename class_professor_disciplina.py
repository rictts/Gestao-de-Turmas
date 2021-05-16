class professor_disciplina():

    Numero_professor = 0
    Nome_Disciplina = ""   

    def __init__(self, Numero_Professor, Nome_Disciplina):
        self.Numero_professor = Numero_Professor
        self.Nome_Disciplina = Nome_Disciplina
        pass
    
    def mostrar_professor_disciplina(self):
        print(self.Numero_professor)
        print(self.Nome_Disciplina)
        pass
