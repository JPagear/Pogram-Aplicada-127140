import os
import sys
from PIL import Image
import customtkinter as ctk
import smtplib
import random
from email.message import EmailMessage
from tkinter import messagebox
from time import sleep


class Historico:
    def __init__(self, localizacao, temperatura_min, temperatura_max, precip, descricao, tipo_procura):
        # Inicializa os atributos de um registo histórico meteorológico
        self.localizacao = localizacao
        self.temperatura_min = temperatura_min
        self.temperatura_max = temperatura_max
        self.precipitacao = precip
        self.descricao = descricao
        self.tipo_procura = tipo_procura


class Utilizador:
    def __init__(self, nome, senha, uid, mail, localizacao):
        # Inicializa os atributos de um utilizador
        self.nome = nome
        self.senha = senha
        self.uid = uid
        self.mail = mail
        self.localizacao = localizacao



class Obter_imagens:
    def __init__(self):
        # Define a base de onde os recursos (imagens) serão carregados
        if hasattr(sys, '_MEIPASS'):
            self.base = sys._MEIPASS  # Para aplicações empacotadas como com o PyInstaller
        else:
            self.base = os.path.abspath(".")

    def caminho_recurso(self, caminho_relativo):
        # Retorna o caminho absoluto de um ficheiro a partir do caminho relativo
        return os.path.join(self.base, caminho_relativo)

    def config_imagem(self, png, frame, size, relx, rely, bg_color=None):
        # Carrega uma imagem e coloca-a no frame especificado
        try:
            caminho_imagem = self.caminho_recurso(png)
            imagem = ctk.CTkImage(Image.open(caminho_imagem), size=size)
            label_logo = ctk.CTkLabel(frame, image=imagem, text="", bg_color=bg_color)
            label_logo.place(relx=relx, rely=rely, anchor="center")
        except Exception as e:
            # Mostra um erro se não for possível carregar a imagem
            messagebox.showerror(f"Erro ao carregar imagem", f"Erro ao carregar imagem '{png}': {e}")


class Remover_frames:
    @staticmethod
    def limpar_widgets_do_frame(frame):
        # Remove todos os widgets de um frame
        for widget in frame.winfo_children():
            widget.destroy()


class Esconder_frames:
    @staticmethod
    def limpar_widgets_do_frame(frame):
        # Esconde todos os widgets de um frame
        for widget in frame.winfo_children():
            widget.forget()

class Visual_senha:
    def __init__(self, entrada, botao):
        self.entrada = entrada  # Campo de entrada de texto (password)
        self.botao = botao      # Botão para alternar visibilidade da password
        self.estado = False     # Estado inicial: senha oculta

    def alternar_modo_visual_senha(self):
        if self.estado:
            # Tornar senha oculta
            self.entrada.configure(show="*")
            self.botao.configure(text="👁")
            self.estado = False
        else:
            # Tornar senha visível
            self.entrada.configure(show="")
            self.botao.configure(text="🙈")
            self.estado = True



class EmailConfirmacao:
    def __init__(self):
        # Configuração do servidor de envio de e-mails
        self.EMAIL_REMETENTE = "weather2travel.senhas@gmail.com"
        self.SENHA_APP = "ehbf gvdz uzbd pcuz"  # Senha da app (não a senha da conta!)
        self.SERVIDOR_SMTP = "smtp.gmail.com"
        self.PORTA_SMTP = 465

    def gerar_codigo(self):
        # Gera um código de 4 dígitos para verificação
        return str(random.randint(1000, 9999))

    def enviar(self, email_destino):
        # Envia o código para o e-mail fornecido
        codigo = self.gerar_codigo()
        assunto = "Código de confirmação de conta - Weather2Travel"
        mensagem = (f"Código necessário para confirmar a sua conta na App Weather2Travel:\n\n{codigo}")

        try:
            msg = EmailMessage()
            msg["From"] = self.EMAIL_REMETENTE
            msg["To"] = email_destino
            msg["Subject"] = assunto
            msg.set_content(mensagem)

            with smtplib.SMTP_SSL(self.SERVIDOR_SMTP, self.PORTA_SMTP) as smtp:
                smtp.login(self.EMAIL_REMETENTE, self.SENHA_APP)
                smtp.send_message(msg)

            return codigo  # Retorna o código para validação posterior
        except Exception:
            return  # Em caso de erro, retorna None


class EnviarEmailVerificacao:
    def __init__(self, frame_fundo, entrada_email, label_aviso, bd, func_mostrar_frame_codigo):
        self.frame_fundo = frame_fundo
        self.entrada_email = entrada_email
        self.label_aviso = label_aviso
        self.bd = bd
        self.func_mostrar_frame_codigo = func_mostrar_frame_codigo

        self.email_remetente = "weather2travel.senhas@gmail.com"
        self.senha_app = "ehbf gvdz uzbd pcuz"

    def enviar_mail(self):
        numero_mail = str(random.randint(1000, 9999))
        assunto = "Código de confirmação de conta - Weather2Travel"
        mensagem = f"Código necessário para mudar a senha da sua conta:\n\n{numero_mail}"

        destinatario = self.entrada_email.get().strip()

        if not destinatario:
            self.label_aviso.configure(text="*Este campo é Obrigatório!", text_color="red")
            return

        if not self.bd.verificar_mail(destinatario):
            messagebox.showerror("E-mail Inválido", "O E-mail não está associado a uma conta")
            return

        try:
            msg = EmailMessage()
            msg["From"] = self.email_remetente
            msg["To"] = destinatario
            msg["Subject"] = assunto
            msg.set_content(mensagem)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(self.email_remetente, self.senha_app)
                smtp.send_message(msg)

            self.label_aviso.configure(text="A enviar e-mail...", text_color="white")
            self.frame_fundo.update()
            sleep(1)

            self.label_aviso.configure(text="Mail enviado com sucesso!\nVerifique o seu e-mail.", text_color="green")
            self.frame_fundo.update()
            sleep(2)

            self.func_mostrar_frame_codigo(numero_mail)

        except Exception:
            self.label_aviso.configure(text="Insira um mail válido!", text_color="red")
