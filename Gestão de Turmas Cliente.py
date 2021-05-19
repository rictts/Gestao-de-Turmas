# ***************** Componente Cliente - MAIN ************************
import socket
import os

# Define a ligação ao servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lê do ficheiro de configuração o IP do servidor
f = open("conexao_conf.txt", "r")
for linha in f:
    valores= linha.split()
    host = valores[0]
f.close()
porto=50000
server_address=(host,porto)
try:
    s.connect(server_address)
except:
    print("Não foi possivel estabelecer ligação ao servidor")
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
    #msg = s.recv(1024)
    #if msg.decode() == "OK":
    Nova_disciplina = class_Disciplina.disciplina(Nome_disciplina)
    lista_disciplinas.append(Nova_disciplina)
    #else:
        #print ("Ocorreu um erro a inserir a disciplina. Tente novamente e verifique se a disciplina já existe")
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
    escolha = input("Escolha o nome da Disciplina que quer eliminar: ")
    disc = class_Disciplina.disciplina(escolha)
    print(disc.Nome_disciplina) 
    indice=lista_disciplinas.index(disc.Nome_Disciplina)
    #try:
    lista_disciplinas.pop(indice)
    #except:
        #print("Ocorreu um erro.")

    s.send(str.encode("3"))
    s.send(str.encode(escolha))
    listarDisciplina()
    pass

# *********** Funções da aluno  ************
#Módulo com a classe aluno
import class_Aluno
import class_alunos_inscritos

def criarAluno():
    lista_aluno_aux = list()
    
    Numero_aluno = int(input("Inserir o numero do aluno: "))
    Nome_aluno = input("Inserir o nome do aluno: ")
    Morada_aluno = input("Inserir a morada do aluno: ")
    Idade_aluno = int(input("Inserir a idade do aluno: "))
    CC_aluno = int(input("Inserir o cartao de cidadao do aluno: "))
       
    Novo_Aluno = class_Aluno.aluno(Numero_aluno, Nome_aluno, Morada_aluno, Idade_aluno, CC_aluno )
    lista_alunos.append(Novo_Aluno)

    lista_aluno_aux.append(Numero_aluno)
    lista_aluno_aux.append(Nome_aluno)
    
    string = str(lista_aluno_aux)
    s.send(str.encode("4"))
    s.send(str.encode(string))
    pass

def listarAluno():
    print ("Os alunos existentes são:")
    for cada_aluno in lista_alunos:
        cada_aluno.mostrarAluno()
    pass

def inscreverAluno():
    lista_inscrever_aux = list()
    
    listarDisciplina()
    disc_inscrita = input("Escolha o nome da disciplina onde quer inscrever o aluno: ")
    listarAluno()
    aluno_inscrito = int(input("Escolha o numero de aluno que quer inscrever: "))

    Novo_aluno_inscrito = class_alunos_inscritos.alunos_inscritos(aluno_inscrito, disc_inscrita)
    lista_alunos_inscritos.append(Novo_aluno_inscrito)

    lista_inscrever_aux.append(aluno_inscrito)
    lista_inscrever_aux.append(disc_inscrita)
    
    string = str(lista_inscrever_aux)
    s.send(str.encode("5"))
    s.send(str.encode(string))
    
    pass

def eliminarAluno():
    listarAluno()
    try:
        escolha = int(input("Indique o numero do aluno a eliminar: "))
        string = str(escolha)
        escolha = escolha - 1
    except:
        print("Ocorreu um erro, tente novamente. Verifique se introduziu corretamente os dados")
    try:
        lista_alunos.pop(escolha)
        lista_alunos_inscritos.pop(escolha)
    except:
        print("Ocorreu um erro ao eliminar o aluno da lista")

    s.send(str.encode("6"))
    s.send(str.encode(string))
    
    pass

def listarAlunoDisciplina():
    listarDisciplina()
    escolha = input("Escolha o nome da Disciplina que quer ver os alunos: ")

    print ("Os alunos inscritos são:")
    for cada_aluno_inscrito in lista_alunos_inscritos:
        cada_aluno_inscrito.mostrar_alunos_inscritos(escolha)
    pass

# *********** Funções da professor  ************
#Módulo com a classe professor
import class_Professor
import class_professor_disciplina

def criarProfessor():
    lista_prof_aux = list()

    Numero_professor = int(input("Inserir o numero do professor: "))
    Nome_professor = input("Inserir o nome do professor: ")
    Morada_professor = input("Inserir a morada do professor: ")
    Idade_professor = int(input("Inserir a idade do professor: "))
    Categoria_profissional = input("Inserira a categoria profissional: ")
    Anos_experiencia = int(input("Inserir anos de experiencia do professor: "))


    Novo_Professor = class_Professor.professor(Numero_professor, Nome_professor, Morada_professor, Idade_professor, Categoria_profissional, Anos_experiencia)
    lista_professores.append(Novo_Professor)


    lista_prof_aux.append(Numero_professor)
    lista_prof_aux.append(Nome_professor)
    string = str(lista_prof_aux)
    s.send(str.encode("9"))
    s.send(str.encode(string))
    pass

def listarProfessor():
    print ("Os professores existentes são:")
    for cada_professor in lista_professores:
        cada_professor.mostrarProfessor()
    pass

def adicionarProfessorDisciplina():
    lista_assoc_aux = list()

    listarDisciplina()
    escolha_disc = input("Escolha o nome da Disciplina que quer adicionar o professor: ")

    listarProfessor()
    escolha_prof = int(input("Escolha o numero do professor que quer adicionar: "))
    
    Novo_professor_disciplina = class_professor_disciplina.professor_disciplina(escolha_prof, escolha_disc)
    lista_professores_disciplina.append(Novo_professor_disciplina)

    lista_assoc_aux.append(escolha_prof)
    lista_assoc_aux.append(escolha_disc)
    string = str(lista_assoc_aux)
    s.send(str.encode("10"))
    s.send(str.encode(string))
    
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
s.send(str.encode("start"))

#vai receber o resultado do select da tabela alunos
msg = s.recv(1024)
msg = eval(msg)
for linha in msg:
    Novo_Aluno = class_Aluno.aluno(linha[0], linha[1], linha[2], linha[3], linha[4])
    lista_alunos.append(Novo_Aluno)

#vai receber o resultado do select da tabela disciplina
msg = s.recv(1024)
msg = eval(msg)
for linha in msg:
    Nova_Disciplina = class_Disciplina.disciplina(linha[0])
    lista_disciplinas.append(Nova_Disciplina)

#vai receber o resultado do select da tabela professor
msg = s.recv(1024)
msg = eval(msg)
for linha in msg:
    Novo_Professor = class_Professor.professor(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
    lista_professores.append(Novo_Professor)

#vai receber o resultado do select da tabela associa alunos
msg = s.recv(1024)
msg = eval(msg)
for linha in msg:
    Novo_aluno_inscrito = class_alunos_inscritos.alunos_inscritos(linha[0], linha[1])
    lista_alunos_inscritos.append(Novo_aluno_inscrito)

#vai receber o resultado do select da tabela professor
msg = s.recv(1024)
msg = eval(msg)
for linha in msg:
    Novo_professor_disciplina = class_professor_disciplina.professor_disciplina(linha[0], linha[1])
    lista_professores_disciplina.append(Novo_professor_disciplina)

# *** Escreve o menu e recebe a opção escolhida pelo utilizador ***
os.system("cls")
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
