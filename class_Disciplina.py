class disciplina():

    Nome_disciplina = ""

    
    def __init__(self, Nome_disciplina):
        self.Nome_disciplina = Nome_disciplina
        pass
    

    def mostrarNomeDisciplina(self, num):
        print(num, "-", self.Nome_disciplina)
        pass


