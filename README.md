🏫 Sistema de Gestão de Turmas (Cliente - Servidor)

Sistema em Python para gestão académica de turmas, alunos, professores e disciplinas. A aplicação utiliza uma arquitetura Cliente-Servidor baseada em comunicação de rede (Sockets) e persistência de dados em SQLite3.

📌 Funcionalidades

🖥️ Módulo Servidor (Gestao turmas Server.py)

Gestão da Base de Dados: Inicialização e estruturação do banco de dados Turmas.db.

Serviço de Escuta: Aguarda por ligações do cliente na porta/IP definidos no ficheiro de configuração.

Operações de BD:

Registo e consulta de Alunos.

Registo e consulta de Professores.

Registo e consulta de Disciplinas.

Associação de Alunos a Disciplinas/Turmas.

Associação de Professores a Disciplinas.

📱 Módulo Cliente (Gestao de Turmas Cliente.py)

Interface/Menu para interação do utilizador.

Envio de pedidos ao servidor para consulta, adição e edição de dados académicos.

Leitura dinâmica das configurações de ligação.

📂 Estrutura do Projeto

Gestao-de-Turmas/
├── Gestao turmas Server.py       # Script principal do Servidor
├── Gestao de Turmas Cliente.py    # Script principal do Cliente
│
├── cria_BD_Turmas.py             # Script de criação/inicialização do esquema de BD
├── Turmas.db                     # Ficheiro de base de dados SQLite
│
├── BD_aluno.py                   # Lógica de acessos à BD para Alunos
├── BD_professor.py               # Lógica de acessos à BD para Professores
├── BD_disciplina.py              # Lógica de acessos à BD para Disciplinas
├── BD_associa_aluno.py           # Inscrições de alunos em disciplinas
├── BD_associa_professor.py        # Atribuições de disciplinas a professores
│
├── class_Aluno.py                # Modelo/Classe Aluno
├── class_Professor.py            # Modelo/Classe Professor
├── class_Disciplina.py           # Modelo/Classe Disciplina
├── class_alunos_inscritos.py     # Modelo de relacionamento Aluno-Disciplina
├── class_professor_disciplina.py # Modelo de relacionamento Professor-Disciplina
│
├── conexacao.py                  # Gestão da conexão socket
├── conf_conexacao.py             # Leitura das configurações
├── conexao_conf.txt              # Configuração do Cliente (ex: IP 127.0.0.1)
├── conexao_server_conf.txt       # Configuração do Servidor (ex: IP localhost)
└── alunos.txt                    # Ficheiro auxiliar / importação inicial


🛠️ Tecnologias Utilizadas

Python 3.x

SQLite3 (Base de dados relacional leve)

Sockets / Networking (Comunicação Cliente-Servidor)

PyInstaller (Suporte a compilação via ficheiros .spec)

🚀 Como Executar o Projeto

1. Clonar o Repositório

git clone https://github.com/rictts/Gestao-de-Turmas.git
cd Gestao-de-Turmas


2. Configurar os IPs de Conexão

Certifica-te de que os ficheiros de configuração contêm os endereços IP corretos:

conexao_server_conf.txt: Endereço do servidor (ex: localhost ou 127.0.0.1).

conexao_conf.txt: Endereço IP ao qual o cliente se vai ligar.

3. Criar a Base de Dados

Antes de iniciar o servidor pela primeira vez, executa o script de criação da base de dados:

python cria_BD_Turmas.py


4. Iniciar o Servidor

Executa o ficheiro do servidor num terminal:

python "Gestao turmas Server.py"


5. Iniciar o Cliente

Noutro terminal (ou máquina na mesma rede), executa a aplicação cliente:

python "Gestao de Turmas Cliente.py"


📦 Executáveis (.exe)

O projeto inclui ficheiros .spec (Gestao turmas Server.spec e Gestao de Turmas Cliente.spec) para compilar os scripts em executáveis independentes recorrendo ao PyInstaller:

pip install pyinstaller
pyinstaller "Gestao turmas Server.spec"
pyinstaller "Gestao de Turmas Cliente.spec"


Os executáveis compilados ficarão disponíveis na pasta dist/.
