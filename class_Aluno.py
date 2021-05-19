class aluno():

    Numero_aluno = 0
    Nome_aluno = ""
    Morada_aluno = ""
    Idade_aluno = 0
    CC_aluno = 0
    

    def __init__(self, Numero_Aluno, Nome_Aluno, Morada_Aluno, Idade_Aluno, CC_Aluno):
        self.Numero_aluno = Numero_Aluno
        self.Nome_aluno = Nome_Aluno
        self.Morada_aluno = Morada_Aluno
        self.Idade_aluno = Idade_Aluno
        self.CC_aluno = CC_Aluno
        pass
    
    def mostrarAluno(self):
        print(self.Numero_aluno, "-", self.Nome_aluno)
        pass
    

