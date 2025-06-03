import json
from time import sleep

with open("animal.json", "r", encoding="utf-8") as f:
    animais = json.load(f)

with open("adotantes.json", "r", encoding="utf-8") as f:
    adotantes = json.load(f)

def voltar_menu():
    print("Voltando ao menu anterior")
    sleep(0.5)

def encontrar_match(adotante, animais):
    for animal in animais:
        if (adotante["Animal de interesse"].lower() == animal["especie"].lower() and
            adotante["Raca de interesse"].lower() == animal["raca"].lower() and
            adotante["Faixa etaria de interesse"] == animal["idade"] and
            adotante["Condicoes de interesse"].lower() == "sim"):
            return animal
    return None

def menu_adocao():
    cpf_adotante = input("Digite o CPF de um adotante cadastrado: ")
    adotante = adotantes.get(cpf_adotante, {})

    if adotante:
        match = encontrar_match(adotante, animais)
        if match:
            print(f"🎉 {adotante['Nome']} pode adotar {match['nome']}!")
            voltar_menu()
        else:
            print("Que pena! Nenhum animal compatível encontrado.")
            voltar_menu()
    else:
        print("Adotante não encontrado.")
        voltar_menu()