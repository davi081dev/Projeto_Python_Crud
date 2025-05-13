# CRUD: Create, Read, Update and Delete
# Não esquecer de utilizar o arquivo .json

def main():

    def invalid():
        print("-"*60)
        print("OPÇÃO INVÁLIDA!")
        print("-"*60)
        main()

    def add():
        print("Deseja algo mais?")
        add=int(input("\n1 - Sim \n2 - Não\n"))
        match add:
            case 1:
                main()
            case 2:
                print("Obrigado!")

    def linha():
        print('-'*60)


    print("-"*60)
    print("Olá! Bem-vindo ao Centro de Adoção Luísa Mel! O que você deseja?" )
    print("-"*60)
    print("1 - Adicionar um novo animal;")
    print("2 - Localizar dados de um animal;")
    print("3 - Atualizar o cadastro de um animal;")
    print("4 - Excluir um animal;")
    print("5 - Solicitar um resgate.")
    opcao = int(input("Escolha uma das opções acima: "))

    match opcao:
        case 1:
           str(input("Qual a espécie do animal? (ex.: gato, cachorro, hamster...) "))
           str(input("Qual a raça do animal? "))
           str(input("Qual a idade estimada do animal? "))
           str(input("O animal possui algum tipo de enfermidade? "))
           str(input("O animal possui algum tipo de doença perceptível? "))
           str(input("Deseja inserir mais alguma informação adicional? "))
           foto=str(input("Deseja inserir alguma foto do animal? "))
           if foto=='Sim':
              input("Insira a foto: ")
              linha()
              print("Uploading...")
              linha()
              print("Cadastro finalizado.")
              add()
           else:
              print("Cadastro finalizado.")
              add()


        case 2:
            input("Informe o nome do animal que deseja localizar: ")
            print("EM CONSTRUÇÃO")

        case 3:
            input("Informe o nome do animal que deseja atualizar: ")
            print("EM CONSTRUÇÃO")

        case 4:
            input("Informe o nome do animal que deseja excluir: ")
            print("EM CONSTRUÇÃO")

        case 5:
            input("Informe o endereço da ocorrência: ")
            print("EM CONSTRUÇÃO")

        case __:
            invalid()


main()