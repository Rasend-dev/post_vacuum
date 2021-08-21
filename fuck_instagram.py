import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL_LOGIN = 'https://www.instagram.com/accounts/login/'
URL_TARGET = 'https://www.instagram.com/importiz_sc/'
USERNAME = 'username_no_generico'
PASS = '32146456q'

class iHateInstagram(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= 'chromedriver.exe')
        driver = self.driver
        driver.get(URL_LOGIN)
        driver.maximize_window()

    def test_instagram(self):
        driver = self.driver 

        def scroll_down(times,sec=1):
            for i in range(times):
                #this command helps to scroll down the page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(sec)

        #esperamos a que cargue el boton
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//form[@id="loginForm"]//input[@name="username"]')))
        
        #encontramos los elementos para llenar el formulario
        username = driver.find_element_by_xpath('//form[@id="loginForm"]//input[@name="username"]')
        password = driver.find_element_by_xpath('//form[@id="loginForm"]//input[@name="password"]')
        login_btn = driver.find_element_by_xpath('//form[@id="loginForm"]/div/div/button[@type="submit"]')

        #Verificamos si el formulario esta disponible 
        self.assertTrue(username and password and login_btn)
        username.click()
        username.clear()
        username.send_keys(USERNAME)

        password.click()
        password.clear()
        password.send_keys(PASS)

        login_btn.click()
        
        #No nos movemos hasta que cargue por lo menos el elemento de la barra de busqueda
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//nav//div/input[@placeholder="Search"]')))

        #Nos movemos al perfil que queremos scrapear
        driver.get(URL_TARGET)

        followers = []

        #Encontramos el Numero de posts, los que te siguen y a los que sigues
        for i in range(3):
            info = driver.find_element_by_xpath(f'//header/section/ul/li[{i + 1}]//span').text
            followers.append(info)


        #here we wait 1 sec to wait the webelement 
        scroll_down(1)
        href = []

        for i in range(8):
           for y in range(3):
                link = driver.find_element_by_xpath(f'//article//div[contains(@style,"flex-direction")]/div[{i + 1}]/div[{y + 1}]/a').get_attribute('href')
                href.append(link)
        
        #here we made 3 scroll down and wait 2 sec for the next
        scroll_down(3,sec=2)

        for i in range(6):
           for y in range(3):
                link = driver.find_element_by_xpath(f'//article//div[contains(@style,"flex-direction")]/div[{4 + 1}]/div[{y + 1}]/a').get_attribute('href')
                href.append(link)

        print(followers)
        print(href)
        print(len(href))
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()    

if __name__ == "__main__":
    unittest.main(verbosity =2)