from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys

servico = Service(GeckoDriverManager().install())

driver = webdriver.Firefox(service=servico)
driver.get("https://www.google.com.br/")
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]').send_key("Jesus")






