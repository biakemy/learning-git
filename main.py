def cadastrar():
    pass

def listar():
    pass

def buscar():
    pass

def emprestar():
    pass

def devolver():
    pass

def main():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastro")
        print("2. Listagem")
        print("3. Busca")
        print("4. Empréstimo")
        print("5. Devolução")
        print("6. Sair")
        
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == '1':
            print("Entrando no cadastro...")
            cadastrar()
        elif opcao == '2':
            print("Entrando na listagem...")
            listar()
        elif opcao == '3':
            print("Entrando na busca...")
            buscar()
        elif opcao == '4':
            print("Entrando no empréstimo...")
            emprestar()
        elif opcao == '5':
            print("Entrando na devolução...")
            devolver()
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
    