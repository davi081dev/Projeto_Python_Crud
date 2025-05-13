import json
import os



#Função para coletar os dados pessoais do adotante
def dados_pessoais_adotante():
    print("🐾 Bem-vindo(a) ao seu novo começo cheio de amor!\n")
    print("\nEstamos muito felizes por você estar aqui! Ao adotar, você não só ganha um amigo leal, mas também dá a um animal a chance de uma vida digna e cheia de carinho.")
    print("\nPara começarmos essa jornada, precisamos de algumas informações sobre você. O cadastro é rápido e seguro, e cada detalhe nos ajuda a garantir a melhor adoção possível.")
    print("\nPreencha os campos abaixo com seus dados – em breve, você estará mais perto de encontrar seu companheiro perfeito!")
    print("\n📌 Dados Pessoais\n")

    #Solicitação do nome Completo
    while True:
        nome_adotante = input("Nome completo: ")
        if all(caractere.isalpha() or caractere.isspace() for caractere in nome_adotante):
            print("✅")
            break
        else:
            print("Use apenas letras e espaços. Tente novamente.")

    #Solicitação da data de nascimento
    from datetime import datetime
    while True:
        nascimento_adotante = input("Data de nascimento (DD/MM/AAAA): ")
        try:
            nascimento_adotante_formatado = datetime.strptime(nascimento_adotante, "%d/%m/%Y")
            if(datetime.now() - nascimento_adotante_formatado).days/365 >= 18:
                print("✅")
                break
            else:
                print("É necessário ser maior de 18 anos!")
        except ValueError:
            print("Formato inválido! Siga o modelo: DD/MM/AAAA")

    #Solicitação de Cpf
    while True:
        cpf_adotante_entrada = input("Cpf (XXX.XXX.XXX-XX): ")
        cpf_adotante = ''.join(filter(str.isdigit,cpf_adotante_entrada))

        if len(cpf_adotante_entrada) == 11:
            cpf_adotante_formatado = f"{cpf_adotante_entrada[:3]}.{cpf_adotante_entrada[4:6]}.{cpf_adotante_entrada[7:9]}-{cpf_adotante_entrada[10:11]}"
            print("✅")
            break
        else:
            print("Formato inválido! Siga o modelo: XXX.XXX.XXX-XX")

    estado_civil_adotante = input("Estado civil: ")

    print("\n📞 Dados de Contato\n")

    #Solicitação do número de telefone
    while True:
        telefone_adotante_entrada = (input("Telefone: "))
        telefone_adotante = ''.join(filter(str.isdigit,telefone_adotante_entrada))

        if len(telefone_adotante) == 11:
            telefone_adotante_formatado = f"({telefone_adotante[:2]}) {telefone_adotante[2:7]}-{telefone_adotante[7:]}"
            print("✅")
            break
        else:
            print("Número inválido! Digite um telefone com 11 dígitos (DDD + número com 9° digito).")

    #Solicitação do email 
    while True:
        email_adotante = input("E-mail: ")
        if "@" in email_adotante and "." in email_adotante:
            print("✅")
            break
        else:
            print("E-mail inválidado. Tente novamente!")

    #Solicitação dados de endereço
    print("\n📍 Dados de endereço\n")
    cidade_adotante = input("Cidade: ")
    bairro_adotante = input("Bairro: ")
    rua_adotante = input("Rua: ")
    numero_adotante = input("Número: ")

    #Especificação do animal que deseja
    print("🐶 Dados sobre a Adoção")
    animal_interesse_adotante = input("Qual o animal que tem interesse?: ")
    raça_interesse_adotante = input("Qual a raça da sua preferência?: ")
    sexo_interesse_adotante= input("Qual a sua preferência para o sexo?: ")
    porte_interesse = input("Qual o porte de sua preferência?: ")
    faixa_etaria_adotante = input("Qual a faixa etária da sua preferência: ")
    condicoes_interesse_adotante = input("Tem interesse em adotar animais com condições especiais(Deficiências, doenças crônicas, entre outros...?")
    
    #Se concorda com todos os termos 
    print("\n🔒 Termos e Consentimentos\n")
    termo_responsabilidade_adotante = input("Número: ")
    autorizacao_visita_adotante = input("Número: ")
    permissao_dados_adotante = input("Número: ")

    #Retorno dos dados fornecidos
    return {
        "nome": nome_adotante,
        "nascimento": nascimento_adotante,
        "cpf": cpf_adotante_formatado,
        "estado_civil": estado_civil_adotante,
        "telefone": telefone_adotante_formatado,
        "email": email_adotante,
        "endereco":{
            "cidade":cidade_adotante,
            "bairro":bairro_adotante,
            "rua":rua_adotante,
            "numero":numero_adotante
        },
        "preferencias_animal":{
            "animal": animal_interesse_adotante,
            "raca":raça_interesse_adotante,
            "sexo":sexo_interesse_adotante,
            "porte":porte_interesse,
            "faixa_etaria":faixa_etaria_adotante,
            "condicoes":condicoes_interesse_adotante
        },
        "termos":{
            "termo_reponsabilidade":termo_responsabilidade_adotante,
            "autorizacao":autorizacao_visita_adotante,
            "permissao":permissao_dados_adotante
        }
    }


