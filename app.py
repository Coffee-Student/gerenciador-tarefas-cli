"""Projeto.: Gerenciador de Tarefas."""
import sqlite3
import os

"""Criação/Retorno a conexão com o banco de dados"""
def conectar_bd():
    conn = sqlite3.connect('tarefas.db')
    return conn

"""Criação da tabela 'tarefas' se ñ existir. """
def inicializar_bd():
    conn = conectar_bd()
    cursor = conn.cursor()

    # SQL → Criação da tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY, 
            descricao TEXT NOT NULL
            )
    """)
    conn.commit()
    conn.close()
    print("\n→ Sistema inicializado com sucesso! ← \n")

# Lógica da nova tarefa
def adicionar_tarefa():
    nova_tarefa = input("\nDigite a descrição da nova tarefa: ")
        
    # Verificação da Lógica
    if nova_tarefa.strip():
        conn = conectar_bd()
        cursor = conn.cursor()

        # SQL → INSERT INTO tabela (coluna) VALUES (placeholder)
        cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (nova_tarefa.strip(),))

        conn.commit() # 'tarefas.db' → Alterações salvas
        conn.close()

        print(f"\nTarefa '{nova_tarefa.strip()}' adicionada com sucesso!\n")
    else:
        print("\nPreencha a descrição da tarefa, por favor.")

# Lógica de Listar Tarefas
def listar_tarefas():
    conn = conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, descricao FROM tarefas")
    
    tarefas_bd = cursor.fetchall()

    if not tarefas_bd:
        print("\nNão há registro de tarefas...\n")
    else:
        print("\n=========================================")
        print("░ Tarefas Registradas no Banco de Dados ░")
        print("=========================================\n")
        for id, descricao in tarefas_bd:
            print(f"ID {id}: {descricao}")
        conn.close()

# Lógica de Remover Tarefas
def remover_tarefa():
    listar_tarefas() # Visualização das tarefas

    # Rotina de Indentificação de Erros
    try:
        id_remover = int(input("\nDigita ID da tarefa que deseja remover: "))

        conn = conectar_bd()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_remover,))

        if cursor.rowcount > 0: # Confirmação da exclusão.
            conn.commit()
            print("\nTarefa removida com sucesso!\n")
        else:
            print("\nOcorreu um erro. Tente novamente.\n")

        conn.close()

    except ValueError:
        print("\n Entrada inválida. Por favor, verifique o ID digitado.\n")

# Lógica de alteração de tarefas
def modificar_tarefa(id_tarefa, nova_descricao):
    conn = conectar_bd()
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE tarefas SET descricao = ? WHERE id = ?", (nova_descricao, id_tarefa))
        conn.commit()
        if cursor.rowcount > 0:
            print("\nAlteração realizada com sucesso!\n")
        else:
            print("\nNão foi possível realizar a alteração.\n")
    
    except Exception as e:
        print("\nErro ao modificar.\n")
    
    finally:
        conn.close

def limpar_console():
        # 1. Determina o sistema operacional
    if os.name == 'nt': # Windows
        comando_limpeza = 'cls'
    elif os.name == 'posix': # Linux e macOS
        comando_limpeza = 'clear'
    else:
        # Se o sistema for desconhecido, não faz nada
        return

    # 2. Executa o comando no shell
    try:
        os.system(comando_limpeza)
    except Exception as e:
        # Mensagem de aviso se o comando falhar por algum motivo
        print(f"Aviso: Não foi possível executar o comando de limpeza. Erro: {e}")

# Exibir Menu Principal
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
def opcao_escolhida():
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            adicionar_tarefa()

        elif opcao == '2':
            listar_tarefas()

        elif opcao == '3':
            remover_tarefa()
        
        elif opcao == '4':
            
            print("=====================")
            print("Modificar Tarefa")
            print("=====================")
            listar_tarefas()
        
            try:
                id_tarefa = int(input("\nDigite a ID da tarefa que deseja alterar: "))
                nova_descricao = input("\nDigite a nova descrição para esta tarefa: ")

                if not nova_descricao.strip():
                    print("\nA descrição está vázia. Operação cancelada...\n")
                    continue
            
                modificar_tarefa(id_tarefa, nova_descricao)
                    
            except ValueError:
                print("\nID inválido. Digite o ID corretamente, por favor.\n")

            except Exception as e:
                print(f"z\nOcorreu um erro: {e}\n")

        elif opcao == '5':
            break

        else:
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.\n")

if __name__ == "__main__":
    inicializar_bd() # <--- Nova função: Banco de Dados
    opcao_escolhida()
