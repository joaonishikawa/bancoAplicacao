import time
import os
import random

class Conta:
    def __init__(self, numero_conta, email, nome, senha, saldo):
        self.numero_conta = numero_conta
        self.email = email
        self.nome = nome
        self.senha = senha
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.contas = []

    def registrar_conta(self):
        email = input("Digite o email: ")
        nome = input("Digite o nome: ")
        senha = input("Digite a senha: ")
        saldo = float(input("Digite o saldo inicial: "))

        # Gerar um número de conta aleatório de 4 dígitos
        numero_conta = random.randint(1000, 9999)

        # Criar uma nova conta
        nova_conta = Conta(numero_conta, email, nome, senha, saldo)
        self.contas.append(nova_conta)
        print("Registro concluído com sucesso. Seu número de conta é:", numero_conta)

    def efetuar_login(self):
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")

        for conta in self.contas:
            if conta.email == email and conta.senha == senha:
                print("Login realizado com sucesso. Bem-vindo,", conta.nome)
                self.exibir_menu_conta(conta)
                return

        print("Email ou senha incorretos.")

    def exibir_menu_inicial(self):
        while True:
            print("\n=== BANCO IANES ===")
            print("1 - Registrar")
            print("2 - Login")
            print("3 - Sair")
            print('===================')

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.registrar_conta()
            elif opcao == "2":
                self.efetuar_login()
                return  # Retorna para encerrar a execução do menu inicial
            elif opcao == "3":
                print("Programa encerrado.")
                return
            else:
                print("Opção inválida.")

    def exibir_menu_conta(self, conta):
        while True:
            time.sleep(3)
            os.system('cls')
            print("\n=== BANCO IANES ===")
            print("Bem-vindo,", conta.nome)
            print(f"Saldo: R${conta.saldo}")
            print("1 - Sacar")
            print("2 - Depositar")
            print("3 - Extrato")
            print("4 - Voltar ao menu inicial")
            print('===================')

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                valor = float(input("Digite o valor a ser sacado: "))
                if valor <= conta.saldo:
                    conta.saldo -= valor
                    print("Saque realizado com sucesso.")
                else:
                    print("Saldo insuficiente.")
            elif opcao == "2":
                valor = float(input("Digite o valor a ser depositado: "))
                conta.saldo += valor
                print("Depósito realizado com sucesso.")
            elif opcao == "3":
                print("Extrato:", conta.__dict__)
            elif opcao == "4":
                print("Voltando ao menu inicial.")
                return
            else:
                print("Opção inválida.")
