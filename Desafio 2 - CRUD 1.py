# Import = bibliotecas/módulos

import time # Usei para adicionar o delay em algumas partes "time.sleep(tempo de delay)""
import sys # Usei para simplificar a saída do sistema "sys.exit()"

def linha():
    print("-" * 60)

def add():
    while True:
        add1 = input("\n❔ Deseja algo mais?\n1️⃣  Sim\n2️⃣  Não\n")
        if add1 == "1":
            time.sleep(1)
            return
        elif add1 == "2":
            end()
            time.sleep(1)
            sys.exit()
        else:
            invalid()
        
def end():
    time.sleep(1)
    print("👋 Saindo...")
    time.sleep(1)
    print("🫂  Obrigado!")
    time.sleep(1)
    print("🐶 Au au!")
    time.sleep(1)
    
def invalid():
    linha()
    print("❌ OPÇÃO INVÁLIDA! ❌")
    linha()
    time.sleep(0.5)
    print("🔃 Vamos tentar novamente?")
    time.sleep(0.5)

def ask_geral(sim_nao): # Criei uma função geral porque são etapas repetitivas.
    while True:
        resp1 = input(sim_nao).strip().lower() # A função ".strip()" remove os espaços em branco
        if resp1 == "sim":
            input ("❓ Qual? ")
            break    
        elif resp1 == "não" or resp1 == "nao":
            break
        else:
            invalid()

def ask_foto(foto): # Tive que criar uma outra função só pra parte da foto porque é uma condicional única.
    while True:
        resp2 = input(foto).strip().lower()
        if resp2 == "sim":
            print("\n🤳 Insira a foto:") # Vai ser necessário anexar uma foto?
            time.sleep(1)
            print("\n⬆️  Uploading...")
            time.sleep(1)
            print("\n✅ Informações recebidas. Cadastro finalizado.")
            linha()
            time.sleep(0.5)
            break    
        elif resp2 == "não" or resp2 == "nao":
            time.sleep(1)
            print("\n✅ Informações recebidas. Cadastro finalizado.")
            time.sleep(0.5)
            linha()
            break
        else:
            invalid()

def not_found(): # Enquanto as outras opções do código e a integração com o json não ficam prontas, redirecionei pra essa função
    time.sleep(1)
    print("🔍  Buscando...")
    time.sleep(1)
    print("😂  Te enganei!")
    time.sleep(1)
    print("🚧  Desculpe. Essa parte do código ainda não tá pronta.")
    time.sleep(1)
    add()

def info():
    while True:
        info = input("\n❓ Deseja adicionar alguma informação complementar?\n1️⃣  Sim\n2️⃣  Não\n")
        if info == "1":
            input("\nℹ️  Insira a informação: ")
            time.sleep(1)
            print("\n✌️  Obrigado pelas informações. Nossa equipe irá até o local em instantes.")
            add()
            return
        elif info == "2":
            time.sleep(1)
            print("\n✌️  Obrigado pelas informações. Nossa equipe irá até o local em instantes.")
            add()
            return
        else:
            invalid()

def menu_crud1():
    while True:
        print("\n🔢 Informe o número correspondente à opção que deseja: 👇")
        print("1️⃣  Cadastrar animal")
        print("2️⃣  Localizar dados de um animal")
        print("3️⃣  Atualizar o cadastro de um animal")
        print("4️⃣  Excluir um animal")
        print("5️⃣  Solicitar um resgate")
        print("0️⃣  Voltar ao menu anterior") # Ainda não integramos todos os CRUDs, então a opção 0 encerra o código.
        
        opcao = int(input("☝️  Escolha uma das opções acima: "))
        match opcao:

            case 1:
                input("\n📛 Qual o nome do bichinho? ")
                input("\n🤔 Qual a espécie do bichinho? (ex.: gato, cachorro, hamster...) ")
                input("\n🔢 Qual a idade estimada do bichinho? ")
                enf = ask_geral("\n😷 Ele possui algum tipo de enfermidade? ")
                add_info = ask_geral("\n➕ Deseja inserir mais alguma informação adicional? ") 
                foto = ask_foto("\n📸 Deseja inserir alguma foto do animal? ")              
                add()

            case 2:
                input("\n📛 Informe o nome do animal que deseja localizar: ")
                not_found()

            case 3:
                input("\n📛 Informe o nome do animal que deseja atualizar: ")
                time.sleep(1)
                not_found()

            case 4:
                input("\n📛 Informe o nome do animal que deseja excluir: ")
                not_found()
        
            case 5:
                time.sleep(1)
                print("\n🚨 Vamos iniciar a solicitação de resgate.\n")
                time.sleep(1)
                input("📌 Informe o endereço da ocorrência: ")
                tel = input("\n📞 Informe um telefone para contato: ")
                info()
                        
            case 0:
                end()
                break

            case __:
                invalid()

linha()
print("🐾 Olá! Bem-vindo ao Centro de Adoção Luísa Mel! 🐾")
linha()
time.sleep(0.5)
menu_crud1()
