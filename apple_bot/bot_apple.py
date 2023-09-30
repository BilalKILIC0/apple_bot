from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


site = webdriver.Chrome()
site.maximize_window()

site.get("https://www.apple.com/tr/")
sleep(4)


def giris():
    site.find_element(By.XPATH, "/html/body/div[1]/nav/div/ul/li[2]/div/div/div[4]/ul/li[1]/a/span[1]").click()
    sleep(1)
    site.find_element(By.XPATH, "/html/body/nav/div/ul/li[1]/a/span[1]").click()
    sleep(1)
    site.find_element(By.XPATH, "/html/body/main/section[1]/div/div[2]/a").click()
    sleep(1)
    site.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/div/div[1]/fieldset/div/div[1]/input").click()
    sleep(2)
    site.execute_script("window.scrollBy(0,800)","")
    sleep(2)
    site.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/div/div[2]/fieldset/ul/li[2]/label/img").click()
    sleep(3)
    site.execute_script("window.scrollBy(0,500)","")
    sleep(2)
    site.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/div/div[3]/fieldset/div/div[1]/label/span/span[1]").click()
    sleep(2)
    site.execute_script("window.scrollBy(0,600)","")
    sleep(2)
    site.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div[3]/div[3]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/span/form/div/span/button").click()
    sleep(3)
    site.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/form/button").click()
    sleep(5)


giris()

sleep(5)
site.close