# Definindo o caminho do arquivo no escopo global
arquivo = "adotantes.json"

#Função para salvar os dados pessoais dos adotantes
def salvar_dados_adotante(dados_adotante):
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as f:
            json.dump([], f, indent=4)
    with open(arquivo, 'r') as f:
        adotantes = json.load(f)
        
    adotantes.append(dados_adotante)
        
    with open(arquivo, 'w') as f:
        json.dump(adotantes, f, indent=4)

#Chama a função principal dados_pessoais_adotante
# adotante = dados_pessoais_adotante()
# print(adotante)  
# #Salva os dados no arquivo json
# salvar_dados_adotante(adotante)

#Função para ler todos adotantes no arquivo json
def listar_adotantes():
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            usuarios_adotantes = json.load(f)

        if usuarios_adotantes:
            print("=" * 50)
            print("Lista de Adotantes:")
            print("=" * 50)
            for adotante in usuarios_adotantes:
                print("*" * 50)
                print(f"Nome: {adotante['nome']}")
                print(f"Nascimento: {adotante['nascimento']}")
                print(f"Telefone: {adotante['telefone']}")
                print(f"E-mail: {adotante['email']}")
                print(f"Cidade: {adotante['endereco']['cidade']}")
                print(f"Interesse: {adotante['preferencias_animal']['animal']} ({adotante['preferencias_animal']['raca']})")
                print("*" * 50)
        else:
            print("Nenhum adotante cadastrado.")
    else:
        print("Arquivo de adotantes não encontrado.")

#Chama a função que lista os adotantes salvos no arquivo JSON
# listar_adotantes()


#Função para atualizar os dados do adotante
def atualizar_adotante():
    #Verifica se o arquivo existe
    if not os.path.exists(arquivo):
        print("Arquivo de adotantes não encontrado.")
        return

    with open(arquivo, 'r') as f:
        adotantes = json.load(f)

    #Digitando o cpf do adotante quer deseja atualizar os dados
    cpf_input = input("Digite o cpf completo do adotante que deseja atualizar:(XXX.XXX.XXX-XX)")

    encontrado = False
    #Menu para escolher o que deseja atualizar
    for adotante in adotantes:
        if adotante['cpf'] == cpf_input:
            print("\n🔄 Adotante encontrado.")
            print("O que deseja atualizar: ")
            print("\n 1-Nome")
            print("\n 2-Data de nascimento")
            print("\n 3-Telefone")
            print("\n 4-Email")
            print("\n 5-Endereço")
            print("\n 6-Interesse")
            opcao = input("\nDigite que deseja: ").strip()
            
            #Selecionando a opção 1 irá pedir para digitar um novo nome sobrescrevendo o atual
            if opcao == "1":
                novo_nome = input(f"Novo nome (pressione Enter para manter '{adotante['nome']}'): ")
                if novo_nome.strip():
                    adotante['nome'] = novo_nome

            #Selecionando a opção 2 irá pedir para digitar uma nova data de nascimento sobrescrevendo o atual
            if opcao == "2":
                nova_data = input(f"Nova data de nascimento (atual: {adotante['nascimento']}) [DD/MM/AAAA]: ")
                if nova_data.strip():
                    from datetime import datetime
                    try:
                        nascimento_formatado = datetime.strptime(nova_data, "%d/%m/%Y")
                        if (datetime.now() - nascimento_formatado).days / 365 >= 18:
                            adotante['nascimento'] = nova_data
                        else:
                            print("⚠️ Usuário precisa ter pelo menos 18 anos. Data não atualizada.")
                    except ValueError:
                        print("⚠️ Formato de data inválido. Data não atualizada.")

            #Selecionando a opção 3 irá pedir para digitar um novo telefone sobrescrevendo o atual
            if opcao == "3":
                novo_telefone = input(f"Novo telefone (atual: {adotante['telefone']}): ")
                if novo_telefone.strip():
                    telefone_numeros = ''.join(filter(str.isdigit, novo_telefone))
                    if len(telefone_numeros) == 11:
                        adotante['telefone'] = f"({telefone_numeros[:2]}) {telefone_numeros[2:7]}-{telefone_numeros[7:]}"
                    else:
                        print("⚠️ Telefone inválido. Deve conter 11 dígitos.")

            #Selecionando a opção 3 irá pedir para digitar um novo email sobrescrevendo o atual
            if opcao== "4":
                novo_email = input(f"Novo e-mail (atual: {adotante['email']}): ")
                if novo_email.strip() and "@" in novo_email and "." in novo_email:
                    adotante['email'] = novo_email
                elif novo_email.strip():
                    print("⚠️ E-mail inválido. E-mail não atualizado.")


            encontrado = True
            break

    if encontrado:
        with open(arquivo, 'w') as f:
            json.dump(adotantes, f, indent=4, ensure_ascii=False)
        print("\n✅ Adotante atualizado com sucesso!")
    else:
        print("❌ Adotante não encontrado.")
        
atualizar_adotante()