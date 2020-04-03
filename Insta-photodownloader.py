'''Simple script to download photos in instagram using selenium and wget  '''



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException)
from urllib.request import urlopen, Request, urlretrieve
import sys
from bs4 import BeautifulSoup
import warnings
from bs4 import BeautifulSoup
import shutil
import wget


# create a new Firefox session
driver = webdriver.Firefox(executable_path = r'C:\Users\rapha\anaconda3\envs\Aulas\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe' ,log_path = None)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page

driver.get("https://www.instragram.com")

#aks user and password
driver.find_element_by_class_name("KPnG0").click()
driver.implicitly_wait(5)


# connec trought facebook




sfc =  driver.find_element_by_id('email')
sfc.click()
sfc.send_keys('') # Your email here <------------------------------------------------
driver.implicitly_wait(2)

sfw = driver.find_element_by_id('pass')
sfw.click()
sfw.send_keys('') # your password here <----------------------------------------------------------

driver.find_element_by_id("loginbutton").click()
driver.implicitly_wait(5)

try: # Try both ways to get over the pop up
   f1form = driver.find_element_by_xpath("/html/body/div[3]/div/div").is_displayed()
   if f1form is True:
      driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
   else:
      driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()


except:
   f2form = driver.find_element_by_xpath("/html/body/div[4]/div/div").is_displayed()
   if f2form is True:
      driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
   else:
      driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()

driver.implicitly_wait(8)
slist = list()
source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')
image_elements = driver.find_elements_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div/div//img") # Xpath to the images

for image in image_elements:            # Get all image link and append to  slist
   img_src = image.get_attribute("src")
   slist.append(img_src)


print(len(slist) , 'Photos URLS extracted')


for i in slist:           # download images
   local_image_filename = wget.download(i)

print("Every photo was all ready download")


