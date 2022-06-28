#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pyperclip
import time

driver = webdriver.Chrome()


#파인리즈리조트 이동
driver.get('https://www.pineridge.co.kr/index.asp')

#통합예약버튼클릭
elem_totalbook = driver.find_element(By.CSS_SELECTOR,"#GNB > li.sub1 > a")
elem_totalbook.click()

#예약하기 버튼 클릭
elem_book = driver.find_element(By.CSS_SELECTOR,"body > div.s_con > div > div > div > p.format_text.btn_style01 > a")
elem_book.click()

#id입력
elem_id = driver.find_element(By.ID, "login")
elem_id.click()
pyperclip.copy('off1122')
elem_id.send_keys(Keys.COMMAND, 'v')
time.sleep(1)

#pw입력
elem_pw = driver.find_element(By.ID, "pwd")
elem_pw.click()
pyperclip.copy('off26187780')
elem_pw.send_keys(Keys.COMMAND, 'v')
time.sleep(1)

#로그인 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "body > div.s_con > div > div > div > div.contents_login_box > div > div > div.login_input_box > fieldset > form > dl > dd:nth-child(3) > span").click()

#경고창 확인버튼 누르기
driver.switch_to.alert
Alert(driver).accept()


