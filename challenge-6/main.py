import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
 #================ CRIANDO UMA FUBÇÃO DE SCRAPPING ===================
 
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
      'pais': nome,
      'codigo': moeda_codigo
    }
    #adiciona dict montada na lista
    todos_paises.append(pais)
    
def pergunta_pais(msg):
  print(msg)
  #tenta pega e converte para int 
  try:
    escolha = int(input("Qual numero? >>"))
    #verifica se nao eh maior do q a lista
    if escolha > len(todos_paises):
      print('numero maior do q pode')
      return pergunta_pais(msg)
    else:
      resultado = todos_paises[escolha]
      print(f"Vc escolheu {resultado['pais']} , e a moeda é {resultado['codigo']}")
      return resultado['codigo']  
  except:
    print('mano, isso nao é um numero')
    return pergunta_pais(msg)

def pergunta_quantia(moeda_origem, moeda_destino):
  print(f'quantos {moeda_origem} você quer converter para {moeda_destino}?')
  try:
    quantia = float(input("#: "))
    return quantia
  except:
    print('isso nao é um numero')
    return pergunta_quantia(moeda_origem, moeda_destino)

#Inicia programa
print("BEM VINDO AO NOSSO CONSULTADOR DE MOEDA! SELECIO UMA OPCAO DO MENU")

#print de todos paises enumerados
for numera, pais in enumerate(todos_paises):
  print(f"## {numera} - {pais['pais']}")

#captura origem e destino
moeda_origem = pergunta_pais('Qual o pais de origem?')
moeda_destino = pergunta_pais('Qual o pais de destino?')

#captura valor
quantia = pergunta_quantia(moeda_origem, moeda_destino)


#monta url com base nos valores
url_tw = f"https://transferwise.com/gb/currency-converter/{moeda_origem}-to-{moeda_destino}-rate?amount={quantia}"

#scraping na tw
request_tw = requests.get(url_tw)
html_tw = request_tw.text
soup_tw = BeautifulSoup(html_tw, 'html.parser')

#pega o conversao e calcula
conversao = float(soup_tw.find('span', class_='text-success').string)

#calcula final
final = quantia * conversao
print(format_currency(final, moeda_destino))