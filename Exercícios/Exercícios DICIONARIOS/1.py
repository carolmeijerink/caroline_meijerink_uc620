alunos = []

while True:
    print("\n--- Menu Acadêmico ---")
    print("1 - Inserir Aluno")
    print("2 - Listar Alunos")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_aluno = {
            "nome": input("Nome: "),
            "idade": input("Idade: "),
            "curso": input("Curso: ")
        }

        alunos.append(novo_aluno)
        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        if not alunos:
            print("\nNenhum aluno cadastrado.")
        
        else:
            print("\n--- Listagem de Alunos ---")
            
            for aluno in alunos:
                print(f"nome: {aluno['nome']}")
                print(f"idade: {aluno['idade']}")
                print(f"curso: {aluno['curso']}")
                print("-" * 20)

    elif opcao == "0":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida!")