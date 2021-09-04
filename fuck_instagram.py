import unittest
import time
import os
from function import Um
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#This module will help us to move the mouse over the posts to get the number of comments and likes
from selenium.webdriver.common.action_chains import ActionChains
#Exceptions
from selenium.common.exceptions import NoSuchElementException

#'https://www.instagram.com/marvel/'
#'https://www.instagram.com/importiz_sc/'

URL_LOGIN = 'https://www.instagram.com/accounts/login/'
URL_TARGET = 'https://www.instagram.com/importiz_sc/'
USERNAME = 'talejandroest'
PASS = '32146456q'
WDIR = os.getcwd()

class iHateInstagram(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= 'chromedriver.exe')
        driver = self.driver
        driver.get(URL_LOGIN)
        driver.maximize_window()

    def test_instagram(self):
        driver = self.driver 
        useful = Um()

        def scroll_down(times,sec=1):
            """
            This is a simple function that allow us to scroll down the instagram page
            to load more posts
            where times = is the number of scroll down that the function will do
            and sec = is the seconds that the function will wait until do the next scroll
            """
            for i in range(times):
                #this command helps to scroll down the page
                driver.execute_script("window.scrollTo(0, window.scrollY + 770);")
                time.sleep(sec)

        def scrape_init(rows=3,state = 0,fname=None):
            """
            This is a function that scrapes instagram most recent post where
            rows = is a vector that represent the current 3 posts to scrape
            state = is the actual place number of the div in the instagram page
            and fname = is the file name where we are going to load the data
            """
            for i in range(rows):
                for y in range(3): 
                    try:
                        # here we set up a action chain for the mouseover event
                        action = ActionChains(driver) #We have to initiate a new instance of ActionChains every time that we want to pass over the element without a restart
                        link = driver.find_element_by_xpath(f'//article//div[contains(@style,"flex-direction")]/div[{i + 1 + state}]/div[{y + 1}]/a')
                        action.move_to_element(link).perform()
                        n_likes = driver.find_element_by_xpath(f'//article//div[contains(@style,"flex-direction")]/div[{i + 1 + state}]/div[{y + 1}]/a/div[@class="qn-0x"]//li[1]/span[1]').text
                        n_comments = driver.find_element_by_xpath(f'//article//div[contains(@style,"flex-direction")]/div[{i + 1 + state}]/div[{y + 1}]/a/div[@class="qn-0x"]//li[2]/span[1]').text
                        useful.write_csv(fname,WDIR,[link.get_attribute('href'),n_likes,n_comments])
                        useful.write_json(fname,WDIR,{'link':link.get_attribute('href'),'n_likes':n_likes,'n_comments':n_comments})
                    except NoSuchElementException:
                        print(f'We have succeed scraping the target page: {fname}')
                        break       


        #Wait to the button
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//form[@id="loginForm"]//input[@name="username"]')))
        
        #Find the elements of forms
        username = driver.find_element_by_xpath('//form[@id="loginForm"]//input[@name="username"]')
        password = driver.find_element_by_xpath('//form[@id="loginForm"]//input[@name="password"]')
        login_btn = driver.find_element_by_xpath('//form[@id="loginForm"]/div/div/button[@type="submit"]')

        #Check if the elements form exits
        self.assertTrue(username and password and login_btn)
        username.click()
        username.clear()
        username.send_keys(USERNAME)

        password.click()
        password.clear()
        password.send_keys(PASS)

        login_btn.click()
        
        #Check if the search bar exits
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//nav//div/input[@placeholder="Search"]')))

        #Go to the target link
        driver.get(URL_TARGET)

        account_name = driver.find_element_by_xpath('//main//section/div/h2').text 

        followers = []

        #Find the first data of the account
        for i in range(3):
            info = driver.find_element_by_xpath(f'//header/section/ul/li[{i + 1}]//span').text
            followers.append(info)


        #here we create the csv and the json files of the account itself
        useful.create_csv(account_name,os.getcwd())
        useful.create_json(account_name,os.getcwd())

        #execute the code
        print(followers)
        scrape_init(rows=10,fname=account_name)
        scroll_down(1)
        scrape_init(rows=3,state=8,fname=account_name)
        scroll_down(1)
        scrape_init(rows=2,state=9,fname=account_name)


    def tearDown(self):
        self.driver.quit()    

if __name__ == "__main__":
    unittest.main(verbosity =2)