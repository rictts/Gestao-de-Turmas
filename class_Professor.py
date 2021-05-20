class professor():

    Numero_professor = 0
    Nome_professor = ""
    Morada_professor = ""
    Idade_professor = 0
    Categoria_profissional = ""
    Anos_experiencia = 0
    
    

    def __init__(self, Numero_Professor, Nome_Professor, Morada_Professor, Idade_Professor, Categoria_profissional,Anos_experiencia ):
        self.Numero_professor = Numero_Professor
        self.Nome_professor = Nome_Professor
        self.Morada_professor = Morada_Professor
        self.Idade_professor = Idade_Professor
        self.Categoria_profissional = Categoria_profissional
        self.Anos_experiencia = Anos_experiencia
        pass
    
    def mostrarProfessor(self):
        print(self.Numero_professor, "-", self.Nome_professor)
        pass

    def devolveProfessor(self):
        return self.Numero_professor
        pass
