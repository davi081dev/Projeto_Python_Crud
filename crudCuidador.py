import json
import os

def carregar_dados():
    if os.path.exists("dados.json"):
        with open("dados.json", "r") as arquivo:
            return json.load(arquivo)
    return {}

def salvar_dados(dados):
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def cadastrar_usuario(dados):
    print("\n🦴\033[30;47m Olá, bem-vindo à área de cadastro dos adotantes de animais. \033[m🦴")
    nome = input("\nInforme seu nome: ")
    idade = int(input("Informe sua idade: "))
    telefone = input("Informe um telefone para contato: ")
    sexo = input("Informe seu sexo: ")

    while True:
        cpf = input("Informe seu CPF (XXX.XXX.XXX-XX) ou digite 'sair' para voltar: ")
        if (cpf == 'sair'):
            return
        elif cpf in dados:
            print("\033[31mCPF já cadastrado, tente novamente\033[m")
        else:
            dados[cpf] = {"nome": nome, "idade": idade, "telefone": telefone, "sexo": sexo}
            print("\033[32mUsuário cadastrado com sucesso.\033[m")
            salvar_dados(dados)
            return
        

def remover_usuario(dados):
        if not dados:
            print("\n\033[31mNenhum usuário cadastrado.\033[m")
            return
        else:
            while True:
                cpf_remover = input("\nInforme o CPF que você deseja remover: ")
                if cpf_remover in dados:
                    del dados[cpf_remover]
                    salvar_dados(dados)
                    print(f"\033[32mUsuário removido com sucesso.\033[m")

                    while True:
                        op01 = str(input("\nDeseja remover outro usuário ? (sim/não) "))

                        if (op01 != 'sim' and op01 != 'nao'):
                            print("\033[31mOpção invalida, tente novamente:\033[m ")

                        elif (op01 != 'sim'):
                            print("\033[32mVoltando pro menu...\033[m")
                            return
                        
                        else:
                            break

                else:
                    print("\033[31mUsuário não encontrado.\033[m")

                    while True:
                        opcao02=str(input("\nDeseja tentar novamente ? (sim/não) "))

                        if (opcao02 != 'sim' and opcao02 != 'nao'):
                            print("\033[31mOpção invalida\033[m")
                    
                        elif (opcao02 != 'sim'):
                            print("\n\033[32mVoltando para o menu...\033[m")
                            return
                        
                        else:
                            break


def editar_usuario(dados):
        if not dados:
            print("\n\033[31mNenhum usuário cadastrado.\033[m")
            return
        else:
            while True:
                cpf_edt = input("\nInforme o CPF do usuário que você deseja editar: ")
                if cpf_edt in dados:
                    print("\n\033[31;47m Deixe em branco para manter o valor atual. \033[m")
                    nome = input(f"Novo nome ({dados[cpf_edt]['nome']}): ") or dados[cpf_edt]['nome']
                    idade = input(f"Nova idade ({dados[cpf_edt]['idade']}): ") or dados[cpf_edt]['idade']
                    telefone = input(f"Novo telefone ({dados[cpf_edt]['telefone']}): ") or dados[cpf_edt]['telefone']
                    sexo = input(f"Novo sexo ({dados[cpf_edt]['sexo']}): ") or dados[cpf_edt]['sexo']
                    dados[cpf_edt] = {"nome": nome, "idade": idade, "telefone": telefone, "sexo": sexo}
                    salvar_dados(dados)
                    print("\033[32mUsuário editado com sucesso.\033[32m")

                    while True:
                        op02=str(input("\nDeseja editar outro usuário ? (sim/não) "))

                        if (op02 != 'sim' and op02 != 'nao'):
                            print("\033[31mOpção invalida, tente novamente.\033[m")

                        elif (op02 != 'sim'):
                            print("\n\033[32mVoltandopro menu...\033[m")
                            return
                        
                        else:
                            break

                else:
                    print("\033[31mUsuário não encontrado.\033[m")

                    while True:
                        opcao03=str(input("\nDeseja tentar novamente ? (sim/não) "))
                        if (opcao03 != 'sim' and opcao03 != 'nao'):
                            print("\033[31mOpção invalida\033[m")
                        
                        elif (opcao03 != 'sim'):
                            print("\n\033[32mVoltando para o menu...\033[m")
                            return
                        
                        else:
                            break


