tarefas = []

# Lógica da nova tarefa
def adicionar_tarefa():
    nova_tarefa = input("Digite a descrição da nova tarefa: ")
    
    # Verificação da Lógica
    if nova_tarefa.strip():
        tarefas.append(nova_tarefa.strip())
        print(f"\nTarefa '{nova_tarefa.strip()}' adicionada com sucesso!")
    else:
        print("\nPreencha a descrição da tarefa, por favor.")
    
# Exibir Menu Principal
def exibir_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Sair")
    return input("Escolha uma opção: ")

# Lógica do Menu Principal
def opcao_escolhida():
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            adicionar_tarefa()

        elif opcao == '2':
            print("Você escolheu Listar Tarefas.")

        elif opcao == '3':
            print("Saindo do gerenciador de tarefas...!")
            break

        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


if __name__ == "__main__":
    opcao_escolhida()
