# Importação de bibliotecas necessárias
import customtkinter as ctk                      # Interface gráfica moderna baseada em tkinter
import json                                      # Importa a biblioteca json
from PIL import Image                            # Manipulação de imagens
from time import sleep                           # Pausa o programa por determinado tempo
from Base_de_Dados import BaseDados              # Importa classes presentes no ficheiro model
from tkinter import messagebox                   # Caixas de mensagem
import API                                       # Importa classes presentes no ficheiro model
from datetime import datetime                    # Obter a data
from caixa_de_texto import CaixaInformacoes      # Widget personalizado para mostrar informações
import model                                     # Importa classes presentes no ficheiro model

# Inicialização de objetos
bd = BaseDados()
ipma = API.classe_ipma

# Classe principal da aplicação
class App:
    def __init__(self):
        self.dados = model.Obter_imagens()        # Objeto responsável por fornecer imagens e caminhos
        self.janela = ctk.CTk()                   # Janela inicial da aplicação
        self.janela.title("Weather2Travel")       # Título da janela
        self.janela.geometry("800x500")           # Dimensões da janela
        self.janela.resizable(False, False)       # Dasabilita o redimensionamento da janela
        self.janela.configure(fg_color="white")   # Cor de fundo da janela

        self.func_frame_boasvindas()              # Chama a função para criar o frame de boas-vindas
        self.func_frame_login()                   # Chama a função para o frame de login
        self.janela.mainloop()                    # Inicia o loop principal da aplicação

    # Função frame boasvindas
    def func_frame_boasvindas(self):
        # Função interna para mostrar as informações do app
        def func_frame_informacoes():
            # Remove todos os widgets do frame de boas-vindas
            model.Remover_frames.limpar_widgets_do_frame(self.frame_boasvindas)

            botao_voltar = ctk.CTkButton(
                self.frame_boasvindas, text="Voltar", fg_color="Red",
                command=self.func_frame_boasvindas, corner_radius=15, width=50, height=25
            )
            botao_voltar.place(relx=0.9, rely=0.95, anchor="center")

            label_boasvindas = ctk.CTkLabel(
                self.frame_boasvindas, text="Informações", font=("Arial Black", 15),
                text_color="#F7DE44"
            )
            label_boasvindas.place(relx=0.5, rely=0.085, anchor="center")

            # Imagem do logo da ESTGA
            self.dados.config_imagem("imagens/logo_estga.png", self.frame_boasvindas, (65, 65), 0.85, 0.075, "steel blue")

            # Caixa de texto com informações relevantes para o utilizador
            CaixaInformacoes(self.frame_boasvindas)

        self.frame_boasvindas = ctk.CTkFrame(
            self.janela, fg_color="steel blue", corner_radius=15, border_width=5, border_color='white'
        )
        self.frame_boasvindas.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        label_boasvindas = ctk.CTkLabel(
            self.frame_boasvindas, text='Bem-Vindo!\nWeather2Travel',
            font=('elephant', 22), text_color='#F7DE44'
        )
        label_boasvindas.place(relx=0.5, rely=0.1, anchor='center')

        # Imagem principal do frame de boas-vindas
        self.dados.config_imagem("imagens/imagem_boasvindas1.png", self.frame_boasvindas, (375, 250), 0.5, 0.45, "steel blue")

        # Tenta carregar o botão de informação com ícone
        try:
            caminho_imagem = self.dados.caminho_recurso("imagens/imagem_informação.png")
            imagem_botao = ctk.CTkImage(Image.open(caminho_imagem), size=(25, 25))
            botao_redondo = ctk.CTkButton(
                self.frame_boasvindas, image=imagem_botao, text="", width=25, height=25,
                corner_radius=20, fg_color="steel blue", hover_color="white",
                command=func_frame_informacoes
            )
            botao_redondo.place(relx=0.025, rely=0.91)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar imagem: {e}")

    # Função Frame Login
    def func_frame_login(self):
        # Função Frame Criar Conta
        def func_frame_criar_conta():
            # Função para limpar os widgets do frame self.frame_login
            model.Remover_frames.limpar_widgets_do_frame(self.frame_login)

            frame_fundo = ctk.CTkFrame(self.frame_login, height=385, width=300, fg_color="gray25", corner_radius=10)
            frame_fundo.place(relx=0.5, rely=0.525, anchor="center")

            label_facalogin = ctk.CTkLabel(frame_fundo, text="Crie a sua Conta!", font=("Arial Black", 14),
                                           text_color="white")
            label_facalogin.place(relx=0.5, rely=0.063, anchor="center")

            frame_nome = ctk.CTkFrame(self.frame_login, height=35, width=250, fg_color="gray15", corner_radius=5,
                                      bg_color="gray25")
            frame_nome.place(relx=0.5, rely=0.28, anchor="center")

            entrada_nome = ctk.CTkEntry(self.frame_login, height=30, width=200, placeholder_text="Nome de Utilizador",
                                        text_color="white", placeholder_text_color="white", fg_color="gray15",
                                        bg_color="gray15", border_width=0)
            entrada_nome.place(relx=0.52, rely=0.28, anchor="center")

            frame_senha = ctk.CTkFrame(self.frame_login, height=35, width=250, fg_color="gray15", corner_radius=5,
                                       bg_color="gray25")
            frame_senha.place(relx=0.5, rely=0.38, anchor="center")

            entrada_senha = ctk.CTkEntry(self.frame_login, height=30, width=200, placeholder_text="Senha",
                                         text_color="white", placeholder_text_color="white", fg_color="gray15",
                                         bg_color="gray15", border_width=0, show="*")
            entrada_senha.place(relx=0.52, rely=0.38, anchor="center")

            botao_olho = ctk.CTkButton(self.frame_login, text="👁", width=30, height=30, bg_color="gray15",
                                       fg_color="gray15",
                                       hover_color="gray25")
            botao_olho.place(relx=0.77, rely=0.38, anchor="center")

            # Função para ver ou esconder a senha
            alterar_visual = model.Visual_senha(entrada_senha, botao_olho)

            # Função para mudar a configuração do botao_olho
            botao_olho.configure(command=alterar_visual.alternar_modo_visual_senha)

            frame_uid = ctk.CTkFrame(self.frame_login, height=35, width=250, fg_color="gray15", corner_radius=5,
                                     bg_color="gray25")
            frame_uid.place(relx=0.5, rely=0.48, anchor="center")

            entrada_uid = ctk.CTkEntry(self.frame_login, height=30, width=200, placeholder_text="UID",
                                       text_color="white", placeholder_text_color="white", fg_color="gray15",
                                       bg_color="gray15", border_width=0)
            entrada_uid.place(relx=0.52, rely=0.48, anchor="center")

            label_aviso = ctk.CTkLabel(self.frame_login, width=100, height=10,
                                       text="⚠️ Aviso: Durante a leitura do UID não digite nada.",
                                       font=("Arial", 10), text_color="yellow", bg_color="gray25")
            label_aviso.place(relx=0.495, rely=0.525, anchor="center")

            frame_mail = ctk.CTkFrame(self.frame_login, height=35, width=250, fg_color="gray15", corner_radius=5,
                                      bg_color="gray25")
            frame_mail.place(relx=0.5, rely=0.58, anchor="center")

            entrada_mail = ctk.CTkEntry(self.frame_login, height=30, width=200, placeholder_text="omeumail@gmail.com",
                                        text_color="white", placeholder_text_color="white", fg_color="gray15",
                                        bg_color="gray15", border_width=0)
            entrada_mail.place(relx=0.52, rely=0.58, anchor="center")

            frame_distrito = ctk.CTkFrame(self.frame_login, height=35, width=250, fg_color="gray15", corner_radius=5,
                                          bg_color="gray25")
            frame_distrito.place(relx=0.5, rely=0.68, anchor="center")

            frame_localizacao = ctk.CTkFrame(self.frame_login, height=35, width=250, fg_color="gray15", corner_radius=5,
                                             bg_color="gray25")
            frame_localizacao.place(relx=0.5, rely=0.78, anchor="center")

            # Variáveis iniciais dos menus
            distrito_selecionado = ctk.StringVar(value="Selecionar...")
            localidade_selecionada = ctk.StringVar(value="Selecionar...")

            menu_distrito = ctk.CTkOptionMenu(frame_distrito, width=200, variable=distrito_selecionado,
                                                  values=["Selecionar..."], fg_color="gray15", bg_color="gray15",
                                                  button_color="gray15", button_hover_color="gray20")
            menu_distrito.place(relx=0.5, rely=0.5, anchor="center")

            menu_localidade = ctk.CTkOptionMenu(frame_localizacao, width=200, variable=localidade_selecionada,
                                                    values=["Selecionar..."], fg_color="gray15", bg_color="gray15",
                                                    button_color="gray15", button_hover_color="gray20")
            menu_localidade.place(relx=0.5, rely=0.5, anchor="center")

            botao_confirmar_mail = ctk.CTkButton(self.frame_login, text="Confirmar mail", font=("Arial", 12),
                                               fg_color="steel blue",
                                               bg_color="gray25", width=90, height=30, corner_radius=25)
            botao_confirmar_mail.place(relx=0.5, rely=0.87, anchor="center")

            botao_voltar = ctk.CTkButton(self.frame_login, text="Voltar", fg_color="Red", command=self.func_frame_login,
                                         corner_radius=15, width=50, height=25)
            botao_voltar.place(relx=0.9, rely=0.955, anchor="center")

            self.dados.config_imagem("imagens/imagem_perfil_login.png", self.frame_login, (60, 60), 0.5, 0.073, "gray80")
            self.dados.config_imagem("imagens/imagem_perfil_nome.png", self.frame_login, (20, 20), 0.235, 0.28, "gray15")
            self.dados.config_imagem("imagens/imagem_cadeado_passe.png", self.frame_login, (20, 20), 0.235, 0.38, "gray15")
            self.dados.config_imagem("imagens/imagem_uid.png", self.frame_login, (20, 20), 0.235, 0.48, "gray15")
            self.dados.config_imagem("imagens/imagem_gmail.png", self.frame_login, (20, 20), 0.235, 0.58, "gray15")
            self.dados.config_imagem("imagens/imagem_localização.png", self.frame_login, (28, 28), 0.235, 0.68, "gray15")
            self.dados.config_imagem("imagens/imagem_localização.png", self.frame_login, (28, 28), 0.235, 0.78, "gray15")

            # Tenta carregar os dados
            try:
                localidades = API.classe_ipma.obter_todas_localidades()
                if localidades is None:
                    raise ValueError("Falha ao obter localidades")

                distritos_ids = API.extrair_distritos(localidades)
                distritos_nomes = [API.distritos_por_id[d_id] for d_id in distritos_ids if d_id in API.distritos_por_id]

                # Atualiza dropdown de distrito
                menu_distrito.configure(values=distritos_nomes)

                # Função de atualização de localidades
                def atualizar_localidades(opcao_distrito):
                    # Procura o id do distrito pelo nome selecionado
                    id_distrito = None
                    for id_, nome in API.distritos_por_id.items():
                        if nome == opcao_distrito:
                            id_distrito = id_
                            break
                    if id_distrito is None:
                        return

                    # Filtra as localidades desse distrito e extrai os nomes
                    nomes_localidades = [loc['local'] for loc in
                                         API.filtrar_localidades_por_distrito(localidades, id_distrito)]

                    # Atualiza o menu de localidades e seleciona a primeira opção de localidade
                    menu_localidade.configure(values=nomes_localidades)
                    localidade_selecionada.set(nomes_localidades[0])

                # Atribui o comando para a função
                menu_distrito.configure(command=atualizar_localidades)

            except Exception:
                messagebox.showwarning("Aviso",
                                       "Não foi possível carregar os dados de localização. Verifique sua internet.")

            def criar_conta():
                # Dá às variáveis o valor inserido nas Entradas
                nome = entrada_nome.get()
                senha = entrada_senha.get()
                uid = entrada_uid.get()
                mail = entrada_mail.get()
                localizacao = localidade_selecionada.get()

                def validar_senha(senha):
                    # Permite explicitamente se a senha for igual ao UID
                    if senha == uid:
                        return True
                    if len(senha) < 8:
                        messagebox.showerror("Erro", "A senha deve ter pelo menos 8 caracteres!")
                        return False
                    if not any(char.isupper() for char in senha):
                        messagebox.showerror("Erro", "A senha deve ter pelo menos uma letra maiúscula!")
                        return False
                    if not any(char.islower() for char in senha):
                        messagebox.showerror("Erro", "A senha deve ter pelo menos uma letra minúscula!")
                        return False
                    if not any(char.isdigit() for char in senha):
                        messagebox.showerror("Erro", "A senha deve ter pelo menos um número!")
                        return False
                    return True

                # Verifica se o nome de utilizador tem mais de 10 caracteres
                if len(nome) > 10:
                    messagebox.showerror("Erro", "O Nome de Utilizador não deve ter mais de 10 caracteres.")
                    return

                # Verifica se todos os campos estão preenchidos
                if not all([nome, senha, uid, mail, localizacao]):
                    messagebox.showwarning("Campos em branco", "Preencha todos os campos antes de continuar.")
                    return

                # Verifica se a senha é válida
                if not validar_senha(senha):
                    return

                utilizador = model.Utilizador(nome, senha, uid, mail, localizacao)
                if bd.verificar_existencia(utilizador, mail):
                    messagebox.showerror("Erro", "Nome de utilizador, UID ou Email já registados.")
                    return

                # Criar instância de EmailConfirmacao
                email_conf = model.EmailConfirmacao()

                # Envia o código de confirmação por email
                codigo_gerado = email_conf.enviar(mail)

                if not codigo_gerado:
                    messagebox.showerror("Erro", "Falha ao enviar o e-mail. Verifique o endereço.")
                    return

                if localizacao == "Selecionar...":
                    messagebox.showerror("Erro", "Selecione uma localidade válida.")
                    return

                # Guarda o código para validação
                self.codigo_confirmacao = codigo_gerado

                # Agora exibe o frame para o utilizador inserir o código enviado
                def mostrar_frame_codigo_confirmacao():
                    frame_fundo = ctk.CTkFrame(self.frame_login, height=385, width=300, fg_color="gray25",
                                               corner_radius=0)
                    frame_fundo.place(relx=0.5, rely=0.525, anchor="center")

                    label_texto = ctk.CTkLabel(frame_fundo, text="Insira o código enviado para o seu e-mail:",
                                               font=("Arial", 15), text_color="white")
                    label_texto.place(relx=0.5, rely=0.1, anchor="center")

                    entrada_codigo = ctk.CTkEntry(frame_fundo, height=30, width=200,
                                                  placeholder_text="####",
                                                  text_color="white", placeholder_text_color="white", fg_color="gray15",
                                                  bg_color="gray15", border_width=0, justify="center")
                    entrada_codigo.place(relx=0.5, rely=0.25, anchor="center")

                    # Número de tentativas para inserir o codigo de confirmação
                    tentativas_restantes = [3]

                    def verificar_codigo():
                        codigo_inserido = entrada_codigo.get()
                        if codigo_inserido == self.codigo_confirmacao:
                            # Cria o utilizador após confirmação correta
                            utilizador = model.Utilizador(nome, senha, uid, mail, localizacao)
                            # Se os dados do utilizador foi adicionado à base de dados
                            bd.inserir_utilizador(utilizador)
                            messagebox.showinfo("Sucesso", "Conta criada com sucesso! Bem-vindo "
                                                               "à Weather2Travel!")
                            # Voltar para o frame login
                            self.func_frame_login()
                        else:
                            # Subtrai uma tentativa caso o código inserido nao seja igual ao código gerado
                            tentativas_restantes[0] -= 1
                            # Caso o número de tentativas seja igual a 0 apresenta uma mensagem de erro
                            if tentativas_restantes[0] == 0:
                                messagebox.showerror("Erro",
                                                     "Número máximo de tentativas excedido. Reinicie o processo.")
                                self.func_frame_login()
                            # Se o número de tentativas ainda é maior que 0
                            else:
                                messagebox.showerror("Erro",
                                                     f"Código inválido. Tentativas restantes: {tentativas_restantes[0]}")

                    botao_confirmar = ctk.CTkButton(frame_fundo, text="Criar Conta", command=verificar_codigo)
                    botao_confirmar.place(relx=0.5, rely=0.85, anchor="center")

                self.codigo_confirmacao = codigo_gerado
                mostrar_frame_codigo_confirmacao()

            botao_confirmar_mail.configure(command=criar_conta)

        def func_frame_mail_mudar_senha():
            model.Esconder_frames.limpar_widgets_do_frame(self.frame_login)

            frame_fundo = ctk.CTkFrame(self.frame_login, height=300, width=300, fg_color="gray25", corner_radius=10)
            frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

            self.dados.config_imagem("imagens/imagem_cadeado_passe.png", frame_fundo, (20, 20), 0.145, 0.25, "gray15")

            label_texto = ctk.CTkLabel(frame_fundo,
                                       text="Digite o e-mail da conta para a qual\ndeseja alterar a senha.",
                                       font=("Arial", 15), text_color="white")
            label_texto.place(relx=0.5, rely=0.1, anchor="center")

            frame_mail = ctk.CTkFrame(frame_fundo, height=35, width=250, fg_color="gray15", corner_radius=5,
                                      bg_color="gray25")
            frame_mail.place(relx=0.5, rely=0.25, anchor="center")

            entrada_mail = ctk.CTkEntry(frame_fundo, height=30, width=200, placeholder_text="omeumail@gmail.com",
                                        text_color="white", placeholder_text_color="white", fg_color="gray15",
                                        bg_color="gray15", border_width=0, justify="center")
            entrada_mail.place(relx=0.5, rely=0.25, anchor="center")

            label_aviso = ctk.CTkLabel(frame_fundo, text="", font=("Arial", 10))
            label_aviso.place(relx=0.5, rely=0.35, anchor="center")

            def mostrar_frame_codigo(numero_mail, email_utilizador):
                model.Esconder_frames.limpar_widgets_do_frame(self.frame_login)

                frame_fundo = ctk.CTkFrame(self.frame_login, height=300, width=300, fg_color="gray25", corner_radius=10)
                frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

                label_texto = ctk.CTkLabel(frame_fundo, text="Insira o código que foi enviado\npara o seu mail.",
                                           font=("Arial", 15), text_color="white")
                label_texto.place(relx=0.5, rely=0.1, anchor="center")

                frame_codigo = ctk.CTkFrame(frame_fundo, height=35, width=250, fg_color="gray15", corner_radius=5,
                                            bg_color="gray25")
                frame_codigo.place(relx=0.5, rely=0.25, anchor="center")

                entrada_codigo = ctk.CTkEntry(frame_fundo, height=30, width=200, placeholder_text="####",
                                              text_color="white", placeholder_text_color="white",
                                              fg_color="gray15", bg_color="gray15", border_width=0, justify="center")
                entrada_codigo.place(relx=0.5, rely=0.25, anchor="center")

                label_aviso_codigo = ctk.CTkLabel(frame_fundo, text="", font=("Arial", 10))
                label_aviso_codigo.place(relx=0.5, rely=0.35, anchor="center")

                tentativas_restantes1 = [3]

                def verificar_codigo():
                    codigo_inserido = entrada_codigo.get().strip()

                    if codigo_inserido == numero_mail:
                        label_aviso_codigo.configure(text="Código de Verificação\nValidado!", text_color="green")
                        frame_fundo.update()
                        sleep(2)

                        model.Esconder_frames.limpar_widgets_do_frame(self.frame_login)

                        frame_nova_senha = ctk.CTkFrame(self.frame_login, height=300, width=300, fg_color="gray25",
                                                        corner_radius=10)
                        frame_nova_senha.place(relx=0.5, rely=0.5, anchor="center")

                        label_texto = ctk.CTkLabel(frame_nova_senha, text="Alteração de Senha", font=("Arial", 15),
                                                   text_color="white")
                        label_texto.place(relx=0.5, rely=0.1, anchor="center")

                        entrada_nova_senha = ctk.CTkEntry(frame_nova_senha, height=30, width=200,
                                                          placeholder_text="Nova Senha",
                                                          text_color="white", placeholder_text_color="white",
                                                          fg_color="gray15", bg_color="gray15", border_width=0,
                                                          justify="center", show="*")
                        entrada_nova_senha.place(relx=0.5, rely=0.25, anchor="center")

                        entrada_confirmar_senha = ctk.CTkEntry(frame_nova_senha, height=30, width=200,
                                                               placeholder_text="Confirmar Senha",
                                                               text_color="white", placeholder_text_color="white",
                                                               fg_color="gray15", bg_color="gray15", border_width=0,
                                                               justify="center", show="*")
                        entrada_confirmar_senha.place(relx=0.5, rely=0.38, anchor="center")

                        botao_olho = ctk.CTkButton(frame_nova_senha, text="👁", width=30, height=30, bg_color="gray15",
                                                   fg_color="gray15", hover_color="gray25")
                        botao_olho.place(relx=0.75, rely=0.25, anchor="center")

                        alterar_visual = model.Visual_senha(entrada_nova_senha, botao_olho)
                        botao_olho.configure(command=alterar_visual.alternar_modo_visual_senha)

                        botao_olho1 = ctk.CTkButton(frame_nova_senha, text="👁", width=30, height=30, bg_color="gray15",
                                                    fg_color="gray15", hover_color="gray25")
                        botao_olho1.place(relx=0.75, rely=0.38, anchor="center")

                        alterar_visual = model.Visual_senha(entrada_confirmar_senha, botao_olho1)
                        botao_olho1.configure(command=alterar_visual.alternar_modo_visual_senha)

                        botao_voltar = ctk.CTkButton(frame_nova_senha, text="Voltar", fg_color="Red",
                                                     command=func_frame_mail_mudar_senha,
                                                     corner_radius=15, width=50, height=25)
                        botao_voltar.place(relx=0.5, rely=0.9, anchor="center")

                        label_aviso_senha = ctk.CTkLabel(frame_nova_senha, text="", font=("Arial", 10))
                        label_aviso_senha.place(relx=0.5, rely=0.48, anchor="center")

                        def confirmar_senha():
                            nova = entrada_nova_senha.get()
                            confirmar = entrada_confirmar_senha.get()

                            def validar_senha():
                                if len(nova) < 8:
                                    messagebox.showerror("Erro", "A senha deve ter pelo menos 8 caracteres!")
                                    return False
                                if not any(char.isupper() for char in nova):
                                    messagebox.showerror("Erro", "A senha deve ter pelo menos uma letra maiúscula!")
                                    return False
                                if not any(char.islower() for char in nova):
                                    messagebox.showerror("Erro", "A senha deve ter pelo menos uma letra minúscula!")
                                    return False
                                if not any(char.isdigit() for char in nova):
                                    messagebox.showerror("Erro", "A senha deve ter pelo menos um número!")
                                    return False
                                return True

                            if not nova or not confirmar:
                                label_aviso_senha.configure(text="*Preencha todos os campos", text_color="red")
                                return

                            if nova != confirmar:
                                label_aviso_senha.configure(text="*As senhas não coincidem", text_color="red")
                                return

                            if not validar_senha():
                                return

                            bd.alterar_senha(entrada_mail.get().strip(), nova)  # <== agora está correto
                            label_aviso_senha.configure(text="Senha Alterada com Sucesso!", text_color="green")
                            frame_nova_senha.update()
                            sleep(2)
                            self.func_frame_login()

                        botao_confirmar_senha = ctk.CTkButton(frame_nova_senha, text="Confirmar Senha", width=25,
                                                              height=20, command=confirmar_senha)
                        botao_confirmar_senha.place(relx=0.5, rely=0.55, anchor="center")

                    else:
                        tentativas_restantes1[0] -= 1
                        if tentativas_restantes1[0] <= 0:
                            label_aviso_codigo.configure(text="Muitas tentativas.\nReenvie o e-mail.", text_color="red")
                            frame_fundo.update()
                            sleep(2)
                            func_frame_mail_mudar_senha()
                        else:
                            label_aviso_codigo.configure(
                                text=f"Código inválido!\nTentativas restantes: {tentativas_restantes1[0]}",
                                text_color="red")

                botao_confirmar_codigo = ctk.CTkButton(frame_fundo, text="Confirmar", command=verificar_codigo)
                botao_confirmar_codigo.place(relx=0.5, rely=0.5, anchor="center")

                botao_voltar = ctk.CTkButton(frame_fundo, text="Voltar", fg_color="Red", command=self.func_frame_login,
                                             corner_radius=15, width=50, height=25)
                botao_voltar.place(relx=0.5, rely=0.9, anchor="center")

            email_enviar = model.EnviarEmailVerificacao(
                frame_fundo=frame_fundo,
                entrada_email=entrada_mail,
                label_aviso=label_aviso,
                bd=bd,
                func_mostrar_frame_codigo=lambda cod: mostrar_frame_codigo(cod, entrada_mail.get().strip()))

            botao_enviar_mail_recuperar_senha = ctk.CTkButton(frame_fundo, text="Enviar mail", width=25, height=20,
                                                              command=email_enviar.enviar_mail)
            botao_enviar_mail_recuperar_senha.place(relx=0.5, rely=0.45, anchor="center")

            botao_voltar = ctk.CTkButton(frame_fundo, text="Voltar", fg_color="Red", command=self.func_frame_login,
                                         corner_radius=15, width=50, height=25)
            botao_voltar.place(relx=0.5, rely=0.9, anchor="center")

        def verificar_login():
            nome = entrada_nome.get()
            senha = entrada_senha.get()

            # Login só com UID (senha vazia e UID == senha)
            if nome and not senha:
                # Tenta login com UID como senha (usando nome como UID e senha)
                utilizador = model.Utilizador(nome, nome, None, None, None)  # só nome e senha (igual ao nome) são usados
            else:
                # Login normal com nome ou UID e senha
                utilizador = model.Utilizador(nome, senha, None, None, None)

            dados_utilizador = bd.obter_dados_utilizador(utilizador)

            if dados_utilizador:
                # Função que inicia a aplicação após o login
                func_frame_APP(dados_utilizador)
            else:
                messagebox.showerror("Erro", "Nome de utilizador ou senha incorretos.")

        self.frame_login = ctk.CTkFrame(self.janela, fg_color="gray80", corner_radius=15, border_width=5,
                                        border_color='white')
        self.frame_login.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        frame_fundo = ctk.CTkFrame(self.frame_login, height=300, width=300, fg_color="gray25", corner_radius=10)
        frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

        label_facalogin = ctk.CTkLabel(frame_fundo, text="Faça o Login!", font=("Arial Black", 15), text_color="white")
        label_facalogin.place(relx=0.5, rely=0.1, anchor="center")

        frame_nome = ctk.CTkFrame(self.frame_login, height=35, width=250, fg_color="gray15", corner_radius=5,
                                  bg_color="gray25")
        frame_nome.place(relx=0.5, rely=0.38, anchor="center")

        entrada_nome = ctk.CTkEntry(self.frame_login, height=30, width=200, placeholder_text="Nome de Utilizador / UID",
                                    text_color="white", placeholder_text_color="white", fg_color="gray15",
                                    bg_color="gray15", border_width=0)
        entrada_nome.place(relx=0.52, rely=0.38, anchor="center")

        frame_senha = ctk.CTkFrame(self.frame_login, height=35, width=250, fg_color="gray15", corner_radius=5,
                                   bg_color="gray25")
        frame_senha.place(relx=0.5, rely=0.48, anchor="center")

        entrada_senha = ctk.CTkEntry(self.frame_login, height=30, width=200, placeholder_text="Senha",
                                     text_color="white", placeholder_text_color="white", fg_color="gray15",
                                     bg_color="gray15", border_width=0, show="*")
        entrada_senha.place(relx=0.52, rely=0.48, anchor="center")

        botao_olho = ctk.CTkButton(self.frame_login, text="👁", width=30, height=30, bg_color="gray15",
                                   fg_color="gray15",
                                   hover_color="gray25")
        botao_olho.place(relx=0.77, rely=0.48, anchor="center")

        alterar_visual = model.Visual_senha(entrada_senha, botao_olho)

        botao_olho.configure(command=alterar_visual.alternar_modo_visual_senha)

        botao_esqueci_senha = ctk.CTkButton(self.frame_login, text='Esqueceu-se da senha?', font=("Arial", 10),
                                            fg_color="gray25", bg_color="gray15", hover_color="gray28", width=1,
                                            height=1,
                                            corner_radius=25, command=func_frame_mail_mudar_senha)
        botao_esqueci_senha.place(relx=0.33, rely=0.53, anchor="center")

        botao_login = ctk.CTkButton(self.frame_login, text="Login", font=("Arial", 12), fg_color="steel blue",
                                    bg_color="gray25",
                                    command=verificar_login,
                                    width=90, height=30, corner_radius=25)
        botao_login.place(relx=0.5, rely=0.6, anchor="center")

        botao_criar_conta = ctk.CTkButton(self.frame_login, text="Criar Conta", font=("Arial", 12),
                                          fg_color="steel blue",
                                          bg_color="gray25",
                                          width=90, height=30, corner_radius=25, command=func_frame_criar_conta)
        botao_criar_conta.place(relx=0.5, rely=0.675, anchor="center")

        self.dados.config_imagem("imagens/imagem_perfil_login.png", self.frame_login, (60, 60), 0.5, 0.125, "gray80")
        self.dados.config_imagem("imagens/imagem_perfil_nome.png", self.frame_login, (20, 20), 0.235, 0.38, "gray15")
        self.dados.config_imagem("imagens/imagem_cadeado_passe.png", self.frame_login, (20, 20), 0.235, 0.48, "gray15")

        # Botão sair da aplicação
        def destruir_janela():
            self.janela.destroy()

        botao_sair = ctk.CTkButton(self.frame_login, text="Sair", font=("Arial", 12), fg_color="red", width=30,
                                   height=25,
                                   corner_radius=25, command=destruir_janela)
        botao_sair.place(relx=0.92, rely=0.95, anchor="center")

        # Função para criar a nova janela
        def func_frame_APP(dados_utilizador):
            # Obter esses dados para utilizar nesta nova função
            uid, nome, localizacao = dados_utilizador
            self.janela.destroy()
            janela_APP = ctk.CTk()
            janela_APP.title('Weather2Travel')
            janela_APP.geometry('1080x720')
            janela_APP.resizable(False, False)
            janela_APP.configure(fg_color="white")

            frame_cabecalho = ctk.CTkFrame(janela_APP, height=65, width=1080, fg_color="gray25", corner_radius=0)
            frame_cabecalho.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.1, anchor="center")

            frame_divisao = ctk.CTkFrame(janela_APP, width=6, height=655, fg_color="gray25", corner_radius=0, border_width=0)
            frame_divisao.place(relx=0.5, rely=0.55, anchor="center")

            label_titulo = ctk.CTkLabel(frame_cabecalho, text="Weather2Travel", font=("elephant", 25),
                                        text_color="#F7DE44")
            label_titulo.place(relx=0.5, rely=0.5, anchor="center")

            label_uid_perfil = ctk.CTkLabel(frame_cabecalho, text=f"UID: {uid}", font=("Arial Black", 10),
                                            text_color="white")
            label_uid_perfil.place(relx=0.825, rely=0.35, anchor="center")

            label_nome_perfil = ctk.CTkLabel(frame_cabecalho, text=f"Utilizador: {nome}", font=("Arial", 12),
                                             text_color="white")
            label_nome_perfil.place(relx=0.825, rely=0.65, anchor="center")

            # Função para fazer logout
            def logout():
                messagebox.showinfo("Sessão terminada com Sucesso", "Terminaste sessão com sucesso.")
                janela_APP.destroy()

                App()

            frame_combobox_localidade = ctk.CTkFrame(janela_APP, fg_color="transparent")
            frame_combobox_localidade.place(relx=0.25, rely=0.625, anchor="center")

            frame_combobox_destino = ctk.CTkFrame(janela_APP, width=380, height=300, fg_color="transparent")
            frame_combobox_destino.place(relx=0.75, rely=0.625, anchor="center")

            label_distrito = ctk.CTkLabel(janela_APP, text="Distrito:", font=("Arial", 15),
                                          fg_color="white", text_color="black")
            label_distrito.place(relx=0.545, rely=0.15, anchor="center")

            valor_distrito = ctk.StringVar(value="Selecionar")

            menu_distrito = ctk.CTkOptionMenu(janela_APP, values=["Selecionar"],
                                               variable=valor_distrito, width=200)
            menu_distrito.place(relx=0.77, rely=0.15, anchor="center")

            label_localidade = ctk.CTkLabel(janela_APP, text="Localidade:", font=("Arial", 15),
                                            fg_color="white", text_color="black")
            label_localidade.place(relx=0.558, rely=0.225, anchor="center")

            valor_localidade = ctk.StringVar(value="Selecionar")
            menu_localidade = ctk.CTkOptionMenu(janela_APP, values=["Selecionar"], variable=valor_localidade,
                                                 width=200)
            menu_localidade.place(relx=0.77, rely=0.225, anchor="center")

            label_num_dias = ctk.CTkLabel(janela_APP, text="Dias de previsão:", font=("Arial", 15),
                                          fg_color="white", text_color="black")
            label_num_dias.place(relx=0.575, rely=0.30, anchor="center")

            valor_num_dias = ctk.StringVar(value="5")
            menu_num_dias = ctk.CTkOptionMenu(janela_APP, values=["1", "3", "5"], variable=valor_num_dias)
            menu_num_dias.place(relx=0.743, rely=0.30, anchor="center")

            def atualizar_previsao_destino(event=None):
                # Obter localidades
                localidades = API.classe_ipma.obter_todas_localidades()
                if not localidades:
                    messagebox.showerror("Erro", "Erro ao onter imagens")
                    return

                distritos_ids = API.extrair_distritos(localidades)

                distritos_nome = [API.distritos_por_id[id_d] for id_d in distritos_ids if id_d in API.distritos_por_id]

                # Atualiza o menu com os distritos
                menu_distrito.configure(values=["Selecionar"] + distritos_nome)

                def atualizar_localidades(localidade_selecionada):
                    # Se o utilizador não escolheu nenhum distrito válido
                    if localidade_selecionada == "Selecionar":
                        # Limpa o menu de localidades e define a opção padrão
                        menu_localidade.configure(values=["Selecionar"])
                        valor_localidade.set("Selecionar")
                        return

                    # Procura o ID do distrito a partir do nome selecionado
                    id_distrito = next(
                        (id_d for id_d, nome in API.distritos_por_id.items() if nome == localidade_selecionada),
                        None
                    )

                    # Se não encontrar um ID válido, define novamente os valores padrão
                    if id_distrito is None:
                        menu_localidade.configure(values=["Selecionar"])
                        valor_localidade.set("Selecionar")
                        return

                    # Filtra as localidades que pertencem ao distrito selecionado
                    locais_filtrados = API.filtrar_localidades_por_distrito(localidades, id_distrito)

                    # Extrai apenas os nomes das localidades
                    nomes_locais = [loc['local'] for loc in locais_filtrados]

                    # Atualiza o dropdown de localidades com os nomes filtrados
                    menu_localidade.configure(values=["Selecionar"] + nomes_locais)
                    valor_localidade.set("Selecionar")  # Define o valor padrão como "Selecionar"

                def mostrar_previsao(localidade_selecionada):
                    # Limpa os widgets anteriores do frame onde será exibida a previsão
                    model.Remover_frames.limpar_widgets_do_frame(frame_combobox_destino)

                    # Lê os valores selecionados pelo utilizador
                    sel_localidade = localidade_selecionada
                    sel_distrito = valor_distrito.get()
                    num_dias = int(valor_num_dias.get())

                    # Se não for selecionado um distrito ou localidade
                    if sel_distrito == "Selecionar" or sel_localidade == "Selecionar":
                        return

                    # Procura o ID do distrito correspondente ao nome selecionado
                    id_distrito = next((id_d for id_d, nome in API.distritos_por_id.items() if nome == sel_distrito),
                                       None)
                    if id_distrito is None:
                        return  # Encerra se não encontrar o ID

                    # Filtra as localidades disponíveis no distrito selecionado
                    locais_filtrados = API.filtrar_localidades_por_distrito(localidades, id_distrito)

                    # Procura a localidade escolhida pelo utilizador
                    local_escolhido = next((loc for loc in locais_filtrados if loc['local'] == sel_localidade), None)
                    if local_escolhido is None:
                        return  # Encerra se não encontrar a localidade

                    # Obtém o ID global da localidade, necessário para pegar a previsão
                    globalIdLocal = local_escolhido['globalIdLocal']

                    # Obtém a previsão do tempo para a localidade
                    previsao = API.classe_ipma.obter_previsao_aggregate(globalIdLocal)
                    if not previsao:
                        # Se falhar, avisa o utilizador
                        messagebox.showerror("Erro", "Erro na obtenção da previsão. Verifique a ligação"
                                                     " à Internet ou tente novamente mais tarde.")
                        return

                    try:
                        # Carrega o arquivo JSON com os tipos de tempo
                        caminho_json = self.dados.caminho_recurso("tipo_de_tempo.json")
                        with open(caminho_json, "r", encoding="utf-8") as f:
                            weather_json = json.load(f)

                            # Cria um dicionário para mapear IDs do tempo com suas descrições em português
                            descricao = {
                                item["idWeatherType"]: item["descWeatherTypePT"]
                                for item in weather_json["data"]
                            }
                    except Exception:
                        # Em caso de erro na leitura do JSON
                        messagebox.showerror("Erro", "Erro ao carregar descrições meteorológicas.")

                    # Contador para controlar quantos dias já foram exibidos
                    dias_exibidos = 0

                    # Percorre cada dia da previsão recebida
                    for dia in previsao:
                        if dias_exibidos >= num_dias:
                            break  # Se já exibiu a quantidade de dias desejada, sai do loop

                        # Extrai dados importantes do dicionário do dia
                        t_min = dia.get("tMin")  # Temperatura mínima
                        t_max = dia.get("tMax")  # Temperatura máxima
                        precip = dia.get("probabilidadePrecipita")  # Probabilidade de precipitação

                        # Se faltar algum dos dados, ignora esse dia
                        if t_min is None or t_max is None or precip is None:
                            continue

                        try:
                            # Formata a data do formato 'YYYY-MM-DD' para 'DD-MM-YYYY'
                            data_original = dia.get('dataPrev', '')[:10]
                            data = datetime.strptime(data_original, '%Y-%m-%d').strftime('%d-%m-%Y')

                            # Converte as temperaturas e precipitação para float
                            temperatura_max = float(t_max)
                            temperatura_min = float(t_min)
                            chuva = float(precip)

                            # ID do tipo de tempo (ex: 1 = Céu limpo, 2 = Pouco nublado, etc.)
                            weather_id = int(dia.get("idTipoTempo", 0))
                        except Exception:
                            # Em caso de erro de conversão, mostra o aviso
                            messagebox.showerror("Erro de conversão", "Erro ao fazer conversão. Tente mais tarde!")
                            continue

                        # Obtém a descrição do tempo a partir do ID (ex: "Céu limpo", etc.)
                        descricao_texto = descricao.get(weather_id, "Descrição não encontrada")

                        try:
                            # Cria um objeto de histórico com os dados do dia
                            h = model.Historico(sel_localidade, temperatura_min, temperatura_max, precip,
                                                descricao_texto, "Destino")

                            # Guarda esse histórico no banco de dados para o utilizador
                            bd.guardar_historico(uid, h)
                        except Exception:
                            # Em caso de erro ao guardar, mostra o aviso
                            messagebox.showerror("Erro ao guardar histórico", "Erro ao guardar histórico. Tente mais tarde!")
                            continue

                        # Formata o ID do tempo com dois dígitos (ex: 1 -> '01') para ser igual ao nome do arquivo da imagem
                        weather_id_formatado = f"{weather_id:02d}"

                        # Cria o nome do arquivo da imagem do ícone baseado no ID do tempo
                        nome_icone_png = f"imagens/w_ic_d_{weather_id_formatado}.png"

                        try:
                            # Tenta abrir o ícone da previsão do tempo
                            imagem = Image.open(self.dados.caminho_recurso(nome_icone_png))

                            # Converte a imagem para o formato do CTk (CustomTkinter)
                            ctk_imagem = ctk.CTkImage(dark_image=imagem, light_image=imagem, size=(55, 55))
                        except Exception:
                            # Caso o ícone não exista, exibe um aviso no terminal
                            messagebox.showerror("Erro", f"Imagem não encontrada: {nome_icone_png}")
                            ctk_imagem = None  # Nenhuma imagem será exibida

                        # Cria um frame para exibir os dados do dia atual
                        frame_dia = ctk.CTkFrame(frame_combobox_destino, corner_radius=8, fg_color="#f0f0f0")
                        frame_dia.grid(row=dias_exibidos, column=0, padx=4, pady=4, sticky="ew")

                        # Monta o texto da previsão
                        texto_previsao = (
                            f'📅 Data: {data}\n'
                            f'🌡 Temp. Máx: {temperatura_max}°C\n'
                            f'❄ Temp. Mín: {temperatura_min}°C\n'
                            f'🌧 Chuva: {chuva}%'
                        )

                        # Cria a label com o texto da previsão e adiciona ao frame do dia
                        label_dia = ctk.CTkLabel(
                            frame_dia, text=texto_previsao, justify="left", anchor="w", font=("Arial", 13),
                            text_color="black"
                        )
                        label_dia.pack(padx=6, pady=6, anchor="w")

                        if ctk_imagem:
                            # Cria um label com a imagem do ícone e o coloca ao lado do frame do dia
                            icone_label = ctk.CTkLabel(frame_combobox_destino, image=ctk_imagem, text="")
                            icone_label.image = ctk_imagem
                            icone_label.grid(row=dias_exibidos, column=1, padx=(6, 12), pady=4, sticky="e")

                        # Soma 1  ao contador de dias exibido
                        dias_exibidos += 1

                # Quando o utilizador escolhe um distrito, atualiza a lista de localidades
                menu_distrito.configure(command=atualizar_localidades)
                # Quando o utilizador escolhe uma localidade, mostra a previsão
                menu_localidade.configure(command=mostrar_previsao)
                # Quando o número de dias é alterado, atualiza a previsão com a localidade atual
                menu_num_dias.configure(command=lambda _: mostrar_previsao(valor_localidade.get()))

            def atualizar_previsao_localidade(event=None):
                # Obtém a cidade selecionada
                cidade = localizacao

                # Obtém a quantidade de dias selecionada no menu
                dias_localidade_str = menu_dias_localidade.get()

                # Se o valor for "Selecionar", ou seja, nenhuma opção válida foi escolhida
                if dias_localidade_str == "Selecionar":
                    return

                # Converte a quantidade de dias para um número inteiro
                dias = int(dias_localidade_str)

                # Obtém o ID global da localidade a partir da API, usando o nome da cidade
                global_id_local = API.classe_ipma.obter_global_id_local(cidade)

                # Se não conseguir obter o ID da localidade, mostra uma mensagem de erro e sai da função
                if global_id_local is None:
                    messagebox.showerror("Erro de ligação",
                                         "Erro na obtenção da previsão. Verifique a ligação à internet ou "
                                         "tente novamente mais tarde.")
                    return

                # Obtém a previsão do tempo agregada para a localidade
                previsao = API.classe_ipma.obter_previsao_aggregate(global_id_local)

                # Limpa o conteúdo do frame onde as previsões são exibidas, para evitar sobreposição
                model.Remover_frames.limpar_widgets_do_frame(frame_combobox_localidade)

                if previsao:
                    dias_exibidos = 0

                    try:
                        caminho_json = self.dados.caminho_recurso("tipo_de_tempo.json")
                        with open(caminho_json, "r", encoding="utf-8") as f:
                            weather_json = json.load(f)
                            descricao = {item["idWeatherType"]: item["descWeatherTypePT"] for item in
                                         weather_json["data"]}
                    except Exception as e:
                        messagebox.showerror("Erro", f"Erro ao carregar descrições meteorológicas: {e}")
                        descricao = {}

                    for dia in previsao:
                        if dias_exibidos >= dias:
                            break

                        t_min = dia.get("tMin")
                        t_max = dia.get("tMax")
                        precip = dia.get("probabilidadePrecipita")

                        if t_min is None or t_max is None or precip is None:
                            continue  # pula dia com dados incompletos

                        try:
                            data_raw = dia.get('dataPrev', '')[:10]
                            data = datetime.strptime(data_raw, '%Y-%m-%d').strftime(
                                '%d-%m-%Y') if data_raw else 'Data desconhecida'

                            temperatura_max = float(t_max)
                            temperatura_min = float(t_min)
                            chuva = float(precip)
                            weather_id = int(dia.get("idTipoTempo", 0))
                        except Exception as e:
                            messagebox.showerror("Erro de conversão", "Erro ao fazer conversão. Tente mais tarde!")
                            continue

                        descricao_texto = descricao.get(weather_id, "Descrição não encontrada")

                        try:
                            h = model.Historico(cidade, temperatura_min, temperatura_max, precip, descricao_texto, "Localidade")
                            bd.guardar_historico(uid, h)
                        except Exception:
                            messagebox.showerror("Erro ao guardar histórico",
                                                 "Erro ao guardar histórico. Tente mais tarde!")

                        weather_id_formatado = f"{weather_id:02d}"
                        nome_icone_png = f"imagens/w_ic_d_{weather_id_formatado}.png"
                        try:
                            imagem = Image.open(self.dados.caminho_recurso(nome_icone_png))
                            ctk_imagem = ctk.CTkImage(dark_image=imagem, light_image=imagem, size=(55, 55))
                        except Exception:
                            messagebox.showerror("Erro", f"Imagem não encontrada: {nome_icone_png}")
                            ctk_imagem = None

                        # Frame do dia
                        frame_dia = ctk.CTkFrame(frame_combobox_localidade, corner_radius=8, fg_color="#f0f0f0")
                        frame_dia.grid(row=dias_exibidos, column=0, padx=4, pady=4, sticky="ew")

                        texto_previsao = (
                            f'📅 Data: {data}\n'
                            f'🌡 Temp. Máx: {temperatura_max}°C\n'
                            f'❄ Temp. Mín: {temperatura_min}°C\n'
                            f'🌧 Chuva: {chuva}%'
                        )

                        label_dia = ctk.CTkLabel(
                            frame_dia, text=texto_previsao, justify="left", anchor="w", font=("Arial", 13),
                            text_color="black"
                        )
                        label_dia.pack(padx=6, pady=6, anchor="w")

                        if ctk_imagem:
                            icone_label = ctk.CTkLabel(frame_combobox_localidade, image=ctk_imagem, text="")
                            icone_label.image = ctk_imagem
                            icone_label.grid(row=dias_exibidos, column=1, padx=(6, 12), pady=4, sticky="e")

                        dias_exibidos += 1
                else:
                    messagebox.showerror("Erro!",
                                         "Erro na obtenção da previsão. Verifique a ligação à internet ou tente novamente mais tarde.")

            # Função para calcular a média de temperatura mínima, máxima e precipitação
            def calcular_media_registos(registos):
                # Inicializa as somas e o contador de registos
                soma_min = 0
                soma_max = 0
                soma_precip = 0
                contagem = 0

                # Espera-se que cada tupla contenha (temp_min, temp_max, precip)
                for temp_min, temp_max, precip in registos:
                    soma_min += temp_min   # Soma das temperaturas mínimas
                    soma_max += temp_max   # Soma das temperaturas máximas
                    soma_precip += precip  # Soma da precipitação
                    contagem += 1          # Conta o número de registos válidos

                # Se não houver registos, retorna None para evitar divisão por zero
                if contagem == 0:
                    return None

                # Retorna um dicionário com as médias calculadas
                return {
                    "media_min": soma_min / contagem,      # Média da temperatura mínima
                    "media_max": soma_max / contagem,      # Média da temperatura máxima
                    "media_chuva": soma_precip / contagem  # Média da precipitação
                }

            # Função que apresenta a média dos últimos registos no interface gráfico
            def ver_media(tipo_procura, frame_destino):
                registos = bd.obter_ultimos_registos(uid,
                                                     tipo_procura)  # Obtém os registos do histórico para o tipo de procura

                # Remove qualquer widget antigo do frame de destino
                model.Remover_frames.limpar_widgets_do_frame(frame_destino)

                # Se não houver registos, mostra mensagem ao utilizador
                if not registos:
                    texto = f"Sem dados do tipo '{tipo_procura}' para calcular média."
                else:
                    medias = calcular_media_registos(registos)  # Calcula as médias a partir dos registos

                    # Cria um frame visual para apresentar o texto das médias
                    frame_texto = ctk.CTkFrame(frame_destino, width=285, height=85, fg_color="#F0F0F0",
                                               corner_radius=10)
                    frame_texto.grid(row=0, column=0, padx=10, pady=10)

                    # Se não foi possível calcular médias, mostra mensagem
                    if not medias:
                        texto = f"Sem dados de {tipo_procura} para os últimos 30 registos."
                    else:
                        # Cria o texto com os dados médios formatados
                        texto = (
                            f"📊 Média dos Últimos 30 Dias ({tipo_procura})\n"
                            f"🌡 Temp. Mínima Média: {medias['media_min']:.1f}°C\n"
                            f"🔥 Temp. Máxima Média: {medias['media_max']:.1f}°C\n"
                            f"🌧 Precipitação Média: {medias['media_chuva']:.1f}%"
                        )

                # Mostra o texto das médias (ou mensagem de erro) dentro de um label no frame
                label_resultado = ctk.CTkLabel(
                    frame_destino, text=texto, font=("Arial", 14),
                    text_color="black", fg_color="#F0F0F0"
                )
                label_resultado.grid(row=0, column=0, columnspan=2, pady=10)

            botao_vermed_met_localidade = ctk.CTkButton(
                janela_APP,
                text="Ver Média Meteorologia (Localidade)",
                command=lambda: ver_media("Localidade", frame_combobox_localidade))
            botao_vermed_met_localidade.place(relx=0.225, rely=0.95, anchor="center")

            botao_vermed_met_destino = ctk.CTkButton(
                janela_APP,
                text="Ver Média Meteorologia (Destino)",
                command=lambda: ver_media("Destino", frame_combobox_destino))
            botao_vermed_met_destino.place(relx=0.725, rely=0.95, anchor="center")

            label_texto_localidade = ctk.CTkLabel(janela_APP, text="Localidade:", font=("Arial", 15),
                                                  text_color="black")
            label_texto_localidade.place(relx=0.05, rely=0.15, anchor="center")

            frame_menu_localidades = ctk.CTkFrame(janela_APP, fg_color="white", border_width=2,
                                                  border_color="#2E2E2E", corner_radius=5, width=207, height=37)
            frame_menu_localidades.place(relx=0.19, rely=0.15, anchor="center")

            label_localidade = ctk.CTkLabel(janela_APP, text=f"{localizacao}", font=("Arial", 15),
                                            fg_color="white", text_color="black")
            label_localidade.place(relx=0.19, rely=0.15, anchor="center")

            label_dias_localidade = ctk.CTkLabel(janela_APP, text="Dias:", font=("Arial", 15),
                                                 text_color="black")
            label_dias_localidade.place(relx=0.03, rely=0.23, anchor="center")

            frame_menu_dias_localidade = ctk.CTkFrame(janela_APP, fg_color="white", border_width=2,
                                                      border_color="black", corner_radius=5, width=131,
                                                      height=37)
            frame_menu_dias_localidade.place(relx=0.155, rely=0.23, anchor="center")

            valor_dias_localidade = ctk.StringVar(value="Selecionar")

            menu_dias_localidade = ctk.CTkOptionMenu(janela_APP, values=["1", "3", "5"],
                                                     variable=valor_dias_localidade, width=124, height=30,
                                                     font=("Arial", 15), fg_color="white", button_color="white",
                                                     text_color="black", dropdown_font=("Arial", 15),
                                                     command=atualizar_previsao_localidade)
            menu_dias_localidade.place(relx=0.155, rely=0.23, anchor="center")

            try:
                caminho_imagem = self.dados.caminho_recurso("imagens/imagem_logout.png")
                imagem_perfil = ctk.CTkImage(Image.open(caminho_imagem), size=(25, 25))
                botao_perfil = ctk.CTkButton(frame_cabecalho, image=imagem_perfil, text="Logout",
                                             font=("Arial", 12), text_color="Black", width=25, height=25,
                                             corner_radius=999, fg_color="#F7DE44", hover_color="white",
                                             command=logout)
                botao_perfil.place(relx=0.945, rely=0.5, anchor="center")

            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar imagem de perfil: {e}")
            atualizar_previsao_destino()
            janela_APP.mainloop()

if __name__ == "__main__":
    App()
