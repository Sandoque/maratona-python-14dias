import requests
from bs4 import BeautifulSoup

#url
url = "https://www.iban.com/currency-codes"

#lista q armazera a lista de
todos_paises = []

#request + soup
requisicao = requests.get(url)
html_doc = requisicao.text
soup = BeautifulSoup(html_doc, 'html.parser')

#filtrar tabela e linhas
tabela = soup.find("table")
linhas = tabela.find_all("tr")[1:]

#loop em cada linha
for linha in linhas:

  #cria lista de tds dentro de cada tr
  items = linha.find_all("td")
  #pega valores 
  nome = items[0].text
  moeda_nome = items[1].text
  moeda_codigo = items[2].text

  #verifica se nao eh no universal currency
  if moeda_nome != "No universal currency":
    #monta dict 
    pais = {
      'país': nome,
      'codigo': moeda_codigo
    }
    #adiciona dict montada na lista
    todos_paises.append(pais)
    
def menu():
  #tenta pega e converte para int 
  try:
    escolha = int(input("Qual numero? >>"))
    #verifica se nao eh maior do q a lista
    if escolha > len(todos_paises):
      print('numero maior do q pode')
      menu()
    else:
      resultado = todos_paises[escolha]
      print(f"Vc escolheu {resultado['país']} , e a moeda é {resultado['codigo']}")
  except:
    print('mano, isso nao é um numero')
    menu()

#Inicia programa
print("BEM VINDO AO NOSSO CONSULTADOR DE MOEDA! SELECIO UMA OPCAO DO MENU")

#print de todos paises enumerados
for numera, pais in enumerate(todos_paises):
  print(f"## {numera} - {pais['país']}")

#chama menu
menu()