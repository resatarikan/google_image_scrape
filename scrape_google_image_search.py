from  selenium import  webdriver;
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import urllib.request
import json;
import os

import time

driver = webdriver.Chrome('D:\webdrivers\chromedriver.exe');
default_path = "D:\\google_images"


def start(country, job_name):       

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    _path = os.path.join(default_path, country+"\\"  + job_name)
    try:
        os.mkdir(_path)
    except:
        pass
    os.chdir(_path)
    count_images = len(images)
    count = 0;
    for image in images:  
        count += 1
        
        if not image.get_attribute('src') == "":     
    
            
            print(str(count))
            try:
                time.sleep(3)
                image.click()
                time.sleep(5)
            
                
                try:
                    big_image = driver.find_element_by_css_selector("#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div > div.v4dQwb > a > img")             
                    #url = driver.execute_script("return document.querySelector('.d87Otf').parentElement.parentElement.parentElement.querySelector(\"[jsname='HiaYvf']\").src")
                    url = big_image.get_attribute("src")
                    print(url)
                    try:
                        urllib.request.urlretrieve(url, str(count) + "_car.jpg")
                    except:
                        print("indirme hatası")
                except:
                    print("javascript hatası")
            except:
                 print("tıklanamadı")
driver.get(uk_very_big_cars_on_road)


start("uk_big", "uk_very_big_cars_on_road_01" )
