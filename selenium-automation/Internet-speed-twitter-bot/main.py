from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = r"C:\Users\DELL\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
TWITTER_EMAIL = "Your Email"
TWITTER_PASSWORD = "Your Password"
USER_NAME = "Your Username"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
class InternetSpeedTwitterBot:
     def __init__(self):
         service = Service(CHROME_DRIVER_PATH)
         self.driver = webdriver.Chrome(service=service, options=chrome_options)
         self.up = 0
         self.down = 0

     def get_internet_speed(self):

         self.driver.get("https://www.speedtest.net/result/18571954998")

         time.sleep(3)

         continue_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
         continue_button.click()

         time.sleep(3)

         go_button = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')
         go_button.click()

         time.sleep(60)

         self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]'
                                                      '/div[1]/div[2]/div/div[2]/span').text
         self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/'
                                                        'div/div[3]/div/div/div[2]/div[1]/div[1]/'
                                                        'div/div[2]/span').text

     def tweet_at_provider(self):

         self.driver.get("https://x.com/i/flow/login")
         wait = WebDriverWait(self.driver, 20)

         email_bar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                                          'div[2]/div[2]/div/div/div/div[4]/label/div/div['
                                                                          '2]/div/input')))
         email_bar.send_keys(TWITTER_EMAIL, Keys.ENTER)

         user_name_bar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]'
                                                                             '/div[2]/div[1]/div/div/div[2]/label/div/div[2]')))
         user_name_bar.send_keys(USER_NAME , Keys.ENTER)

         password_bar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                                          'div[2]/div[2]/div/div/div/div[4]/label/div/div['
                                                                          '2]/div/input')))
         password_bar.send_keys(TWITTER_PASSWORD, Keys.ENTER)

         tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
         tweet_bar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/'
                                                                          'div/div/div/div[1]/div/div'
                                                                          '/div/div/div/div[2]/div/'
                                                                          'div/div/div')))
         tweet_bar.send_keys(tweet)

         post_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div'
                                                                            '/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')))
         post_button.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()