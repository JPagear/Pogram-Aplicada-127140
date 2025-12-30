import customtkinter as ctk


class CaixaInformacoes:
    def __init__(self, frame):
        self.frame = frame  # Guarda o frame onde a caixa de texto será colocada
        self.textbox = None  # Inicializa a variável da caixa de texto como None
        self.criar_caixa_texto()  # Chama o método para criar e mostrar a caixa de texto

    def criar_caixa_texto(self):
        # Cria uma CTkTextbox dentro do frame fornecido
        self.textbox = ctk.CTkTextbox(
            self.frame,
            width=300, height=350,
            corner_radius=10,
            border_width=2,
            border_color="white",
            wrap="word",
            font=("Segoe UI", 12)
        )
        self.textbox.place(relx=0.5, rely=0.5, anchor="center")

        self.inserir_texto()

    def inserir_texto(self):
        # Insere um cabeçalho de boas-vindas
        self.textbox.insert("end", "                                Bem-Vindo!\n\n")

        # Insere a descrição da aplicação e os autores
        self.textbox.insert("end",
                            "Weather2Travel é uma aplicação desenvolvida no âmbito da unidade curricular de "
                            "Programação Aplicada, do curso de Redes e Sistemas Informáticos da Escola Superior de "
                            "Tecnologia e Gestão de Águeda – Universidade de "
                            "Aveiro, no ano letivo 2024/2025.\n\nCriada pelos alunos:\nRodrigo Marques - 127829\nGlória Henriques - 120843\n"
                            "João Botelho - 126991\nJoão Almeida - 127140\n\nAplicação permite a autenticação de utilizadores via RFID "
                            "ou pelos métodos tradicionais de login, e "
                            "apresenta a previsão meteorológica da cidade de origem do utilizador, com dados fornecidos "
                            "pela API do IPMA.\n\nEste projeto representa a consolidação prática de vários conceitos "
                            "fundamentais da programação orientada a objetos, integração de sistemas, gestão de base de "
                            "dados e desenvolvimento de interfaces gráficas, refletindo o esforço colaborativo e o "
                            "compromisso académico dos seus autores.\n\n"
                            )

        # Insere a secção de notas importantes para o utilizador
        self.textbox.insert("end",
                            "=================================\n"
                            "                            Notas a Reter\n"
                            "=================================\n"
                            "Ao criar conta, tem em Atenção os cuidados a ter em alguns tópicos.\n\n"
                            "Senha - A sua senha deve conter:\n"
                            "-> Pelo menos 8 caracteres;\n"
                            "-> Pelo menos uma letra maiúscula;\n"
                            "-> Pelo menos uma letra minúscula;\n"
                            "-> Pelo menos um número;\n\n"
                            "Caso queira Iniciar Sessão apenas com UID, ao criar conta preencha os campos UID e Senha "
                            "com o UID. Após criar a conta será possivel Iniciar Sessão apenas com UID no campo "
                            "Nome de Utilizador / UID e clicando no botão Login.\nComo deve saber, esta forma não é "
                            "segura, logo fica ao seu critério.\n\nVersão em "
                            "vigor: 1.0"
                            )

        # Torna a caixa de texto não editável ou seja somente leitura
        self.textbox.configure(state="disabled")
