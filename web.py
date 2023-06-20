from selenium import webdriver
from selenium.webdriver.common.by import By #Some how needed to for Xpath find element :D
from bs4 import BeautifulSoup as bs
import re
from config_web import *
from helium import *
from time import sleep


uni_count=0
Uni_name_list = []


driver = webdriver.Firefox()
driver.implicitly_wait(20)


driver.get(WEB_URL)
y = 1000
for timer in range(0,50):
         driver.execute_script("window.scrollTo(0, "+str(y)+")")
         y += 1000  
         sleep(1)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

html_s=driver.page_source


#Load_more = driver.find_element(By.XPATH , Load_more_Button_Xpath)
#driver.execute_script("arguments[0].click();", Load_more)
#for more in range (4):
   # Load_more.click(Load_more_Button_Xpath)
   #sleep(5)
#   will  show you index of 40 uni as it is ranged "4"


reader=bs(html_s,"html.parser")
link_list=reader.find_all("a", class_="Anchor-byh49a-0 DetailCardGlobalUniversities__StyledAnchor-sc-1v60hm5-5 eMEqFO bFdMFJ")
#Will take all the Link with the change of uni name in it

for Eachlink in link_list: # Find the uni name and append into list
    Uni_name = re.findall(r'>.*<',str(Eachlink))
    Uni_name_list.append(Uni_name)

print(Uni_name_list , "\n", '-'*60 )
#driver.close()


for index in Uni_name_list:
    uni_count+=1
print("Total University count is : ", uni_count)






