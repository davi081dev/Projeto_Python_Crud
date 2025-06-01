import time
import sys
import json
import os

ARQUIVO = 'animal.json'

def linha():
    print("-" * 60)

def add():
    while True:
        add1 = input("\n❔ Deseja algo mais?\n1️⃣  Sim\n2️⃣  Não\n")
        if add1 == "1":
            time.sleep(0.5)
            return
        elif add1 == "2":
            time.sleep(1)
            end()   
        else:
            invalid()

def invalid():
    print("🤭 Oops... Não localizei a opção informada.")
    time.sleep(0.5)
    print("🔃 Vamos tentar novamente?")
    time.sleep(0.5)

def end():
    time.sleep(1)
    print("👋 Saindo...")
    time.sleep(1)
    print("🫂  Obrigado!")
    time.sleep(1)
    print("🐶 Au au!")
    time.sleep(1)
    sys.exit()

def carregar_animais():
    if not os.path.exists(ARQUIVO):
        return []
    try:
        with open(ARQUIVO, 'r') as f:
            conteudo = f.read()
            if not conteudo:
                return []
            return json.loads(conteudo)
    except json.JSONDecodeError:
        print("⚠️ ERRO! O arquivo JSON está corrompido ou mal formatado.")
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
    print(f"\n✅ O cadastro de {nome} foi criado com sucesso!")
    add()

def listar_animais():
    tentativas = 0
    while tentativas < 3:
        time.sleep(0.5)
        senha = input("🔑 Informe a senha do administrador: ").lower()
        if senha == "cachorrinho":
            animais = carregar_animais()
            time.sleep(0.5)
            print("🧠 Buscando dados")
            time.sleep(0.5)
            if not animais:
                print("❕ Nenhum animal cadastrado.")
                add()
            else:
                print("👇 Estes são os animais cadastrados até o momento:")
                for animal in animais:
                    time.sleep(0.5)
                    linha()
                    print(f"ID: {animal['id']} | Nome: {animal['nome']} | Espécie: {animal['especie']} | Idade: {animal['idade']}")
                    linha()
                add()
            return
        else:
            tentativas += 1
            time.sleep(0.5)
            print(f"❌ Senha incorreta. Tentativa {tentativas}/3.\n")
    print("🚫 Número máximo de tentativas excedido. Você será desconectado do sistema.\n")
    end()


def buscar_animal():
    nome_input = input("📛 Informe o nome do animal que deseja localizar: ").upper()
    animais = carregar_animais()
    encontrados = [a for a in animais if a['nome'] == nome_input]
    while True:
        if not encontrados:
            try:
                again = int(input("❌ Animal não encontrado. Deseja tentar novamente?\n1️⃣  Sim\n2️⃣  Não\n"))
                match again:
                    case 1:
                        buscar_animal()
                        break
                    case 2:
                        add()
                        break
                    case _:
                        invalid()
            except ValueError:
                invalid()
                continue
                
        if len(encontrados) == 1:
            animal = encontrados[0]
            time.sleep(0.5)
            linha()
            print(f"ID: {animal['id']} | Nome: {animal['nome']} | Espécie: {animal['especie']} | Idade: {animal['idade']}")
            add()
        else:
            print(f"⚠️  Foram encontrados {len(encontrados)} animais com o nome '{nome_input}':")
            for a in encontrados:
                time.sleep(0.5)
                linha()
                print(f"🔹 ID: {a['id']} | Espécie: {a['especie']} | Idade: {a['idade']}")
            add()
        break

def deletar_animal():
    try:
        id_delete = int(input("🔍 Informe o ID do animal que deseja excluir: "))
    except ValueError:
        invalid()

    animais = carregar_animais()
    animal = next((a for a in animais if a['id'] == int(id_delete)), None)

    if not animal:
        print("🧠 Buscando dados")
        time.sleep(0.5)
        print("❌ Animal não encontrado na base de dados.")
        time.sleep(0.5)
        try:
            again = int(input("\n🔃 Quer tentar novamente?\n1️⃣  Sim\n2️⃣  Não\n"))
            match again:
                case 1:
                    deletar_animal()
                case 2:
                    add()
        except ValueError:
            invalid()
    else:
            print("🧠 Buscando dados")
            time.sleep(0.5)
            print("🐾 Animal localizado")
            time.sleep(0.5)
            linha()
            print(f"ID: {animal['id']} | Nome: {animal['nome']} | Espécie: {animal['especie']} | Idade: {animal['idade']}")
            linha()
            try:
                confirm = int(input("🤔 Deseja prosseguir com a exclusão dos dados acima?\n1️⃣  Sim\n2️⃣  Não: "))
                match confirm:
                    case 1:
                        animais = [a for a in animais if a['id'] != id_delete]
                        time.sleep(0.5)
                        print("\n🗑️ Deletando...")
                        time.sleep(0.5)
                        salvar_animais(animais)
                        print(f"\n✅ Cadastro nº {id_delete} excluído com sucesso.\n")
                        time.sleep(0.5)
                        add()
                    case 2:
                        print("❌ Exclusão cancelada.")
                        add()
            except ValueError:
                invalid()

