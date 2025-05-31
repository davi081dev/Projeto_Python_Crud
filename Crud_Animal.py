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


//

import json
import os

ARQUIVO = 'animais.json'

def carregar_animais():
    if not os.path.exists(ARQUIVO):
        return []
    try:
        with open(ARQUIVO, 'r') as f:
            conteudo = f.read().strip()
            if not conteudo:
                return []  
            return json.loads(conteudo)
    except json.JSONDecodeError:
        print("⚠️ Erro: O arquivo JSON está corrompido ou mal formatado.")
        return []

def salvar_animais(animais):
    with open(ARQUIVO, 'w') as f:
        json.dump(animais, f, indent=2)

def criar_animal(nome, especie, idade):
    animais = carregar_animais()
    novo_id = 1 if not animais else animais[-1]['id'] + 1
    novo_animal = {
        "id": novo_id,
        "nome": nome,
        "especie": especie,
        "idade": idade
    }
    animais.append(novo_animal)
    salvar_animais(animais)
    print(f"Animal '{nome}' cadastrado com sucesso!")

def listar_animais():
    animais = carregar_animais()
    if not animais:
        print("Nenhum animal cadastrado.")
    else:
        for animal in animais:
            print(f"ID: {animal['id']} | Nome: {animal['nome']} | Espécie: {animal['especie']} | Idade: {animal['idade']} anos")

def atualizar_animal(id, nome=None, especie=None, idade=None):
    animais = carregar_animais()
    for animal in animais:
        if animal['id'] == id:
            if nome: animal['nome'] = nome
            if especie: animal['especie'] = especie
            if idade is not None: animal['idade'] = idade
            salvar_animais(animais)
            print(f"Animal ID {id} atualizado com sucesso!")
            return
    print("Animal não encontrado.")

def deletar_animal(id):
    animais = carregar_animais()
    novos_animais = [a for a in animais if a['id'] != id]
    if len(animais) == len(novos_animais):
        print("Animal não encontrado.")
        return
    salvar_animais(novos_animais)
    print(f"Animal ID {id} removido com sucesso.")

def buscar_animal(id):
    animais = carregar_animais()
    for animal in animais:
        if animal['id'] == id:
            print(f"ID: {animal['id']} | Nome: {animal['nome']} | Espécie: {animal['especie']} | Idade: {animal['idade']} anos")
            return
    print("Animal não encontrado.")



def menu():
    while True:
        print("\n=== Clínica de Adoção ===")
        print("1. Listar animais")
        print("2. Cadastrar novo animal")
        print("3. Atualizar animal")
        print("4. Remover animal")
        print("5. Buscar animal")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_animais()
        elif opcao == '2':
            nome = input("Nome: ")
            especie = input("Espécie: ")
            idade = int(input("Idade: "))
            criar_animal(nome, especie, idade)
        elif opcao == '3':
            id = int(input("ID do animal a atualizar: "))
            nome = input("Novo nome (ou Enter para manter): ")
            especie = input("Nova espécie (ou Enter para manter): ")
            idade_str = input("Nova idade (ou Enter para manter): ")
            idade = int(idade_str) if idade_str else None
            atualizar_animal(id, nome or None, especie or None, idade)
        elif opcao == '4':
            id = int(input("ID do animal a remover: "))
            deletar_animal(id)
        elif opcao == '5':
            id = int(input("ID do animal a buscar: "))
            buscar_animal(id)

        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()

