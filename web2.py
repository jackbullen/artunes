#!/usr/bin/env python3

import shutil
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from subprocess import call

class google_image:

    def __init__(self):
        print('google_image object created.')

    def download_song_imgs(self, song_name):
        
        url = 'https://www.google.ca/imghp'
        driver = webdriver.Chrome(r'/Users/fred/Downloads/chromedriver')
        driver.get(url)

        driver.find_element_by_name('q').send_keys(song_name)
        driver.find_element_by_name('q').send_keys(Keys.RETURN)

        driver.find_element_by_id('hdtb-tls').click()
        time.sleep(1)
        driver.find_element_by_class_name('mn-hd-txt').click()
        driver.find_element_by_link_text('Large').click()

        img_links = set()

        for i in range(10):
            driver.find_element_by_css_selector("div[data-ri = '"+str(i)+"'] img ").click()
            try:
                link = driver.find_element_by_class_name("irc_mi").get_attribute("src")
            except:
                print("Couldnt grab a file")
            print(i,':',link)
            if link is not None:
                print("adding")
                img_links.add(link)


#   Interesting bit of code to get bunch of href thingys.
#img_links = driver.find_elements_by_xpath("//a[@href]")
#img_links = [e.get_attribute('href') for e in img_links]
#img_links = [e for e in img_links if e[:28]=='https://www.google.ca/imgres']


        for i,img_link in enumerate(img_links):
            call("wget "+img_link+" -P ./images/", shell=True)
            #img_data = requests.get(img_link).content
            #with open('./images/'+img_link[-8:]+str(i)+'.jpg','wb') as handle:
                #handle.write(img_data)

        print("Saved images")
        driver.close()
