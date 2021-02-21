## está sem usuário e senha do IG
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
from flask import Flask, render_template, request

#### CONFIG DO SELENIUM #####
#setup para usar webdriver no repl.it
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#driver
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1024, 768)


vencedor = 'bruno'

app = Flask('SorteioInsta')

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/result')
def result():
  print('FUNCAO RESULT INCIADA')
  url_post = request.args.get('url')
  winners = request.args.get('winners')
  ## ABRE PAGINA LOGIN
  url_ig = 'https://www.instagram.com/'
  driver.get(url_ig)
  sleep(4)
  
  #### FAZ LOGIN
  ## seleciona elementos (inputs e botão)
  input_username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
  input_password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
  btn_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
  ## faz as ações
  input_username.send_keys('seleniumPython_tdi') #inserir usuario
  input_password.send_keys('seleniumPython') #inserir senha
  btn_login.click()
  sleep(3)
  
  ### APÓS LOGIN ABRE O POST
  driver.get(url_post)
  sleep(4)

  ## tenta 
  try:
    ## seleciona btn de carregar mais comentarios 
    btn_more_comments = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button/span')
    ## enquanto o btn existing (is diplayed)
    while btn_more_comments.is_displayed():
      #clique nele
      btn_more_comments.click()
      sleep(4)
      #seleciona ele denovo
      btn_more_comments = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button/span')
  #tratativa de erro quando o botao nao poder ser mais selecionado
  #ou não existe.
  #poderia deixar apenas o pass mas uso o print para tbm ver o erro ;) 
  except Exception as err_msg:
    print(err_msg)
    pass
  sleep(3)

  ### PEGO TODOS COMENTARIOS
  comments = driver.find_elements_by_class_name('gElp9')
  list_users = []
  ## loop pegando cada usuario
  for comment in comments:
    username = comment.find_element_by_class_name('_6lAjh').text
    #verifico se nao esta na lista já
    if username not in list_users:
      #adiciono usuario na lista
      list_users.append(username)
  #seleciono o vencedor
  winner = random.choice(list_users)
  
  return render_template('result.html', winner=winner)



app.run(host='0.0.0.0')


