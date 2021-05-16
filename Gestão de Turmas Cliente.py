import socket

# Componente Cliente - MAIN


#Estabelece a ligação ao servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='127.0.0.1'
porto=50000
#host = "192.168.1.125"
#porto = 5525
server_address=(host,porto)

s.connect(server_address)

#Define as listas e outras variaveis
escolha = 100
lista_alunos = list()
lista_professores = list()
lista_disciplinas = list()
lista_alunos_inscritos = list()
lista_professores_disciplina = list()


# *********** Funções da disciplina  ************
#Módulo com a classe disciplina
import class_Disciplina

def criarDisciplina():
    Nome_disciplina = input("Inserir o nome da disciplina: ")

    s.send(str.encode("1"))
    s.send(str.encode(Nome_disciplina))

    Nova_disciplina = class_Disciplina.disciplina(Nome_disciplina)
    lista_disciplinas.append(Nova_disciplina)
    pass

def listarDisciplina():
    contador = 0
    print ("As disciplinas existentes são:")
    for cada_disciplina in lista_disciplinas:
        cada_disciplina.mostrarNomeDisciplina(contador)
        contador = contador + 1
    pass

def eliminarDisciplina():
    listarDisciplina()
    escolha = int(input("Escolha a Disciplina que quer eliminar: "))
    try:
        lista_disciplinas.pop(escolha)
    except:
        print("Ocorreu um erro.")
    pass

# *********** Funções da aluno  ************
#Módulo com a classe aluno
import class_Aluno
import class_alunos_inscritos

def criarAluno():
    Numero_aluno = int(input("Inserir o numero do aluno: "))
    Nome_aluno = input("Inserir o nome do aluno: ")
    Morada_aluno = input("Inserir a morada do aluno: ")
    Idade_aluno = int(input("Inserir a idade do aluno: "))
    CC_aluno = int(input("Inserir o cartao de cidadao do aluno: "))
    s.send(str.encode("4"))
    string = str(Numero_aluno)
    s.send(str.encode(string))
    s.send(str.encode(Nome_aluno))
        
    Novo_Aluno = class_Aluno.aluno(Numero_aluno, Nome_aluno, Morada_aluno, Idade_aluno, CC_aluno )
    lista_alunos.append(Novo_Aluno)
    pass

def listarAluno():
    print ("Os alunos existentes são:")
    for cada_aluno in lista_alunos:
        cada_aluno.mostrarAluno()
    pass

def inscreverAluno():
    listarDisciplina()
    disc_inscrita = input("Escolha o nome da disciplina onde quer inscrever o aluno: ")
    listarAluno()
    aluno_inscrito = int(input("Escolha o numero de aluno que quer inscrever: "))

    Novo_aluno_inscrito = class_alunos_inscritos.alunos_inscritos(aluno_inscrito, disc_inscrita)
    lista_alunos_inscritos.append(Novo_aluno_inscrito)
    pass

def eliminarAluno():
    listarAluno()
    escolha = int(input("Elimina um aluno: "))
    escolha = escolha - 1
    try:
        lista_alunos.pop(escolha)
    except:
        print("Ocorreu um erro.")
    pass

def listarAlunoDisciplina():
    listarDisciplina()
    escolha = input("Escolha o nome da Disciplina que quer ver os alunos: ")

    print ("Os alunos inscritos são:")
    for cada_aluno_inscrito in lista_alunos_inscritos:
        cada_aluno_inscrito.mostrar_alunos_inscritos()
    pass

# *********** Funções da professor  ************
#Módulo com a classe professor
import class_Professor
import class_professor_disciplina

def criarProfessor():
    Numero_professor = int(input("Inserir o numero do professor: "))
    Nome_professor = input("Inserir o nome do professor: ")
    Morada_professor = input("Inserir a morada do professor: ")
    Idade_professor = int(input("Inserir a idade do professor: "))
    Categoria_profissional = input("Inserira a categoria profissional: ")
    Anos_experiencia = int(input("Inserir anos de experiencia do professor: "))
    s.send(str.encode("9"))
    string = str(Numero_professor)
    s.send(str.encode(string))
    s.send(str.encode(Nome_professor))

    Novo_Professor = class_Professor.professor(Numero_professor, Nome_professor, Morada_professor, Idade_professor, Categoria_profissional, Anos_experiencia)
    lista_professores.append(Novo_Professor)
    pass

def listarProfessor():
    print ("Os professores existentes são:")
    for cada_professor in lista_professores:
        cada_professor.mostrarProfessor()
    pass

def adicionarProfessorDisciplina():
    listarDisciplina()
    escolha_disc = input("Escolha o nome da Disciplina que quer adicionar o professor: ")

    listarProfessor()
    escolha_prof = int(input("Escolha o numero do professor que quer adicionar: "))
    
    Novo_professor_disciplina = class_professor_disciplina.professor_disciplina(escolha_prof, escolha_disc)
    lista_professores_disciplina.append(Novo_professor_disciplina)
    pass  
  
def ImportarFicheiroAlunos():
    ficheiro = input("Indique o nome do ficheiro a importar: ")
    f = open(ficheiro, "r")
    listarDisciplina()
    escolha_disc = input("Escolha o nome da Disciplina que quer associar os alunos do ficheiro: ")
    for linha in f:
        print(linha)
        Novo_aluno_inscrito = class_alunos_inscritos.alunos_inscritos(linha, escolha_disc)
        lista_alunos_inscritos.append(Novo_aluno_inscrito)
    f.close()
    pass

# *** Acede ao servidor e carrega as listas

# *** Escreve o menu e recebe a opção escolhida pelo utilizador ***
while escolha !=0:
                      
              print("1 - Criar Disciplina")
              print("2 - Listar Disciplina")
              print("3 - Eliminar Disciplina")
              print("4 - Criar Aluno")
              print("5 - Inscrever Aluno")
              print("6 - Eliminar Aluno")
              print("7 - Listar Alunos")
              print("8 - Listar Alunos inscritos numa dada disciplina")
              print("9 - Criar Professor")
              print("10 - Adicionar professor a uma disciplina")
              print("11 - Importar alunos de um ficheiro")
              
              print("0 -Sair")
              escolha = int(input("escolha: "))
              if escolha == 1:
                  criarDisciplina()
              if escolha == 2:
                  listarDisciplina()
              if escolha == 3:
                  eliminarDisciplina()
              if escolha == 4:
                  criarAluno()
              if escolha == 5:
                  inscreverAluno()
              if escolha == 6:
                  eliminarAluno()
              if escolha == 7:
                  listarAluno()
              if escolha == 8:
                  listarAlunoDisciplina()
              if escolha == 9:
                  criarProfessor()
              if escolha == 10:
                  adicionarProfessorDisciplina()
              if escolha == 11:
                  ImportarFicheiroAlunos()
