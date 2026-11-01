import json
import os

ARQUIVO_JSON = 'acervo.json'
livros = []

def carregar_dados():
    global livros
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
            livros = json.load(f)

def salvar_dados():
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(livros, f, ensure_ascii=False, indent=4)

def cadastrar():
    print("\n--- Cadastro de Livro ---")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação: ")
    
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": "Sim" 
    }
    
    livros.append(livro)
    salvar_dados()
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def listar():
    print("\n--- Lista de Livros ---")
    if not livros:
        print("Nenhum livro cadastrado no acervo.")
        return
        
    for i, livro in enumerate(livros, 1):
        print(f"{i}. Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Disponível: {livro['disponivel']}")

def buscar():
    print("\n--- Busca de Livros ---")
    termo = input("Digite o título ou autor que deseja buscar: ").lower()
    encontrados = [livro for livro in livros if termo in livro['titulo'].lower() or termo in livro['autor'].lower()]
            
    if encontrados:
        print("\nLivros encontrados:")
        for i, livro in enumerate(encontrados, 1):
            print(f"{i}. Título: {livro['titulo']} | Autor: {livro['autor']} | Disponível: {livro['disponivel']}")
    else:
        print("\nNenhum livro encontrado com esse título ou autor.")

def emprestar():
    print("\n--- Empréstimo de Livro ---")
    titulo = input("Digite o título do livro que será emprestado: ").lower()
    
    for livro in livros:
        if titulo in livro['titulo'].lower():
            if livro['disponivel'] == "Sim":
                livro['disponivel'] = "Não"
                salvar_dados()
                print(f"Empréstimo do livro '{livro['titulo']}' realizado com sucesso!")
            else:
                print("Este livro já está emprestado no momento.")
            return
            
    print("Livro não encontrado no acervo.")

def devolver():
    print("\n--- Devolução de Livro ---")
    titulo = input("Digite o título do livro que está sendo devolvido: ").lower()
    
    for livro in livros:
        if titulo in livro['titulo'].lower():
            if livro['disponivel'] == "Não":
                livro['disponivel'] = "Sim"
                salvar_dados()
                print(f"Devolução do livro '{livro['titulo']}' registrada com sucesso!")
            else:
                print("Este livro já consta como disponível no acervo.")
            return
            
    print("Livro não encontrado no acervo.")

def remover():
    print("\n--- Remoção de Livro ---")
    titulo = input("Digite o título exato do livro que deseja remover: ")
    
    for livro in livros:
        if livro['titulo'].lower() == titulo.lower():
            livros.remove(livro)
            salvar_dados()
            print(f"Livro '{livro['titulo']}' removido do sistema.")
            return
            
    print("Livro não encontrado.")

def estatisticas():
    print("\n--- Estatísticas do Acervo ---")
    total = len(livros)
    disponiveis = sum(1 for livro in livros if livro['disponivel'] == "Sim")
    emprestados = total - disponiveis
    
    print(f"Total de livros cadastrados: {total}")
    print(f"Livros disponíveis: {disponiveis}")
    print(f"Livros emprestados: {emprestados}")

def main():
    carregar_dados() # Carrega o arquivo JSON logo ao abrir o programa
    
    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1. Cadastro")
        print("2. Listagem")
        print("3. Busca")
        print("4. Empréstimo")
        print("5. Devolução")
        print("6. Remover Livro")
        print("7. Estatísticas do Acervo")
        print("8. Sair")
        
        opcao = input("Escolha uma opção (1-8): ")
        
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            buscar()
        elif opcao == '4':
            emprestar()
        elif opcao == '5':
            devolver()
        elif opcao == '6':
            remover()
        elif opcao == '7':
            estatisticas()
        elif opcao == '8':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()