# Componente Servidor - MAIN

#importa o modulo com funções da tabela disciplina
import BD_disciplina
#importa o modulo com funções da tabela aluno
import BD_aluno
#importa o modulo com funções da tabela professor
import BD_professor
#importa o modulo com funções da tabela associa_aluno_disciplina
import BD_associa_aluno
#importa o modulo com funções da tabela associa_professor
import BD_associa_professor


#Estabelece a conexão Socket
import socket
print("Arranque de servidor")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# lê do ficheiro de configuração o IP do servidor
f = open("conexao_server_conf.txt", "r")
for linha in f:
    valores= linha.split()
    ip = valores[0]
f.close()
porto = 50000
server_address =(ip,porto)
s.bind(server_address)

#o Servidor fica à esculta de receber mensagens
s.listen()
print("Servidor à escuta")

#o servidor aceita a conexão
c, addr = s.accept()
print("Servidor conectado com",addr)



#Recebe as mensagens
while True:
    msg = c.recv(1024)
    if not msg:
            print("vou fechar a conexão")
            c.close()
            break
    #START - Acede às tabelas e carrega as listas
    if msg.decode() == 'start':
        #No arranque da aplicação cliente envia para o cliente os dados da tabela aluno
         lista_aluno = list()
         lista_aluno = BD_aluno.select_aluno()
         string = str(lista_aluno)
         c.send(str.encode(string))
        #No arranque da aplicação cliente envia para o cliente os dados da tabela disciplina
         lista_disciplina = list()
         lista_disciplina = BD_disciplina.select_disciplina()
         string = str(lista_disciplina)
         c.send(str.encode(string))
        #No arranque da aplicação cliente envia para o cliente os dados da tabela professor
         lista_professor = list()
         lista_professor = BD_professor.select_professor()
         string = str(lista_professor)
         c.send(str.encode(string))
         
         #No arranque da aplicação cliente envia para o cliente os dados da tabela associa aluno
         lista_associa_aluno = list()
         lista_associa_aluno = BD_associa_aluno.select_associa_aluno()
         string = str(lista_associa_aluno)
         c.send(str.encode(string))

         #No arranque da aplicação cliente envia para o cliente os dados da tabela associa professor
         lista_associa_professor = list()
         lista_associa_professor = BD_associa_professor.select_associa_professor()
         string = str(lista_associa_professor)
         c.send(str.encode(string))
        
    
    #Opção 1 - Criar Disciplina
    elif msg.decode() == '1':
        print("Opção1-Criar Disciplina")
        msg = c.recv(1024)
        #try:
        BD_disciplina.insert_disciplina(msg.decode())
            #s.send(str.encode("OK"))
        #except:
            #s.send(str.encode("ERRO"))
            
    #Opção 3 - Eliminar Disciplina
    elif msg.decode() == '3':
        print("Opção3-Eliminar Disciplina")
        msg = c.recv(1024)
        #try:
        BD_disciplina.delete_disciplina(msg.decode())
            #s.send(str.encode("OK"))
        #except:
            #s.send(str.encode("ERRO"))
            
    #Opção 4 - Criar Aluno
    elif msg.decode() == '4':
        print("Opção4-Criar Aluno")
        msg = c.recv(1024)
        msg =eval(msg)
        BD_aluno.insert_aluno(msg)
        
    #Opção 5 - Inscrever Aluno
    elif msg.decode() == '5':
        print("Opção5-Inscrever Aluno")
        msg = c.recv(1024)
        msg =eval(msg)
        BD_associa_aluno.insert_associa_aluno(msg)

    #Opção 6 - Eliminar Aluno
    elif msg.decode() == '6':
        print("Opção6-Eliminar Aluno")
        msg = c.recv(1024)
        #try:
        BD_aluno.delete_aluno(msg.decode())
        BD_associa_aluno.delete_associa_aluno(msg.decode())
            #s.send(str.encode("OK"))
        #except:
            #s.send(str.encode("ERRO"))

      
    #Opção 9 - Criar Professor
    elif msg.decode() == '9':
        print("Opção9-Criar Professor")
        msg = c.recv(1024)
        msg =eval(msg)
        BD_professor.insert_professor(msg)

    #Opção 10 - Associa Professor
    elif msg.decode() == '10':
        print("Opção10-Associa Professor")
        msg = c.recv(1024)
        msg =eval(msg)
        BD_associa_professor.insert_associa_professor(msg)        
        
        
            
    
