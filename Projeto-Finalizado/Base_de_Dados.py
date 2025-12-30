import sqlite3
from datetime import datetime

# Classe responsável por interagir com a base de dados SQLite
class BaseDados:
    def __init__(self):
        self.nome_bd = 'Base_de_Dados.db'  # Nome do ficheiro da base de dados
        self.criar_tabelas()  # Cria as tabelas na inicialização se não existirem

    # Método para estabelecer ligação à base de dados
    def conectar_base_de_dados(self):
        return sqlite3.connect(self.nome_bd)

    # Método que cria as tabelas 'Utilizadores' e 'Historico' caso não existam
    def criar_tabelas(self):
        conn = self.conectar_base_de_dados()
        cursor = conn.cursor()

        # Criação da tabela de utilizadores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Utilizadores (
                ID INTEGER PRIMARY KEY,
                Nome_de_Utilizador TEXT UNIQUE,
                Senha TEXT NOT NULL,
                UID INTEGER UNIQUE,
                Email TEXT UNIQUE,
                Localizacao TEXT
            )
        ''')

        # Criação da tabela de histórico associada a cada utilizador via UID
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Historico (
                ID INTEGER PRIMARY KEY,
                Data TEXT NOT NULL,
                UID INTEGER,
                Localizacao TEXT NOT NULL,
                Temperatura_Min REAL,
                Temperatura_Max REAL,
                Precipitacao REAL,
                Descricao TEXT,
                Tipo_Procura TEXT,
                FOREIGN KEY(UID) REFERENCES Utilizadores(UID)
            )
        ''')

        conn.commit()  # Confirma as alterações
        conn.close()   # Fecha a ligação

    # Método para inserir um novo utilizador na base de dados
    def inserir_utilizador(self, utilizador):
        if not utilizador:
            return False  # Verifica se o objeto utilizador é válido

        # Verifica se o utilizador já existe (por nome, UID ou e-mail)
        if self.verificar_existencia(utilizador, utilizador.mail):
            return False  # Se já existe, não insere na base de dados

        conn = self.conectar_base_de_dados()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Utilizadores (Nome_de_Utilizador, Senha, UID, Email, Localizacao)
            VALUES (?, ?, ?, ?, ?)
        ''', (utilizador.nome, utilizador.senha, utilizador.uid, utilizador.mail, utilizador.localizacao))
        conn.commit()
        conn.close()
        return True

    # Verifica se já existe um utilizador com o mesmo nome, UID ou email
    def verificar_existencia(self, utilizador, email):
        conn = self.conectar_base_de_dados()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 1 FROM Utilizadores
            WHERE Nome_de_Utilizador = ? OR UID = ? OR Email = ?
        ''', (utilizador.nome, utilizador.uid, email))
        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None  # Retorna True se encontrou resultado

    # Verifica se o login do utilizador é válido (nome/UID + senha)
    def login(self, utilizador):
        conn = self.conectar_base_de_dados()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM Utilizadores WHERE (Nome_de_Utilizador = ? OR UID = ?) AND Senha = ?
        ''', (utilizador.nome, utilizador.nome, utilizador.senha))
        resultado = cursor.fetchone()

        # Se não encontrou por nome ou UID, tenta caso especial: UID == senha (ambos numéricos)
        if not resultado:
            try:
                uid = int(utilizador.nome)
                if str(uid) == utilizador.senha:
                    cursor.execute('SELECT * FROM Utilizadores WHERE UID = ?', (uid,))
                    resultado = cursor.fetchone()
            except ValueError:
                pass  # Se não for número, ignora

        conn.close()
        return resultado is not None  # True se login for bem-sucedido

    # Verifica se já existe um utilizador com determinado e-mail
    def verificar_mail(self, email):
        conn = self.conectar_base_de_dados()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Utilizadores WHERE Email = ?", (email,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None

    # Altera a senha de um utilizador com base no seu e-mail
    def alterar_senha(self, email, nova_senha):
        conn = self.conectar_base_de_dados()
        cursor = conn.cursor()
        cursor.execute("UPDATE Utilizadores SET Senha = ? WHERE Email = ?", (nova_senha, email))
        conn.commit()
        conn.close()

    # Obtém dados do utilizador autenticado: UID, nome e localização
    def obter_dados_utilizador(self, utilizador):
        conn = self.conectar_base_de_dados()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT UID, Nome_de_Utilizador, Localizacao
            FROM Utilizadores
            WHERE (Nome_de_Utilizador = ? OR UID = ?) AND Senha = ?
        ''', (utilizador.nome, utilizador.nome, utilizador.senha))
        resultado = cursor.fetchone()
        conn.close()
        return resultado

    # Guarda um registo de histórico de pesquisa meteorológica do utilizador
    def guardar_historico(self, uid, historico):
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Data e hora atual
        conn = self.conectar_base_de_dados()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Historico (Data, UID, Localizacao, Temperatura_Min, Temperatura_Max, Precipitacao, Descricao, Tipo_Procura)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data_atual, uid, historico.localizacao, historico.temperatura_min,
            historico.temperatura_max, historico.precipitacao,
            historico.descricao, historico.tipo_procura
        ))

        conn.commit()
        conn.close()

    # Obtém os últimos registos (últimos 30 dias) do histórico do utilizador com base no tipo de procura
    def obter_ultimos_registos(self, uid, tipo_procura):
        conn = self.conectar_base_de_dados()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT Temperatura_Min, Temperatura_Max, Precipitacao
                FROM Historico
                WHERE UID = ? AND Tipo_Procura = ? AND date(Data) >= date('now', '-30 days')
                ORDER BY Data DESC
            ''', (uid, tipo_procura))

            return cursor.fetchall()  # Retorna lista de tuplas com os dados
        except Exception:
            return []
        finally:
            conn.close()

