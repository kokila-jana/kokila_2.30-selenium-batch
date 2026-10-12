# from  selenium import webdriver
# from  selenium.webdriver.common.by import By
# import  time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.facebook.com/")
# a.find_element(By.ID,'_R_c9l6neappb6amH1_').send_keys("Kokila")
# t.sleep(3)
# a.find_element(By.NAME,'pass').send_keys("1234556")
# t.sleep(5)
# # a.find_element(By.XPATH,'//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div/div[1]').click()
# # a.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div[1]/div/div[3]/div/div/div/div[1]').click()
# a.find_element(By.CSS_SELECTOR,'#login_form > div > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xz9dl7a > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x2lah0s.x193iq5w.x6s0dn4.xz9dl7a.x1k70j0n.xzueoph.xzboxd6.x14l7nz5 > div > div > div > div.html-div.xdj266r.xat24cr.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x6s0dn4.x78zum5.xl56j7k.x1e0frkt.xf0ucvx.xx2axb6').click()
# t.sleep(5)

# from  selenium import webdriver
# from  selenium.webdriver.common.by import By
# import  time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.google.com/")
# a.find_element(By.CLASS_NAME,'gLFyf').send_keys("Dhoni")
# a.find_element(By.TAG_NAME,'textarea').send_keys("kohli")
# a.find_element(By.LINK_TEXT,'Gmail').click()
# a.find_element(By.PARTIAL_LINK_TEXT,'Gma').click()
# t.sleep(5)

# from  selenium import webdriver
# from  selenium.webdriver.common.by import By
# import  time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.facebook.com/")
# a.find_element(By.CSS_SELECTOR,'#_r_3_').send_keys("Kokila")
# t.sleep(5)

# from  selenium import webdriver
# from  selenium.webdriver.common.by import By
# import  time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://artoftesting.com/samplesiteforselenium")
# t.sleep(2)
# # a.find_element(By.ID,'male').click()
# # t.sleep(2)
# # a.find_element(By.ID,'female').click()
# # t.sleep(5)
# a.find_element(By.CLASS_NAME,'Automation').click()
# t.sleep(2)
# a.find_element(By.CLASS_NAME,'Performance').click()
# t.sleep(5)


# from  selenium import webdriver
# from  selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import  time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.amazon.in/")
# t.sleep(5)
# a.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys("Laptop"+Keys.ENTER)
# t.sleep(5)


# from  selenium import webdriver
# from  selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import  time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://artoftesting.com/samplesiteforselenium")
# t.sleep(2)
# a.find_element(By.XPATH,'//*[@id="fname"]').send_keys("kokila")
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="fname"]').clear()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="fname"]').send_keys("Jana")
# t.sleep(3)

# from  selenium import webdriver
# from  selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import  time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://artoftesting.com/samplesiteforselenium")
# t.sleep(2)
# b=a.find_element(By.XPATH,'//*[@id="fname"]')
# print(b.get_attribute("id"))
# print(b.get_attribute("type"))
# print(b.get_attribute("name"))

# from  selenium import webdriver
# from  selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import  time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://artoftesting.com/samplesiteforselenium")
# t.sleep(2)
# b=a.find_element(By.XPATH, '//*[@id="fname"]')
# print(b.value_of_css_property("height"))
# print(b.value_of_css_property("width"))
# print(b.value_of_css_property("color"))
# print(b.value_of_css_property("border"))
# print(b.value_of_css_property("background-color"))

# from  selenium import webdriver
# from  selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import  time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.amazon.in/")
# t.sleep(2)
# b=a.find_element(By.LINK_TEXT,'Mobiles')
# print(b.is_displayed())

from  selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import  time as t
a=webdriver.Chrome()
a.maximize_window()
a.get("https://artoftesting.com/samplesiteforselenium")
t.sleep(2)
b=a.find_element(By.ID, 'male')
b.click()
print(b.is_selected())
