"""Projeto.: Gerenciador de Tarefas."""
import sqlite3

# Desativando a lista global. Utilização de um Banco de Dados
# tarefas = []

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
    print("\nBanco de dados inicializado com sucesso!")

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

        print(f"\nTarefa '{nova_tarefa.strip()}' adicionada com sucesso!")
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
        print("\n--- Tarefas Registradas no Banco de Dados ---\n")
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
            print("\nTarefa removida com sucesso!")
        else:
            print("\nOcorreu um erro. Tente novamente.")

        conn.close()

    except ValueError:
        print("\n Entrada inválida. Por favor, verifique o ID digitado.")


# Exibir Menu Principal
def exibir_menu():
    print("\n ▒▒▒ Gerenciador de Tarefas ▒▒▒\n")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Atualizar Tarefa")
    print("5. Sair")
    return input("\nEscolha uma opção: ")

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
            break

        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    inicializar_bd() # <--- Nova função: Banco de Dados
    opcao_escolhida()
