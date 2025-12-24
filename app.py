import db_manager
from db_manager import inicializar_bd
from tarefas_manager import adicionar_tarefa, listar_tarefas, remover_tarefa, modificar_tarefa

def exibir_menu():
    print("\n==========================")
    print("▒ Gerenciador de Tarefas ▒")
    print("==========================")
    print("──────────────────────────")
    print("1 → Adicionar Tarefa")
    print("2 → Listar Tarefas")
    print("3 → Remover Tarefa")
    print("4 → Atualizar Tarefa")
    print("5 → Sair")
    print("──────────────────────────")
    return input("Escolha uma opção: ")

# Lógica do Menu Principal
def principal():
    inicializar_bd()

    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            descricao = input("\nDigite a nova descrição da tarefa: ")
            if descricao.strip():
                adicionar_tarefa(descricao)
            else:
                print("\nA descrição não pode estar vazia.")
                print(".... → Operação Cancelada ← ....")

        elif opcao == '2':
            listar_tarefas()

        elif opcao == '3':
            listar_tarefas()
            try:
                id_remover = int(input("Digite o ID da tarefa que deseja remover: "))
               
                if remover_tarefa(id_remover):
                    print(f"\nTarefa removida com sucesso!")
                else:
                    print("\nID inválido. Por favor, digite o ID correto")
            
            except ValueError:
                print("\nEntrada inválida. Tente novamente.")

        elif opcao == '4':
            listar_tarefas()
            try:
                id_modificar = int(input("\nDigite a ID da tarefa que deseja alterar: "))
                nova_descricao = input("\nDigite a NOVA descrição para esta tarefa: ")

                if not nova_descricao.strip():
                    print("\nA descrição está vázia. Operação cancelada...\n")
                    continue

                if modificar_tarefa(id_modificar, nova_descricao):
                    print("\n... → Alteração feita com sucesso ← ...")
                    pass
                else:
                    print(f"Não foi possível modificar a tarefa ID {id_modificar}")
            
            except ValueError:
                print("\nID inválido. Digite o ID corretamente, por favor.\n")

            except Exception as e:
                print(f"z\nOcorreu um erro: {e}\n")

        elif opcao == '5':
            print("\nSaindo do Gerenciador de Tarefas...")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    principal()