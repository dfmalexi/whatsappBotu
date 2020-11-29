from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time
import win32clipboard
import speech
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\EMRE\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") #Path to your chrome profile
options.add_argument("--profile-directory= Profile 1")
w = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", chrome_options=options)
w.get("https://web.whatsapp.com/")
wait = WebDriverWait(w, 600)
w.maximize_window()
time.sleep(10)

def sentMessage(s):
    box=w.find_element_by_class_name("_2vJ01").find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    box.send_keys(s)
    box.send_keys(Keys.RETURN)


def whatsapp(t):
    
    x=0
    t+=1
        
    users= w.find_elements_by_class_name("_1582E")
    for i in users:

        try:
            m=i.find_element_by_class_name("_31gEB")
            i.click()
            time.sleep(2)
            messages=i.find_element_by_class_name("_2iq-U")
            s=messages.get_attribute("title")
            print(s)
            sent=speech.speech(s)
            print(s)
            
            try:
                sentMessage(sent)
            except Exception as e:
                print(e)
            x=1

                
        except:
            if(x==1):
                i.click()
       
    if t==60:

        w.refresh()
        wait = WebDriverWait(w, 600)
        time.sleep(3)
    return t
        
t=0
while True:
    
    t=whatsapp(t)






# pyautogui.doubleClick(742,886)
# pyautogui.click(742,886)



# time.sleep(3)
# users = w.find_elements_by_class_name("_2iq-U")
# for i in users:
#     x=i.get_attribute("title")
#     print(x)
# w.close()
# pyautogui.hotkey('ctrl', 'c')
# win32clipboard.OpenClipboard()
# data = win32clipboard.GetClipboardData()
# print(type(data))
# print(data)
# win32clipboard.CloseClipboard()