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
            id INTEREGER PRIMARY KEY, 
            descricao TEXT NOT NULL
            )
    """)
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso!")

# Lógica da nova tarefa
def adicionar_tarefa():
    nova_tarefa = input("Digite a descrição da nova tarefa: ")
    
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
        print("\nNão há registro de tarefas")
    else:
        print("\n--- Tarefas Registradas no Banco de Dados ---")
        for id, descricao in tarefas_bd:
            print(f"ID {id}: {descricao}")

    conn.close()    
    
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
            listar_tarefas()

        elif opcao == '3':
            print("Saindo do gerenciador de tarefas...!")
            break

        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    inicializar_bd() # <--- Nova função: Banco de Dados
    opcao_escolhida()
