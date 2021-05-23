# ***************** Componente Cliente - MAIN ************************
import socket
import os
import time

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
    flag = 0
    for cada_disciplina in lista_disciplinas:
        disciplina = cada_disciplina.devolveNomeDisciplina()
        if disciplina == Nome_disciplina:
            flag = 1
    if flag == 1:
        print("A disciplina que introduziu já existe.")
    else:
        s.send(str.encode("1"))
        s.send(str.encode(Nome_disciplina))
    
        Nova_disciplina = class_Disciplina.disciplina(Nome_disciplina)
        lista_disciplinas.append(Nova_disciplina)
    pass

def listarDisciplina():
    contador = 1
    print ("As disciplinas existentes são:")
    for cada_disciplina in lista_disciplinas:
        cada_disciplina.mostrarNomeDisciplina(contador)
        contador = contador + 1
    pass

def eliminarDisciplina():
    listarDisciplina()
    try:
        escolha = int(input("Escolha o nome da Disciplina que quer eliminar: "))
        escolha = escolha - 1
        contador = 0
        for cada_disciplina in lista_disciplinas:
            if contador == escolha:
                disciplina = cada_disciplina.devolveNomeDisciplina()
                break
            contador = contador + 1

        lista_disciplinas.pop(escolha)

        s.send(str.encode("3"))
        s.send(str.encode(disciplina))
        listarDisciplina()
    except:
        print("Ocorreu um erro, verifique se introduziu um numero válido")
    pass

# *********** Funções da aluno  ************
#Módulo com a classe aluno
import class_Aluno
import class_alunos_inscritos

def criarAluno():
    lista_aluno_aux = list()
    try:
        Numero_aluno = int(input("Inserir o numero do aluno: "))
        flag = 0
        for cada_aluno in lista_alunos:
            aluno = cada_aluno.devolveAluno()
            if aluno == Numero_aluno:
                flag = 1
        if flag == 1:
            print("O aluno que introduziu já existe.")
        else:
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
    except:
        print("Ocorreu um erro, verifique se introduziu corretamente os dados do aluno")
    pass

def listarAluno():
    print ("Os alunos existentes são:")
    for cada_aluno in lista_alunos:
        cada_aluno.mostrarAluno()
    pass

def inscreverAluno():
    lista_inscrever_aux = list()

    try:
        listarDisciplina()
        disc_inscrita = input("Escolha o nome da disciplina onde quer inscrever o aluno: ")
        flag = 0
        for cada_disciplina in lista_disciplinas:
            disciplina = cada_disciplina.devolveNomeDisciplina()
            if disciplina == disc_inscrita:
                flag = 1
        if flag == 0:
            print("Disciplina não existe.")
        else:
            listarAluno()
            aluno_inscrito = int(input("Escolha o numero de aluno que quer inscrever: "))

            flag = 0
            for cada_aluno in lista_alunos:
                aluno = cada_aluno.devolveAluno()
                if aluno == aluno_inscrito:
                    flag = 1
            if flag == 0:
                print("Aluno não existe.")
            else:
                Novo_aluno_inscrito = class_alunos_inscritos.alunos_inscritos(aluno_inscrito, disc_inscrita)
                lista_alunos_inscritos.append(Novo_aluno_inscrito)

                lista_inscrever_aux.append(aluno_inscrito)
                lista_inscrever_aux.append(disc_inscrita)
                
                string = str(lista_inscrever_aux)
                s.send(str.encode("5"))
                s.send(str.encode(string))
    except:
        print("Ocorreu um erro, verifique se introduziu um numero do aluno inscrito bem")
    pass

def eliminarAluno():
    listarAluno()
    try:
        escolha = int(input("Indique o numero do aluno a eliminar: "))
        string = str(escolha)
        escolha = escolha - 1
        
        lista_alunos.pop(escolha)
        lista_alunos_inscritos.pop(escolha)
    
        s.send(str.encode("6"))
        s.send(str.encode(string))
    except:
        print("Ocorreu um erro, verifique se introduziu corretamente os dados")    
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
    try:
        Numero_professor = int(input("Inserir o numero do professor: "))
        flag = 0
        for cada_professor in lista_professores:
            professor = cada_professor.devolveProfessor()
            if professor == Numero_professor:
                flag = 1
        if flag == 1:
            print("O professor que introduziu já existe.")
        else:
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
    except:
        print("Ocorreu um erro, verifique se introduziu corretamente os dados do professor")
    pass

