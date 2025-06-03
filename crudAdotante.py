import json
import os

def carregar_dados():
    if os.path.exists("adotantes.json"):
        with open("adotantes.json", "r") as f:
                return json.load(f)
    return {}

def salvar_dados(dados_adotante):
    with open("adotantes.json", "w") as f:
        json.dump(dados_adotante, f, indent=4)
        
def cadastrar_adotante(dados_adotante):
    print("\n🦴\033[30;47m Olá, bem-vindo à área de cadastro dos adotantes de animais. \033[m🦴")
    print("\n📌 Dados Pessoais\n")
    nome_adotante = input("\nInforme seu nome: ")
    nascimento_adotante = input("Informe sua data de nascimento:[DD/MM/AAAA] ")
    estado_civil_adotante = input("Informe seu estado civil: ")
    telefone_adotante = input("Informe um telefone para contato: ")
    email_adotante = input("Informe seu email para contato: ")
    sexo_adotante = input("Informe seu sexo: ")
    
    print("\n📍 Dados de endereço\n")
    cidade_adotante = input("Cidade: ")
    bairro_adotante = input("Bairro: ")
    rua_adotante = input("Rua: ")
    numero_adotante = input("Número: ")
    
    print("🐶 Dados sobre a Adoção")
    animal_interesse_adotante = input("Qual o animal que tem interesse?: ")
    raça_interesse_adotante = input("Qual a raça da sua preferência?: ")
    sexo_interesse_adotante= input("Qual a sua preferência para o sexo?: ")
    porte_interesse = input("Qual o porte de sua preferência?: ")
    faixa_etaria_adotante = input("Qual a faixa etária da sua preferência: ")
    condicoes_interesse_adotante = input("Tem interesse em adotar animais com condições especiais(Deficiências, doenças crônicas, entre outros...)? ")

    print("\n🔒 Termos e Consentimentos\n")
    while True:
        termo_responsabilidade_adotante = input("Você concorda com os termos de responsabilidade como adotante?[S/N] ").upper()
        if termo_responsabilidade_adotante == "S":
            print("Termo de responsabilidade assinado!")
            break
        elif termo_responsabilidade_adotante == "N":
            print("Termo de responsabilidade não assinado, você precisa assinar para continuar!")
            return
        else:
            print("Opção inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
            
    while True:
        autorizacao_visita_adotante = input("Você concorda o termo de visita a residência?[S/N] ").upper()
        if autorizacao_visita_adotante == "S":
            print("Termo de visita assinado!")
            break
        elif autorizacao_visita_adotante == "N":
            print("Termo de visita não assinado, você precisa assinar para continuar!")
            return
        else:
            print("Opção inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
            
    while True:
        permissao_dados_adotante = input("Você concorda com o acesso as suas informações?[S/N] ").upper()
        if permissao_dados_adotante == "S":
            print("Termo de permissão de dados assinado!")
            break
        elif permissao_dados_adotante == "N":
            print("Termo de permissão de dados não assinado, você precisa assinar para continuar!")
            return
        else:
            print("Opção inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")  

    while True:
        cpf_adotante = input("Informe seu CPF (XXX.XXX.XXX-XX) ou digite 'sair' para voltar: ")
        if cpf_adotante == 'sair':
            return
        if cpf_adotante in dados_adotante:
            print("\033[31mCPF já cadastrado.\033[m")
        else:
            dados_adotante[cpf_adotante] = {
                                            "Nome": nome_adotante, 
                                            "Data de nascimento": nascimento_adotante, 
                                            "Estado civil": estado_civil_adotante,
                                            "Telefone": telefone_adotante, 
                                            "Email": email_adotante,
                                            "Sexo": sexo_adotante,
                                            "Cidade": cidade_adotante,
                                            "Bairro": bairro_adotante,
                                            "Rua": rua_adotante,
                                            "Numero": numero_adotante,
                                            
                                            "Animal de interesse": animal_interesse_adotante,
                                            "Raca de interesse": raça_interesse_adotante,
                                            "Sexo de interesse": sexo_interesse_adotante,
                                            "Porte de interesse": porte_interesse,
                                            "Faixa etaria de interesse": faixa_etaria_adotante,
                                            "Condicoes de interesse": condicoes_interesse_adotante,
                                            
                                            }
            print("\033[32mUsuário cadastrado com sucesso.\033[m")
            salvar_dados(dados_adotante)
            return
   
def remover_adotante(dados_adotante): 
    if not dados_adotante:
        print("\033[31mNenhum adotante cadastrado.\033[m")
        return
    cpf_adotante = input("\nInforme o CPF que você deseja remover: ")
    if cpf_adotante in dados_adotante:
        del dados_adotante[cpf_adotante]
        salvar_dados(dados_adotante)
        print("\033[32mAdotante removido com sucesso.\033[m")
    else:
        print("\033[31mAdotante não encontrado.\033[m")

def editar_adotante(dados_adotante):
    if not dados_adotante:
        print("\n\033[31mNenhum adotante cadastrado.\033[m")
        return
    cpf_adotante = input("\nInforme o CPF do adotante que você deseja editar: ")
    if cpf_adotante in dados_adotante:
        print("\n\033[31;47m Deixe em branco para manter o valor atual. \033[m")
        nome_adotante = input(f"Novo nome ({dados_adotante[cpf_adotante]['Nome']}): ") or dados_adotante[cpf_adotante]['Nome']
        nascimento_adotante = input(f"Nova data de nascimento ({dados_adotante[cpf_adotante]['Data de nascimento']}): ") or dados_adotante[cpf_adotante]['Data de nascimento']
        novo_estado_civil = input(f"Novo estado civil ({dados_adotante[cpf_adotante]['Estado civil']}): ") or dados_adotante[cpf_adotante]['Estado civil']
        novo_telefone = input(f"Novo telefone ({dados_adotante[cpf_adotante]['Telefone']}): ") or dados_adotante[cpf_adotante]['Telefone']
        novo_email = input(f"Novo email ({dados_adotante[cpf_adotante]['Email']}): ") or dados_adotante[cpf_adotante]['Email']
        novo_sexo = input(f"Novo sexo ({dados_adotante[cpf_adotante]['Sexo']}): ") or dados_adotante[cpf_adotante]['Sexo']
        
        nova_cidade = input(f"Nova cidade ({dados_adotante[cpf_adotante]['Cidade']}): ") or dados_adotante[cpf_adotante]['Cidade']
        novo_bairro = input(f"Novo bairro ({dados_adotante[cpf_adotante]['Bairro']}): ") or dados_adotante[cpf_adotante]['Bairro']
        nova_rua = input(f"Nova rua ({dados_adotante[cpf_adotante]['Rua']}): ") or dados_adotante[cpf_adotante]['Rua']
        novo_numero = input(f"Novo numero ({dados_adotante[cpf_adotante]['Numero']}): ") or dados_adotante[cpf_adotante]['Numero']
        
        novo_animal_interesse = input(f"Novo animal de interesse({dados_adotante[cpf_adotante]['Animal de interesse']}): ") or dados_adotante[cpf_adotante]['Animal de interesse']
        nova_raça_interesse = input(f"Nova raca de interesse ({dados_adotante[cpf_adotante]['Raca de interesse']}): ") or dados_adotante[cpf_adotante]['Raca de interesse']
        novo_sexo_interesse = input(f"Novo sexo de interesse ({dados_adotante[cpf_adotante]['Sexo de interesse']}): ") or dados_adotante[cpf_adotante]['Sexo de interesse']
        novo_porte = input(f"Novo porte de interesse ({dados_adotante[cpf_adotante]['Porte de interesse']}): ") or dados_adotante[cpf_adotante]['Porte de interesse']
        nova_faixa_etaria = input(f"Nova faixa etaria de interesse ({dados_adotante[cpf_adotante]['Faixa etaria de interesse']}): ") or dados_adotante[cpf_adotante]['Faixa etaria de interesse']
        novo_condicoes_interesse = input(f"Nova condicoes de interesse ({dados_adotante[cpf_adotante]['Condicoes de interesse']}): ") or dados_adotante[cpf_adotante]['Condicoes de interesse']
        
        dados_adotante[cpf_adotante] = {
                                        "Nome": nome_adotante, 
                                        "Data de nascimento": nascimento_adotante, 
                                        "Estado Civil": novo_estado_civil,
                                        "Telefone": novo_telefone, 
                                        "Email": novo_email,
                                        "Sexo": novo_sexo,
                                        "Cidade": nova_cidade,
                                        "Bairro": novo_bairro,
                                        "Rua": nova_rua,
                                        "Numero": novo_numero,
                                        "Animal de interesse": novo_animal_interesse,
                                        "Raca de interesse": nova_raça_interesse,
                                        "Sexo de interesse": novo_sexo_interesse,
                                        "Porte de interesse": novo_porte,
                                        "Faixa etaria de interesse": nova_faixa_etaria,
                                        "Condicoes de interesse": novo_condicoes_interesse,
                                    }
        salvar_dados(dados_adotante)
        print("\n\033[32mAdotante editado com sucesso.\033[32m")
    else:
        print("\n\033[31mAdotante não encontrado.\033[m")

def listar_adotantes(dados_adotante):
    if not dados_adotante:
        print("\n\033[31mNenhum adotante cadastrado.\033[m")
        return
    for cpf_adotante in dados_adotante:
        print(f"\n\033[35mNome: {dados_adotante[cpf_adotante]['Nome']}\033[m")

def buscar_adotantes(dados_adotante):
    if not dados_adotante:
        print("\n\033[31mNenhum adotante cadastrado.\033[m")
        return
    cpf_adotante = input("\nInforme o CPF do adotante que você deseja ver os dados: ")
    if cpf_adotante in dados_adotante:
        print(f"\n\033[35;47m DADOS DO ADOTANTE: {dados_adotante[cpf_adotante]['Nome']} \033[m")
        print(f"\033[35mNome: {dados_adotante[cpf_adotante]['Nome']}\033[m")
        print(f"\033[35mData de Nascimento: {dados_adotante[cpf_adotante]['Data de nascimento']}\033[m")
        print(f"\033[35mEstado civil: {dados_adotante[cpf_adotante]['Estado civil']}\033[m")
        print(f"\033[35mTelefone: {dados_adotante[cpf_adotante]['Telefone']}\033[m")
        print(f"\033[35mEmail: {dados_adotante[cpf_adotante]['Email']}\033[m")
        print(f"\033[35mSexo: {dados_adotante[cpf_adotante]['Sexo']}\033[m")
        print(f"\033[35mCidade: {dados_adotante[cpf_adotante]['Cidade']}\033[m")
        print(f"\033[35mBairro: {dados_adotante[cpf_adotante]['Bairro']}\033[m")
        print(f"\033[35mRua: {dados_adotante[cpf_adotante]['Rua']}\033[m")
        print(f"\033[35mNumero: {dados_adotante[cpf_adotante]['Numero']}\033[m")
        print(f"\033[35mAnimal de Interesse: {dados_adotante[cpf_adotante]['Animal de interesse']}\033[m")
        print(f"\033[35mRaca de interesse: {dados_adotante[cpf_adotante]['Raca de interesse']}\033[m")
        print(f"\033[35mSexo de interesse: {dados_adotante[cpf_adotante]['Sexo de interesse']}\033[m")
        print(f"\033[35mPorte de interesse: {dados_adotante[cpf_adotante]['Porte de interesse']}\033[m")
        print(f"\033[35mFaixa etaria de interesse: {dados_adotante[cpf_adotante]['Faixa etaria de interesse']}\033[m")
        print(f"\033[35mCondicoes de interesse: {dados_adotante[cpf_adotante]['Condicoes de interesse']}\033[m")
    else:
        print("\033[31mAdotante não encontrado.\033[m")

def crud_cpf_adotante():
    dados_adotante = carregar_dados()
    
    print("-" * 40)
    print(" SEJA BEM VINDO A TELA DE ADOTANTES😁")
    print("-" * 40)

    while True:
        print("\n       \033[30;47m   ==== MENU ====   \033[m")
        print("1-Cadastrar Adotante")
        print("2-Listar Adotantes")
        print("3-Editar Adotante")
        print("4-Remover adotante")
        print("5-Sair")
        print("6-Buscar Adotante")

        try:
            opcao = int(input("Informe a opção desejada: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if opcao == 1:
            cadastrar_adotante(dados_adotante)
        elif opcao == 2:
            listar_adotantes(dados_adotante)
        elif opcao == 3:
            editar_adotante(dados_adotante)
        elif opcao == 4:
            remover_adotante(dados_adotante)
        elif opcao == 5:
            salvar_dados(dados_adotante)
            break
        elif opcao == 6:
            buscar_adotantes(dados_adotante)
        else:
            print("Opção inválida.")
