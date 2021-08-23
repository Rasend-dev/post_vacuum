import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#This module will help us to move the mouse over the posts to get the number of comments and likes
from selenium.webdriver.common.action_chains import ActionChains


URL_LOGIN = 'https://www.instagram.com/accounts/login/'
URL_TARGET = 'https://www.instagram.com/importiz_sc/'
USERNAME = 'talejandroest'
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
                driver.execute_script("window.scrollTo(0, window.scrollY + 770);")
                time.sleep(sec)

        def scrape_init(rows=3,state = 0):
            posts = {}
            for i in range(rows):
                for y in range(3):
                    # here we set up a action chain for the mouseover event
                    action = ActionChains(driver) #We have to initiate a new instance of ActionChains every time that we want to pass over the element without a pause
                    link = driver.find_element_by_xpath(f'//article//div[contains(@style,"flex-direction")]/div[{i + 1 + state}]/div[{y + 1}]/a')
                    action.move_to_element(link).perform()
                    n_likes = driver.find_element_by_xpath(f'//article//div[contains(@style,"flex-direction")]/div[{i + 1 + state}]/div[{y + 1}]/a/div[@class="qn-0x"]//li[1]/span[1]').text
                    n_comments = driver.find_element_by_xpath(f'//article//div[contains(@style,"flex-direction")]/div[{i + 1 + state}]/div[{y + 1}]/a/div[@class="qn-0x"]//li[2]/span[1]').text
                    posts[link.get_attribute('href')] = {'n_likes': n_likes, 'n_comments': n_comments}    

            return posts        

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

        #Here we get the n of posts
        n_posts = int(followers[0][:2])

        print(followers)
        print(scrape_init(rows=10))
        scroll_down(1)
        print(scrape_init(rows=3,state=8))
        scroll_down(1)
        print(scrape_init(rows=1,state=9))

    def tearDown(self):
        self.driver.quit()    

if __name__ == "__main__":
    unittest.main(verbosity =2)