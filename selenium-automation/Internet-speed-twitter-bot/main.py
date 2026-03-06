from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "Your Email"
TWITTER_PASSWORD = "Your Password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        try:
            accept = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept.click()
        except:
            pass

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)

    
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        print("Download:", self.down)
        print("Upload:", self.up)

    def tweet_at_provider(self):

        self.driver.get("https://x.com/i/flow/login")
        time.sleep(10)
        
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(5)

        # Password
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        tweet_box = self.driver.find_element(By.CSS_SELECTOR, "div[aria-label='Post text']")
        tweet_box.send_keys(tweet)

        time.sleep(3)

        post_button = self.driver.find_element(By.XPATH, "//span[text()='Post']")
        post_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
