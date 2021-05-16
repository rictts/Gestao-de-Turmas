
# Componente Servidor - MAIN

#importa o modulo com funções da tabela disciplina
import BD_disciplina

#importa o modulo com funções da tabela disciplina
import BD_aluno


#Estabelece a conexão Socket
import socket
print("Arranque de servidor")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
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
    #Opção 1 - Criar Disciplina
    if msg.decode() == '1':
        print("Opção1-Criar Disciplina")
        msg = c.recv(1024)
        BD_disciplina.insert_disciplina(msg.decode())
    #Opção 4 - Criar Aluno
    if msg.decode() == '4':
        print("Opção4-Criar Aluno")
        msg = c.recv(1024)
        print (msg)
        BD_aluno.insert_aluno(msg.decode())
    #Opção 9 - Criar Professor
    if msg.decode() == '9':
        print("Opção9-Criar Professor")
        msg = c.recv(1024)
        print(msg)
        BD_professor.insert_professor(msg.decode())
        
        
            
    