def atualizar_animal():
    try:
        id_atualizar = int(input("\n🔍 Informe a ID do animal que deseja atualizar: "))
    except ValueError:
        time.sleep(0.5)
        invalid()
    animais = carregar_animais()
    encontrados = [a for a in animais if a['id'] == id_atualizar]
    if not encontrados:
        print("❌ Animal não encontrado.")
        try:
            again = int(input("\n🔃 Quer tentar novamente?\n1️⃣  Sim\n2️⃣  Não\n"))
            match again:
                case 1:
                    atualizar_animal()
                case 2:
                    add()
        except ValueError
            invalid()

    if len(encontrados) > 1:
        print("⚠️  Existe mais de um animal com esse nome:")
    else:
        animal = encontrados[0]
        for a in encontrados:
            print("🧠 Buscando dados")
            time.sleep(0.5)
            print("🐾 Animal localizado")
            time.sleep(0.5)
            linha()
            print(f"🔹 ID: {a['id']} | Nome: {a['nome']} | Espécie: {a['especie']} | Idade: {a['idade']}")
            linha()
    try:
        confirm = int(input("❓ Deseja atualizar o cadastro acima?\n1️⃣  Sim\n2️⃣  Não "))
        match confirm:
            case 1:
                nome_atual = input("\n✏️  Informe o nome: ").upper()
                especie_atual = input("✏️  Informe a espécie: ").upper()
                idade_atual = input("✏️  Informe a idade: ")
            case 2:
                print("❌ Atualização cancelada.")
                add()
    except ValueError:
        invalid()
    try:
            confirm = int(input("\n🤔 Confirma a atualização?\n1️⃣  Sim\n2️⃣  Não\n"))
            match confirm:
                case 1:
                    if not nome_atual or not especie_atual or not idade_atual:
                        print("❌ Todos os campos devem ser preenchidos.")
                        return
                    animal['nome'] = nome_atual
                    animal['especie'] = especie_atual
                    animal['idade'] = idade_atual
                    salvar_animais(animais)
                    linha()
                    print("✅ Cadastro atualizado com sucesso!")
                    linha()
                    add()
                case 2:
                    print("❌ Atualização cancelada.")
                    add()
    except ValueError:
        invalid()

def ask_geral(sim_nao):
    while True:
        resp1 = input(sim_nao).strip().lower()
        if resp1 == "sim":
            input("❓ Qual? ")
            break
        elif resp1 in ("não", "nao"):
            break
        else:
            invalid()

def ask_foto(foto):
    while True:
        resp2 = input(foto).strip().lower()
        if resp2 == "sim":
            print("🤳 Insira a foto:")
            time.sleep(1)
            linha()
            print("⬆️  Uploading...")
            linha()
            time.sleep(1)
            break
        elif resp2 in ("não", "nao"):
            time.sleep(1)
            break
        else:
            invalid()

def info():
    while True:
        info_add = input("\n❓ Deseja adicionar alguma informação complementar?\n1️⃣  Sim\n2️⃣  Não\n")
        if info_add == "1":
            input("\nℹ️  Insira a informação: ")
            time.sleep(1)
            print("✌️  Obrigado pelas informações. Nossa equipe irá até o local em instantes.")
            add()
            return
        elif info_add == "2":
            time.sleep(1)
            print("✌️  Obrigado pelas informações. Nossa equipe irá até o local em instantes.")
            add()
            return
        else:
            invalid()

def menu_crud1():
    while True:
        print("\n1️⃣  Cadastrar animal") #OK
        print("2️⃣  Localizar animal") #OK
        print("3️⃣  Atualizar o cadastro de um animal") #OK
        print("4️⃣  Excluir um animal") #OK
        print("5️⃣  Listar animais cadastrados") #OK
        print("6️⃣  Solicitar um resgate") # OK
        print("7️⃣  Sair")

        try:
            opcao = int(input("☝️  Escolha uma das opções acima: "))
        except ValueError:
            invalid()
            continue

        match opcao:
            case 1:
                time.sleep(0.5)
                nome = input("\n📛 Qual o nome do bichinho? ").upper()
                especie = input("🤔 Qual a espécie do bichinho? (ex.: gato, cachorro, hamster...) ").upper()
                idade = input("🔢 Qual a idade estimada do bichinho? ")
                ask_geral("😷 Ele possui algum tipo de enfermidade? ")
                ask_geral("➕ Deseja inserir mais alguma informação adicional? ")
                ask_foto("📸 Deseja inserir alguma foto do animal? ")
                criar_animal(nome, especie, idade)
            case 2:
                buscar_animal()
            case 3:
                atualizar_animal()
            case 4:
                deletar_animal()
            case 5:
                listar_animais()
            case 6:
                time.sleep(0.5)
                print("\n🚨 Vamos iniciar a solicitação de resgate.")
                time.sleep(0.5)
                input("\n📌 Informe o endereço da ocorrência: ")
                while True:
                    tel = input("📞 Informe um telefone para contato com DDD: ").strip()
                    if tel.isdigit() and len(tel) in [10, 11]:
                        break
                    else:
                        invalid()
                info()
            case 7:
                end()
                break
            case _:
                invalid()

linha()
print("🐾 Olá! Bem-vindo ao Centro de Adoção Luísa Mel! 🐾")
linha()
time.sleep(0.5)
print("🔢 Informe o número correspondente à opção que deseja: 👇")
menu_crud1()
