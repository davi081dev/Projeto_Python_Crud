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

def obterInputValido(mensagem, tipo=str):
     
     while True:
          entrada = input(mensagem).strip()

          if entrada == '' or entrada == None:
               print('\n❌ Este campo é obrigatório. Por favor, preencha.\n') 
               continue

          if tipo == int:
               if entrada.isdigit():
                    return int(entrada)
               
               else:
                    print("\n❌ Digite um número válido.\n")
                    continue
          return entrada
        
def cadastrar_adotante(dados_adotante):
    print("\n🦴\033[30;47m Olá, bem-vindo à área de cadastro dos adotantes de animais. \033[m🦴")

    print("\n📌 Dados Pessoais\n")
    
    while True:
        nome_adotante = obterInputValido("Nome completo: ").upper()
        if all(caractere.isalpha() or caractere.isspace() for caractere in nome_adotante):
            print("✅")
            break
        else:
             print("Use apenas letras e espaços. Tente novamente.")


    nascimento_adotante = obterInputValido("Data de nascimento (DD/MM/AAAA): ")
    print("✅")

    while True:
        email_adotante = obterInputValido("E-mail: ")
        if '@'in email_adotante and '.' in email_adotante and email_adotante.count('@') == 1:
            print("✅")
            break
        else:
            print("E-mail inválido! Digite no formato: nome@provedor.com")

    print("✅")
            
    while True:
        estado_civil_adotante = obterInputValido("Informe seu estado civil:\n-SOLTEIRO\n-CASADO\n-VIÚVO\n-DIVORCIADO\n-SEPARADO\n: ").upper()
        if estado_civil_adotante == "SOLTEIRO" or estado_civil_adotante == "CASADO" or estado_civil_adotante == "VIUVO" or estado_civil_adotante == "VIÚVO" or estado_civil_adotante == "DIVORCIADO" or estado_civil_adotante == "SEPARADO":
            print("✅")
            break
        else:
            print("Opção inválida! Digite um estado civil válido.")

    while True:
        telefone_adotante_entrada = obterInputValido("Telefone [(XX) XXXXX-XXXX: ]:")
        telefone_adotante = ''.join(filter(str.isdigit,telefone_adotante_entrada))

        if len(telefone_adotante) == 11:
            telefone_adotante = f"({telefone_adotante[:2]}) {telefone_adotante[2:7]}-{telefone_adotante[7:]}"
            print("✅")
            break
        else:
            print("Número inválido! Digite um telefone com 11 dígitos (DDD + número com 9° digito).")

    while True:
        sexo_adotante = obterInputValido("Informe seu sexo[M/F]: ").upper()
        if sexo_adotante == "M" or sexo_adotante == "F":
            print("✅")
            break
        else:
            print("Opção inválida! Digite apenas M ou F.")

    
    print("\n📍 Dados de endereço\n")

    while True:
        cidade_adotante = obterInputValido("Cidade: ").upper()
        if all(caractere.isalpha() or caractere.isspace() for caractere in cidade_adotante):
            print("✅")
            break
        else:
            print("Use apenas letras e espaços. Tente novamente.")

    while True:
            bairro_adotante = obterInputValido("Bairro: ").upper()
            if all(caractere.isalpha() or caractere.isspace() for caractere in bairro_adotante):
                print("✅")
                break
            else:
                print("Use apenas letras e espaços. Tente novamente.")

    while True:
                rua_adotante = obterInputValido("Rua:").upper()
                if all(caractere.isalpha() or caractere.isspace() for caractere in rua_adotante):
                    print("✅")
                    break
                else:
                    print("Use apenas letras e espaços. Tente novamente.")

    while True:
        numero_adotante = obterInputValido("Número: ")
        if numero_adotante.isdigit():
            print("✅")
            break
        else:
            print("Use apenas números. Tente novamente.")

    print("🐶 Dados sobre a Adoção")
    animal_interesse_adotante = obterInputValido("Qual o animal que tem interesse?: ").upper()
    print("✅")

    raça_interesse_adotante = obterInputValido("Qual a raça da sua preferência?: ")
    print("✅")
    while True:
            sexo_interesse_adotante= obterInputValido("Qual a sua preferência para o sexo?(M/F): ").upper()
            if sexo_interesse_adotante == "M" or sexo_interesse_adotante == "F":
                print("✅")
                break
            else:
                print("Opção inválida! Digite apenas M ou F.")

    while True:
        porte_interesse = obterInputValido("Qual o porte de sua preferência?: \n(0-10 kg)-Pequeno\n(11-24 kg)-Médio\n(25-...)-Grande\n:").upper()
        if porte_interesse == "PEQUENO" or porte_interesse == "MEDIO" or porte_interesse == "MÉDIO" or porte_interesse == "GRANDE":
            print("✅")
            break
        else:
            print("Opção inválida! Digite um Porte válido.")

    while True:
            faixa_etaria_adotante = obterInputValido("Qual a idade da sua preferência:\n(0-1 ano)-Filhote\n(1-6 anos)-Jovem\n(7-10 anos)-Adulto\n(10-... anos)-Idoso\n: ").upper()
            if faixa_etaria_adotante.isdigit:
                print("✅")
                break
            else:
                print("Opção inválida! Digite uma Faixa etária válida.")

    while True:
        condicoes_interesse_adotante = obterInputValido("Tem interesse em adotar animais com condições especiais(Deficiências, doenças crônicas, entre outros...)?: ").upper()
        if condicoes_interesse_adotante == "S" or condicoes_interesse_adotante == "N":
            print("✅")
            break
        else:
            print("Opção inválida! Digite S ou N")

    print("\n🔒 Termos e Consentimentos\n")
    while True:
        termo_responsabilidade_adotante = input("Você concorda com os termos de responsabilidade como adotante?[S/N] ").upper()
        if termo_responsabilidade_adotante == "S":
            print("Termo de responsabilidade assinado!✅")
            break
        elif termo_responsabilidade_adotante == "N":
            print("Termo de responsabilidade não assinado, você precisa assinar para continuar!")
            return
        else:
            print("Opção inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
            
    while True:
        autorizacao_visita_adotante = input("Você concorda o termo de visita a residência?[S/N] ").upper()
        if autorizacao_visita_adotante == "S":
            print("Termo de visita assinado!✅")
            break
        elif autorizacao_visita_adotante == "N":
            print("Termo de visita não assinado, você precisa assinar para continuar!")
            return
        else:
            print("Opção inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
            
    while True:
        permissao_dados_adotante = input("Você concorda com o acesso as suas informações?[S/N] ").upper()
        if permissao_dados_adotante == "S":
            print("Termo de permissão de dados assinado!✅")
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
            print("\033[32mAdotante cadastrado com sucesso.\033[m")
            salvar_dados(dados_adotante)
            return
   
def remover_adotante(dados_adotante):
    while True: 
        if not dados_adotante:
            print("\033[31mNenhum adotante cadastrado.\033[m")
            return
        cpf_adotante = input("\nInforme o CPF que você deseja remover: ")
        if cpf_adotante in dados_adotante:
            del dados_adotante[cpf_adotante]
            salvar_dados(dados_adotante)
            print("\033[32mAdotante removido com sucesso.\033[m")
            return
        else:
            while True:
                print("\033[31mAdotante não encontrado.\033[m")
                opcao= str(input("Deseja tentar novamente?[S/N] ").upper()) 
                if (opcao != 'S' and opcao != 'N'):
                    print("\033[31mOpção inválida.Por favor, digite 'S' ou 'N'.\033[m")

                elif (opcao != 'S'):
                    print("\n\033[32mVoltando para o menu...\033[m")
                    return
                else:
                    break
                
def editar_adotante(dados_adotante):
    while True:
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
                                            "Estado civil": novo_estado_civil,
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
            return
        else:
            while True:
                    print("\033[31mAdotante não encontrado.\033[m")
                    opcao= str(input("Deseja tentar novamente?[S/N] ").upper()) 
                    if (opcao != 'S' and opcao != 'N'):
                        print("\033[31mOpção inválida\033[m")

                    elif (opcao != 'S'):
                        print("\n\033[32mVoltando para o menu...\033[m")
                        return
                    else:
                        break

def listar_adotantes(dados_adotante):
    if not dados_adotante:
        print("\n\033[31mNenhum adotante cadastrado.\033[m")
        return
    for cpf_adotante in dados_adotante:
        print(f"\n\033[35mNome: {dados_adotante[cpf_adotante]['Nome']}\033[m")

def buscar_adotantes(dados_adotante):
    while True:
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
            return
        else:
            while True:
                    print("\033[31mAdotante não encontrado.\033[m")
                    opcao= str(input("Deseja tentar novamente?[S/N] ").upper()) 
                    if (opcao != 'S' and opcao != 'N'):
                        print("\033[31mOpção inválida\033[m")

                    elif (opcao != 'S'):
                        print("\n\033[32mVoltando para o menu...\033[m")
                        return
                    else:
                        break

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
        print("5-Buscar Adotante")
        print("6-Sair")

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
            buscar_adotantes(dados_adotante)
        elif opcao == 6:
            salvar_dados(dados_adotante)
            return
        else:
            print("Opção Inválida. Por favor, digite um número de 1 a 6")                
crud_cpf_adotante()