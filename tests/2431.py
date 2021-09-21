import time
import selenium
from selenium import webdriver #подключение библиотеки
driver = webdriver.Chrome() #получение объекта веб-драйвера для нужного браузера

selenium.get('https://google.com')

time.sleep(5)

selenium.quit()