import json
import os
import crudAnimal
import crudCuidador
import crudAdotante
from time import sleep

def adotar():
    print("Adotando...")

def menu_inicial_da_escolha_do_crud():
    print("Escolha o que deseja fazer: ")
    print("1. Menu animal")
    print("2. Menu cuidador")
    print("3. Menu adotante")
    print("4. Encontrar um pet")
    print("5. Encerrar o programa")
    sleep(1)

def crud_cpf_animal():
    print("\nCrud CPF Animal\n")
    sleep(2)

def crud_cpf_cuidador():
    print("\nCrud CPF Cuidador\n")
    sleep(2)

def crud_cpf_adotante():
    print("\nCrud CPF Adotante\n")
    sleep(2)

def main ():
    while True:
        menu_inicial_da_escolha_do_crud()
        opcao_inicial = int(input("Opção do crud: "))
        sleep(1)

        match (opcao_inicial):
            case 1:
                crudAnimal.crud_cpf_animal()
            case 2:
                crudCuidador.crud_cpf_cuidador()
            case 3:
                crudAdotante.crud_cpf_adotante()
            case 4:
                adotar()
            case 5:
                print("Encerrando...")
                sleep(2)
                break

if __name__ == "__main__":
    main()