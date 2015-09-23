import datetime,os,sys
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def checkInternetConnection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print 'Sem conexao com a internet aguarde...'
        return False

def main():
    while checkInternetConnection() == True:
        count = 0
        i = 0
        url = 'www.guiadosquadrinhos.com'
        driver = webdriver.PhantomJS(executable_path='/home/suedx1000/Dropbox/python/scraping/node_modules/phantomjs/bin/phantomjs', port=65000)
        #driver = webdriver.PhantomJS(executable_path=r"C:/Users/UserName/Desktop/plumb/phantomjs.exe", port=65000)
        driver.set_window_size(1120, 550)
        driver.get("http://www.guiadosquadrinhos.com/todas-capas-disponiveis")
        driver.implicitly_wait(50)
        while True:          
            pg = driver.page_source
            s = BeautifulSoup(pg, "html.parser")
            for link in s.find_all('a', {'class': 'suppress'}):
                print url+'/'+ link.get('href').encode('utf-8')
                #print link.get('title').encode('utf-8')            
            count+=1
            print count
            wait = WebDriverWait(driver, 100)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='next_last']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='Lista_album_capas']")))
            pg_next = driver.find_elements_by_xpath("//a[@class='next_last']")         
            pg_next[0].click()            
        else:
            pass
        time.sleep(1)

        print datetime.datetime.now()
        print "Passamos em "+count+" paginas."
    else:
            print "Esta sem internet ou sua conexao caiu, reiniciando..."
main()