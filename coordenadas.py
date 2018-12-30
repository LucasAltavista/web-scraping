import selenium
import pandas
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Definindo o driver e abrindo o site
driver = webdriver.Firefox(executable_path=r'C:\\Users\\Lucas Altavista\\Desktop\\geckodriver.exe')
driver.get('http://www.mapcoordinates.net/pt')
wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.inputLat')))


# Abrindo arquivo com endereço das localidades
data = pandas.read_csv('C:\\Users\\Lucas Altavista\\Desktop\\Base.csv', sep = ';', encoding = "ISO-8859-1")

# Pegando apenas os endereços unicos para fazer a consulta
endereco = data['Endereco'].unique()

# Realizando a consulta 
txt = open('C:\\Users\\Lucas Altavista\\Desktop\\coordenadas.txt', 'w')
coordenadas = []
coordenadas.append('Endereço' + ';' + 'latitude' + ';' + 'longitude\n')

for item in endereco:
	element = driver.find_element_by_css_selector('#searchtext9')
	element.clear()
	element.send_keys(item)
	element.send_keys(Keys.ENTER)
	time.sleep(2.7)

	latitude_valor = driver.find_element_by_css_selector('.inputLat')
	latitude_valor = latitude_valor.get_attribute("value")
	longitude_valor = driver.find_element_by_css_selector('.inputLng')
	longitude_valor = longitude_valor.get_attribute("value")
	
	coordenadas.append(item + ';' + latitude_valor + ';' + longitude_valor + '\n')
	print(item + ';' + latitude_valor + ';' + longitude_valor)

driver.close()
txt.writelines(coordenadas)
txt.close()
