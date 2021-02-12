import requests


print("Bem-vindo ao verificador de sites 1.0!")
print("Nenhum direito reservado.")
print("")
ficar = "s"
while ficar == "s":
	print("")
	urls = input("Insira as URLs dos sites que deseja verificar o status. (Separados por virgula :")
	print("")
	url_arr = [lista.strip() for lista in urls.split(',')]
	for i in url_arr:
		if "." in (i[-4:]):
			if (i[:7]) == "http://":
				url_request = i
			else:
				i = "http://" + str(i)
				url_request = i
			r_url_request = requests.get(url_request)
			c_request = r_url_request.status_code
			if c_request >= 200 and c_request <= 200:
				status =" Sucesso"
			else:
				status = "falha" 
			print (url_request + " " + status)
		else:
			print("URL inválido")
	
	ficar =" "
	while ficar not in ["s","n"]:
		ficar = input("Deseja verificar mais algum site? s/n :")
		if ficar == "n":
			print("Programa encerrado")
			break
		elif ficar == "s":
			continue
		else:
			print("Opção inválida")