def listar_usuarios(dados):
    if not dados:
        print("\n\033[31mNenhum usuário cadastrado.\033[m")
        return
    else:
        for cpf in dados:
            print(f"\n\033[35mNome: {dados[cpf]['nome']}\033[m")

    while True:
        opcao04=str(input("\nDigite 'sair' para voltar pro menu: "))

        if (opcao04 == 'sair'):
            print("\n\033[32mVoltando...\033[m")
            return
        
        else:
            print("\033[31mOpção invalida, tente novamente:\033[m")


def buscar_usuario(dados):
    while True:
        if not dados:
            print("\n\033[31mNenhum usuário cadastrado.\033[m")
            return
        else:
            cpf = input("\nInforme o CPF do usuário que você deseja ver os dados: ")
            if cpf in dados:
                print(f"\n\033[35;47m DADOS DO USUÁRIO: {dados[cpf]['nome']} \033[m")
                print(f"\033[35mNome: {dados[cpf]['nome']}\033[m")
                print(f"\033[35mIdade: {dados[cpf]['idade']}\033[m")
                print(f"\033[35mSexo: {dados[cpf]['sexo']}\033[m")
                print(f"\033[35mTelefone: {dados[cpf]['telefone']}\033[m")

                while True:
                    op03=str(input("\nDeseja buscar outro usuário ? (sim /não) "))

                    if (op03 != 'sim' and op03 != 'nao'):
                        print("\033[31mOpção invalida, tente novamente:\033[m")

                    elif (op03 != 'sim'):
                        print("\n\033[32mVoltando pro menu...\033[m")
                        return
                    
                    else:
                        break
            else:
                print("\033[31mUsuário não encontrado.\033[m")

                while True:
                    opcao05=str(input("\nDeseja tentar novamente ? (sim/não) "))

                    if (opcao05 != 'sim' and opcao05 != 'nao'):
                        print("\033[31mOpção invalida, tente novamente:\033[m")

                    elif (opcao05 != 'sim'):
                        print("\n\033[32mVoltando para o menu...\033[m")
                        return

                    else:
                        break


def menu_adm(dados):
    while True:
        senha = input("\nInforme a senha ou digite 'sair' para voltar: ")
        if senha == 'sair':
            return
        if senha == 'gruponota10':
            print("\n\033[47mDADOS DOS USUÁRIOS:\033[m")
            for cpf in dados:
                print(f"\n\033[35mNome: {dados[cpf]['nome']}\033[m")
                print(f"\033[35mCpf: {cpf}\033[m")
                print(f"\033[35mIdade: {dados[cpf]['idade']}\033[m")
                print(f"\033[35mTelefone: {dados[cpf]['telefone']}\033[m")
                print(f"\033[35mSexo: {dados[cpf]['sexo']}\033[m")
            break
        else:
            print("\033[31mSenha incorreta, tente novamente:\033[m")

    while True:
        voltar = input("\nDigite 'sair' para voltar pro menu: ")
        
        if voltar == 'sair':
            print("\n\033[32mVoltando...\033[m")
            return
        print("\033[31mErro, tente novamente:\033[m")


def crud_cpf_cuidador():
    dados = carregar_dados()

    print("-" * 40)
    print(" 🐶-- BEM VINDOS AO PET-SHOP \033[31mCESAR\033[m --🐶")
    print("-" * 40)

    while True:
        print("\n       \033[30;47m   ==== MENU ====   \033[m")
        print("Digite 1 para CADASTRO")
        print("Digite 2 para REMOVER o cadastro")
        print("Digite 3 para EDITAR o usuário")
        print("Digite 4 para LISTAR os usuários")
        print("Digite 5 para BUSCAR um usuário")
        print("Digite 6 para SAIR")
        print("\033[31m*APENAS PARA ADM*\033[m DIGITO 7")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            cadastrar_usuario(dados)
        elif opcao == 2:
            remover_usuario(dados)
        elif opcao == 3:
            editar_usuario(dados)
        elif opcao == 4:
            listar_usuarios(dados)
        elif opcao == 5:
            buscar_usuario(dados)
        elif opcao == 6:
            salvar_dados(dados)
            break
        elif opcao == 7:
            menu_adm(dados)
        else:
            print("Opção inválida.")

