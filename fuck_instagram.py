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
        
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//nav//div/input[@placeholder="Search"]')))

        driver.get(URL_TARGET)

        followers = []

        for i in range(3):
            info = driver.find_element_by_xpath(f'//header/section/ul/li[{i + 1}]//span').text
            followers.append(info)

        #Extraemos el numero de posts
        n_posts = int(followers[0][:2])
        print(n_posts)
        href = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a')
        print(href.get_attribute('href'))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(30)

    def tearDown(self):
        self.driver.quit()    

if __name__ == "__main__":
    unittest.main(verbosity =2)