def listarProfessor():
    print ("Os professores existentes são:")
    for cada_professor in lista_professores:
        cada_professor.mostrarProfessor()
    pass

def adicionarProfessorDisciplina():
    lista_assoc_aux = list()
    try:
        listarDisciplina()
        escolha_disc = input("Escolha o nome da Disciplina que quer adicionar o professor: ")
        flag = 0
        for cada_disciplina in lista_disciplinas:
            disciplina = cada_disciplina.devolveNomeDisciplina()
            if disciplina == escolha_disc:
                flag = 1
        if flag == 1:
            print("A disciplina que introduziu já existe.")
        else:
            Novo_professor_disciplina = class_professor_disciplina.professor_disciplina(escolha_prof, escolha_disc)
            lista_professores_disciplina.append(Novo_professor_disciplina)

            lista_assoc_aux.append(escolha_prof)
            lista_assoc_aux.append(escolha_disc)
            string = str(lista_assoc_aux)
            s.send(str.encode("10"))
            s.send(str.encode(string))
    except:
        print("Ocorreu um erro, verifique se introduziu corretamente o numero do professor")
    pass
  
def ImportarFicheiroAlunos():
    lista_aux = list()
    try:
        ficheiro = input("Indique o nome do ficheiro a importar: ")
        f = open(ficheiro, "r")
        listarDisciplina()
        escolha_disc = input("Escolha o nome da Disciplina que quer associar os alunos do ficheiro: ")
        flag = 0
        for cada_disciplina in lista_disciplinas:
            disciplina = cada_disciplina.devolveNomeDisciplina()
            if disciplina == escolha_disc:
                flag = 1
        if flag == 0:
            print("A disciplina não existe.")
        else:
            for linha in f:
                aluno = int(linha)
                print(aluno)

                Novo_aluno_inscrito = class_alunos_inscritos.alunos_inscritos(aluno, escolha_disc)
                lista_alunos_inscritos.append(Novo_aluno_inscrito)
                
                lista_aux.clear()
                lista_aux.append(aluno)
                lista_aux.append(escolha_disc)
                    
                string = str(lista_aux)
                s.send(str.encode("5"))
                time.sleep(2)
                print(string)
                s.send(str.encode(string))
                time.sleep(2)

                lista_aux.clear()
                
                
        f.close()
    except:
        print("Ocorreu um erro, verifique se introduziu corretamente o nome do ficheiro")
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
              try:
                  escolha = int(input("escolha: "))
                  if escolha == 1:
                      os.system("cls")
                      criarDisciplina()
                      input("Pressione uma tecla para voltar ao menu.")
                      os.system("cls")
                  if escolha == 2:
                      os.system("cls")
                      listarDisciplina()
                      input("Pressione uma tecla para voltar ao menu. ")
                      os.system("cls")
                  if escolha == 3:
                      os.system("cls")
                      eliminarDisciplina()
                      input("Pressione uma tecla para voltar ao menu.")
                      os.system("cls")
                  if escolha == 4:
                      os.system("cls")
                      criarAluno()
                      input("Pressione uma tecla para voltar ao menu.")
                      os.system("cls")
                  if escolha == 5:
                      os.system("cls")
                      inscreverAluno()
                      input("Pressione uma tecla para voltar ao menu.")
                      os.system("cls")
                  if escolha == 6:
                      os.system("cls")
                      eliminarAluno()
                      input("Pressione uma tecla para voltar ao menu.")
                      os.system("cls")
                  if escolha == 7:
                      os.system("cls")
                      listarAluno()
                      input("Pressione uma tecla para voltar ao menu.")
                      os.system("cls")
                  if escolha == 8:
                      os.system("cls")
                      listarAlunoDisciplina()
                      input("Pressione uma tecla para voltar ao menu.")
                      os.system("cls")
                  if escolha == 9:
                      os.system("cls")
                      criarProfessor()
                      os.system("cls")
                      input("Pressione uma tecla para voltar ao menu.")
                      os.system("cls")
                  if escolha == 10:
                      os.system("cls")
                      adicionarProfessorDisciplina()
                      input("Pressione uma tecla para voltar ao menu. ")
                      os.system("cls")
                  if escolha == 11:
                      os.system("cls")
                      ImportarFicheiroAlunos()
                      input("Pressione uma tecla para voltar ao menu.")
                      os.system("cls")
              except:
                    print("Ocorreu um erro, verifique se introduziu a opção correta")
