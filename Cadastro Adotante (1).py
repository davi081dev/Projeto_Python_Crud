def mostrar_mensagem_bem_vindo_cadastro_adotante():
    print("🐾 Bem-vindo(a) ao seu novo começo cheio de amor!\n")
    print("\nEstamos muito felizes por você estar aqui! Ao adotar, você não só ganha um amigo leal, mas também dá a um animal a chance de uma vida digna e cheia de carinho.")
    print("\nPara começarmos essa jornada, precisamos de algumas informações sobre você. O cadastro é rápido e seguro, e cada detalhe nos ajuda a garantir a melhor adoção possível.")
    print("\nPreencha os campos abaixo com seus dados – em breve, você estará mais perto de encontrar seu companheiro perfeito!")

print("\n📌 Dados Pessoais\n")

#Solicitação do nome Completo
def coleta_nome_adotante():
    while True:
        nome_adotante = input("Nome completo: ")
        if all(caractere.isalpha() or caractere.isspace() for caractere in nome_adotante):
            nome_adotante = nome_adotante.title()
            print("✅")
            break
        else:
            print("Use apenas letras e espaços. Tente novamente.")

#Solicitação da data de nascimento
def coleta_data_nascimento_adotante():
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
def coleta_cpf_adotante():
    while True:
        cpf_adotante_entrada = input("Cpf (XXX.XXX.XXX-XX): ")
        cpf_adotante = ''.join(filter(str.isdigit,cpf_adotante_entrada))

        if len(cpf_adotante_entrada) == 11:
            cpf_adotante_formatado = f"{cpf_adotante_entrada[:3]}.{cpf_adotante_entrada[4:6]}.{cpf_adotante_entrada[7:9]}-{cpf_adotante_entrada[10:11]}"
            print("✅")
            break
        else:
            print("Formato inválido! Siga o modelo: XXX.XXX.XXX-XX")

#Solicitação de Estado Civil
def coleta_estado_civil_adotante():
    while True:
        try:
            possibilidade_estado_civil = ["Solteiro(a)","Casado(a)","Divorciado(a)","Viúvo(a)","Separado(a)"]

            print("Estado Civil:\n1-Solteiro(a)\n2-Casado(a)\n3-Divorciado(a)\n4-Viúvo(a)\n5-Separado(a)")
            estado_civil_adotante_entrada = int(input("Escolha Seu estado civil: "))
            if estado_civil_adotante_entrada >= 1 <= len(possibilidade_estado_civil):
                estado_civil_adotante_formatado = possibilidade_estado_civil[estado_civil_adotante_entrada - 1]
                print("✅ Você selecionou:", estado_civil_adotante_formatado)
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Digite apenas números!")

print("\n📞 Dados de Contato\n")

#Solicitação do número de telefone
def coleta_telefone_adotante():
    while True:
        telefone_adotante_entrada = (input("Telefone: "))
        telefone_adotante = ''.join(filter(str.isdigit,telefone_adotante_entrada))

        if len(telefone_adotante) == 11:
            telefone_adotante_formatado = f"({telefone_adotante[:2]}) {telefone_adotante[2:7]}-{telefone_adotante[7:]}"
            print("✅")
            break
        else:
            print("Número inválido! Digite um telefone com 11 dígitos (DDD + número com 9° digito).")

#Solicitação do Email
def coleta_email_adotante():
    while True:
        email_adotante = input("E-mail: ")
        if '@'in email_adotante and '.' in email_adotante and email_adotante.count('@') == 1:
            print("✅")
            break
        else:
            print("E-mail inválido! Digite no formato: nome@provedor.com")

print("\n📍 Dados de endereço\n")

#Solicitação da cidade
def coleta_cidade_adotante():
    while True:
        cidade_adotante = input("Cidade: ")
        if all(caractere.isalpha() or caractere.isspace() for caractere in cidade_adotante):
            cidade_adotante = cidade_adotante.title()
            print("✅")
            break
        else:
            print("Use apenas letras e espaços. Tente novamente.")

#Solicitação bairro
def coleta_bairro_adotante():
    while True:
        bairro_adotante = input("Bairro:")
        if all(caractere.isalpha() or caractere.isspace() for caractere in bairro_adotante):
            bairro_adotante = bairro_adotante.title()
            print("✅")
            break
        else:
            print("Use apenas letras e espaços. Tente novamente.")

#Solicitação rua
def coleta_rua_adotante():
    while True:
        rua_adotante = input("Rua:")
        if all(caractere.isalpha() or caractere.isspace() for caractere in rua_adotante):
            rua_adotante = rua_adotante.title()
            print("✅")
            break
        else:
            print("Use apenas letras e espaços. Tente novamente.")

#Solicitação número residêncial
def coleta_numero_casa_adotante():
    while True:
            numero_adotante_entrada = input("Número: ")
            numero_adotante = ''.join(filter(str.isdigit,numero_adotante_entrada))
            print("✅")
            break

print("🐶 Dados sobre a Adoção")

animal_interesse_adotante = input("Qual o animal que tem interesse?: ")
raça_interesse_adotante = input("Qual a raça da sua preferência?: ")
sexo_interesse_adotante= input("Qual a sua preferência para o sexo?: ")
porte_interesse = input("Qual o porte de sua preferência?: ")
faixa_etaria_adotante = input("Qual a faixa etária da sua preferência: ")
condicoes_interesse_adotante = input("Tem interesse em adotar animais com condições especiais(Deficiências, doenças crônicas, entre outros...?")

print("\n🔒 Termos e Consentimentos\n")

#Solicitação do Termo de responsabilidade
def coleta_termo_responsabilidade_adotante():
    while True:
        print("Aceita o Termo de responsabilidade?:\n1-Sim\n2-não")
        termo_responsabilidade_adotante = int(input(": "))
        if termo_responsabilidade_adotante == 1:
            print("✅")
            break
        else:
            print("É necessário aceitar o Termo de responsabilidade Para continuar.")

#Solicitação da Permissão de uso de dados
def coleta_permissao_uso_dados_adotante():
    while True:
        print("Permissão para uso de dados?:\n1-Sim\n2-não")
        permissao_dados_adotante = int(input(": "))
        if permissao_dados_adotante == 1:
            print("✅")
            break
        else:
            print("É necessário permitir a utilização dos dados coletados para continuar.")

#Solicitação da Autorização de visita
def coleta_Autorizaçao_visita():
    while True:
        print("Autorização para visita pós-adoção?:\n1-Sim\n2-não")
        autorizacao_visita_adotante = int(input(": "))
        if autorizacao_visita_adotante == 1:
            print("✅")
            break
        else:
            print("É necessário aceitar o Termo de responsabilidade Para continuar.")
