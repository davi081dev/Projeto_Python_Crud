import json
import os
import crudAnimal
import crudCuidador
import crudAdotante
import algoritmoAdotar
from time import sleep  

def menu_inicial_da_escolha_do_crud():
    print("\nEscolha o que deseja fazer: ")
    print("1. Menu animal")
    print("2. Menu cuidador")
    print("3. Menu adotante")
    print("4. Adoção")
    print("5. Encerrar o programa\n")
    sleep(1)

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
                algoritmoAdotar.menu_adocao()
            case 5:
                print("Encerrando...")
                sleep(2)
                break

if __name__ == "__main__":
    main()