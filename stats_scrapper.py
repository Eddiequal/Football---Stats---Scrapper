from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd



# PATH VARIABLES
PATH = "D:\Program files\chromedriver.exe"
PATH_TO_EXTENSION = R"C:\Users\Днс\Desktop\3.17_0"

# INITIAL SETTINGS
options = Options()
options.add_argument('load-extension=' + PATH_TO_EXTENSION)
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

user_input = input("Enter the league: ")
time.sleep(5)


driver.get('https://www.soccerstats.com/')

# # PRIVACY POLICY
# driver.find_element(By.CSS_SELECTOR, 'button[mode="primary"]'):
# driver.click()
time.sleep(3)
alert = driver.find_element(By.CSS_SELECTOR, 'button[class="fc-close"]').click()
 
time.sleep(3)

# LEAGUE CHOOSING
find = driver.find_element(By.CSS_SELECTOR, f'a[href="latest.asp?league={user_input}"]')
find.click()
time.sleep(4)

# ALERT BLOCKER
alert = driver.find_element(By.CSS_SELECTOR, 'button[class="fc-close"]').click()

# MATCHES
matches = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//a[@href="results.asp?league={user_input}" and text()="All matches"]')))
matches.click()
time.sleep(4)

# ALERT BLOCKER
alert = driver.find_element(By.CSS_SELECTOR, 'button[class="fc-close"]').click()
time.sleep(3)

# ALL MATCHES
all_matches = driver.find_element(By.XPATH, f'//a[@href="results.asp?league={user_input}&pmtype=bydate"]')
all_matches.click()
time.sleep(4)

# ALERT BLOCKER
alert = driver.find_element(By.CSS_SELECTOR, 'button[class="fc-close"]').click()

time.sleep(3)

webtable = pd.read_html(driver.find_element(By.XPATH, '//table[@id="btable"]').get_attribute('outerHTML'))[0]
df = pd.DataFrame(webtable)

df.columns = ["Date", "First Team", "Score", "Second  Team", "Stats", "HT", "2.5+", "TG", "BTS", "BTS2"]

df.drop(["Stats", "HT", "2.5+", "TG", "BTS", "BTS2"], axis=1, inplace=True)
df.to_csv('C:/Users/Днс/Desktop/file_match.csv')

print(df)








  
    




