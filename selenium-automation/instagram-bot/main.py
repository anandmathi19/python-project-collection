import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = "Your Email"
PASSWORD = "Your Password"
ACCOUNT = "Account Name"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)

    def login(self):
        self.driver.get("https://www.instagram.com/#")
        email_bar = self.wait.until(expected_conditions.presence_of_element_located
                                    ((By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')))
        email_bar.send_keys(EMAIL)

        password_bar = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')))
        password_bar.send_keys(PASSWORD, Keys.ENTER)

        not_now_button = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='button' and normalize-space(text())='Not now']")))
        not_now_button.click()

    def follow_users(self):
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}/followers")


        following_path = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(@href, '/following/')]")))
        following_path.click()

        time.sleep(2)

        scroll_bar = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@role='dialog']//div[@style and contains(@style,'overflow')]")))


        for i in range(10):

            self.driver.execute_script(
                "arguments[0].parentNode.scrollTop = arguments[0].parentNode.scrollHeight", scroll_bar)

            time.sleep(1)

            follow_button = scroll_bar.find_elements(By.XPATH, ".//button[text()='Follow']")

            for button in follow_button:

                button.click()
                time.sleep(1)



bot = InstaFollower()
bot.login()
bot.follow_users()


