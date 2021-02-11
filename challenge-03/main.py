
# use esta parte de cima para declarar a 4 funções #


#####!! NÃO EDITE O CÓDIGO ABAIXO DESTA LINHA !!#####

#criação da food_list
food_list = {
  'paçoquinha': 'Um doce de amendoím brasileiro',
  'brigadeiro': 'Um doce muito delicioso',
  'pizza': 'um tipo de comida da italia',
  'hamburguer': 'comida dos USA'
}

#####################################
######## TESTES ADD_FOOD #########
#####################################

def add_food(comida=None, descricao=None):
	if (comida and descricao) is not None:
		if (type(comida) and type(descricao)) == str:
			if comida in food_list:
				print(f"{comida} já existe na lista")
			else:
				nova_comida = {comida:descricao}
				food_list.update(nova_comida)
				print(f"{comida} cadastrado com sucesso")
		else:
			print("Os valores precisam ser do tipo string")
	else:
		print("digita a comida e descrição aí")

# ADD_FOOD - TESTE 1
print("\n#### ADD_FOOD - TESTE 1")
print("Usando add_food com valores sendo int")
print("add_food(100, 23)\n")
#excuta:
add_food(100, 23)

# ADD_FOOD - TESTE 2
print("\n#### ADD_FOOD - TESTE 2")
print("Usando add_food sem passar a descrição.")
print("add_food('pizza')\n")
#excuta:
add_food('pizza')

# ADD_FOOD - TESTE 3
print("\n#### ADD_FOOD - TESTE 3")
print("Usando add_food com comida já existente.")
print("add_food('brigadeiro', 'Um doce brasileiro')\n")
#excuta:
add_food('brigadeiro', 'Um doce brasileiro')

# ADD_FOOD - TESTE 4
print("\n#### ADD_FOOD - TESTE 4")
print("Usando add_food adicionando uma comida.")
print("add_food('lasanha', 'Camadas de massa e molho')\n")
#excuta:
add_food('lasanha', 'Camadas de massa e molho')


#####################################
######## TESTES DELETE_FOOD #########
#####################################

def delete_food (comida=None):
	if comida is not None:
		if type(comida) == str:
			if comida in food_list:
				food_list.pop(comida)
				print(f"{comida} removido da lista")
		else:
			print("Nome de comida é string")
	else:
		print("Precisa digitar nome de comida")


# DELETE_FOOD - TESTE 1
print("\n#### DELETE_FOOD - TESTE 1")
print("Usando delete_food com valor sendo int")
print("delete_food(100)\n")
#excuta:
delete_food(100)

# DELETE_FOOD - TESTE 2
print("\n#### DELETE_FOOD - TESTE 2")
print("Usando delete_food sem nenhum valor.")
print("delete_food()\n")
#excuta:
delete_food()

# DELETE_FOOD - TESTE 3
print("\n#### DELETE_FOOD - TESTE 3")
print("Usando delete_food com comida que não existe na lista.")
print("delete_food('massa')\n")
#excuta:
delete_food('massa')

# DELETE_FOOD - TESTE 4
print("\n#### DELETE_FOOD - TESTE 4")
print("Usando delete_food removendo uma comida.")
print("delete_food('paçoquinha')\n")
#excuta:
delete_food('paçoquinha')

#####################################
## TESTES UPDATE_FOOD ##
#####################################

def update_food(comida=None, descricao=None):
	if (comida and descricao) is not None:
		if (type(comida) and type(descricao)) == str:
			if comida in food_list:
				print(f"{comida} será atualizada")
				(food_list[comida])=descricao

			else:
				print(f"{comida} não existe na lista")
		else:
			print("Os valores precisam ser do tipo string")
	else:
		print("digita a comida e descrição aí")

# UPDATE_FOOD - TESTE 1
print("\n#### UPDATE_FOOD - TESTE 1")
print("Usando update_food com valores sendo int")
print("update_food(100, 23)\n")
#excuta:
update_food(100, 23)

# UPDATE_FOOD - TESTE 2
print("\n#### UPDATE_FOOD - TESTE 2")
print("Usando update_food sem passar a descrição.")
print("update_food('pizza')\n")
#excuta:
update_food('pizza')

# UPDATE_FOOD - TESTE 3
print("\n#### UPDATE_FOOD - TESTE 3")
print("Usando update_food com comida não existente.")
print("update_food('sorvete', 'Um doce gelado da italia')\n")
#excuta:
update_food('sorvete', 'Um doce gelado da italia')


# UPDATE_FOOD - TESTE 4
print("\n#### UPDATE_FOOD - TESTE 4")
print("Usando update_food e atualizando uma comida.")
print("update_food('brigadeiro', 'Melhor doce do mundo.')\n")
#excuta:
update_food('brigadeiro', 'Melhor doce do mundo.')

#####################################
## TESTES GET_FOOD ##
#####################################

def get_food(comida=None):
	if comida is not None:
		if type(comida) == str:
			if comida in food_list:
				print(food_list[comida])
			else:
				print(f"{comida} não existe na lista")
		else:
			print("Os valores precisam ser do tipo string")
	else:
		print("digita a comida e descrição aí")

# GET_FOOD - TESTE 1
print("\n#### GET_FOOD - TESTE 1")
print("Usando get_food com valor sendo int")
print("get_food(505)\n")
#excuta:
get_food(505)

# GET_FOOD - TESTE 2
print("\n#### GET_FOOD - TESTE 2")
print("Usando get_food sem passar a comida.")
print("get_food()\n")

get_food()

# GET_FOOD - TESTE 3
print("\n#### GET_FOOD - TESTE 3")
print("Usando get_food com comida não existente.")
print("get_food('noodle')\n")
get_food('noodle')

# GET_FOOD - TESTE 4
print("\n#### GET_FOOD - TESTE 4")
print("Usando get_food e pesquisando a descrição uma comida.")
print("get_food('hamburguer')\n")
get_food('hamburguer')


#####!!!!!!!!!!!!!! THE END !!!!!!!!!!!!!!#####


## Linha de Chegada ##
print("\n Winners win")
print(u"\U0001F40D" + " Maratona Python")
# © 2020 Maratona Python. Todos os direitos reservados.
# https://www.maratonapython.com.br