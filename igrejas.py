import mysql.connector
        
def cadastrarSanto():
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="aluno",
      database="sistema_pampulha"
    )
    cursor = connection.cursor()
    sql = "INSERT INTO santos (nome, data) VALUES (%s, %s)"
    data = (
      input("Digite o nome do santo: "),
      input("Digite a data de comemoração - EX: 2022-06-26: ")
    )
    cursor.execute(sql, data)
    connection.commit()
    userid = cursor.lastrowid
    cursor.close()
    connection.close()
    print("Foi cadastrado o novo usuário de ID:", userid)

def cadastrarIgreja():
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="aluno",
      database="sistema_pampulha"
    )
    cursor = connection.cursor()
    sql = "INSERT INTO igrejas (id_santo, nome, endereco, responsavel, telefone) VALUES (%s, %s, %s, %s, %s)"
    listarSantos()
    data = (
      input("Digite o Id do santo: "),
      input("Digite o nome da igreja: "),
      input("Digite o endereço completo: "),
      input("Digite o nome do responsável: "),
      input("Digite o telefone: ")
    )
    cursor.execute(sql, data)
    connection.commit()
    userid = cursor.lastrowid
    cursor.close()
    connection.close()
    print("Foi cadastrado o novo usuário de ID:", userid)

def listarIgrejas():
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="aluno",
      database="sistema_pampulha"
    )
    cursor = connection.cursor()
    sql = "SELECT i.id,s.nome,i.nome,i.endereco,i.responsavel,i.telefone FROM igrejas as i inner join santos as s on s.id = i.id_santo"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    print("|ID  |Santo  |Nome   |Endereco   |Responsável|   Telefone|")
    for x in results:
        print("| {:^3} | {:10} | {:20} | {:30} | {:10} | {:12} |".format(x[0], x[1], x[2], x[3], x[4], x[5]))
      
def listarSantos():
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="aluno",
      database="sistema_pampulha"
    )
    cursor = connection.cursor()
    sql = "SELECT * FROM santos"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    print("{:^10} | {:30} | {} |".format("ID", "Santo", "Data"))
    for id, santo, data in results:
      print("{:^10} | {:30} | {} |".format(id, santo, data))

def consultarIgreja():
    try:
        conectar()
        idIgreja = input("Digite o id da igreja: ") 
        consulta_sql = 'select * from igrejas WHERE id = ' + idIgreja
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print("Id:", linha[0])
            print("Nome:", linha[2])
            print("Responsável:", linha[4])
    except Error as erro:
        print("Falha ao consultar tabela: {}".format(erro))
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
    

# Programa principal
while True:
    print(''' Menu
    1- Cadastrar santos
    2- Cadastrar igrejas
    3- Listar igrejas
    4- Listar Santos
    5- Consultar igreja
    6- Sair
    ''')
    print('Digite uma opção: ')
    opcao = int(input())
    if opcao == 1:
        cadastrarSanto()
    elif opcao == 2:
        cadastrarIgreja()
    elif opcao == 3:
        listarIgrejas()
    elif opcao == 4: 
        listarSantos()
    elif opcao == 5:
        consultarIgreja()
    elif opcao == 6:
        print('Saindo')
        break   