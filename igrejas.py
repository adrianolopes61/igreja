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
      'São Paulo',
      "2022-06-29"
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
    data = (
      '5',
      'Igreja de Fátima',
      'Av. Treze de Maio, 154 - Bairro de Fátima, Fortaleza - CE',
      'Pe. Cardoso'
      '85987321942'
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
	sql = "SELECT * FROM igrejas"
	cursor.execute(sql)
	results = cursor.fetchall()
	cursor.close()
	connection.close()
	for result in results:
	  print(result)
	  
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
	for result in results:
	  print(result)

while True:
	print(''' Menu
	1- Cadastrar santos
	2- Cadastrar igrejas
	3- Listar igrejas
	4- Listar Santos
	5- Sair
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
		print('Saindo')
		break	