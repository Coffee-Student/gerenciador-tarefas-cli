tarefas = []

# Menu Principal


def exibir_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Sair")
    return input("Escolha uma opção: ")


def principal():
    # Funcionamento do Menu Principal
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            print("Você escolheu Adicionar Tarefa.")

        elif opcao == '2':
            print("Você escolheu Listar Tarefas.")

        elif opcao == '3':
            print("Saindo do gerenciador de tarefas...!")
            break

        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


# Ponto de entrada do programa: garante que 'principal()' rode ao executar o arquivo.
if __name__ == "__main__":
    principal()
