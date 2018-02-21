#-*- coding: utf-8-*-
import os
import time as ti
import keyboard as kb
import requests as rq

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_window_handle = None
signin_window_handle = None


if __name__ == "__main__":

	url = "https://www.upbit.com/exchange?code=CRIX.UPBIT.KRW-ARK"

	driver = webdriver.Chrome("chromedriver")
	#driver.implicitly_wait(3)
	driver.get(url)
	main_window_handle = driver.current_window_handle

	count = 5
	
	for i in range(count):
		ti.sleep(1)

	#--------------------------login--------------------------

	driver.find_element_by_css_selector('section.ty01 .orderB .btnB > li:nth-of-type(2)').click()
	driver.find_element_by_css_selector('.btnKakao').click()

	while not signin_window_handle:
		for handle in driver.window_handles:
			if handle != main_window_handle:
				signin_window_handle = handle
				break

	driver.switch_to.window(signin_window_handle)

	driver.find_element_by_css_selector('#email').send_keys("input your email")
	driver.find_element_by_css_selector('#password').send_keys("input your password")
	driver.find_element_by_css_selector('#btn_login').click()

	driver.switch_to.window(main_window_handle)

	#--------------------------keyDown Check--------------------------

	activation = False

	while 1:

		try:
			if kb.is_pressed('/'):
				activation = not activation
				print("activation = True" if activation else "activation = False")
				ti.sleep(0.4)
			
			if activation == True:
				if kb.is_pressed('1'): #가장 위 매수
					driver.find_element_by_css_selector('section.ty01 .tabB li:nth-of-type(1)').click() #매수 창
					driver.find_element_by_css_selector('section.ty01 div.scrollB tbody > tr:nth-of-type(11)').click() #아래호가 클릭
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.inputB .plus').click() #호가 +
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB .btn').click() # 수량 선택버튼
					ti.sleep(0.1)
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB li:nth-of-type(1)').click() # 100% 버튼				
					driver.find_element_by_css_selector('section.ty01 .orderB .btnB > li:nth-of-type(2)').click() #주문 버튼
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a:nth-child(2)').click() #팝업 결정
					ti.sleep(0.1)
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a').click() #팝업 최종확인
					
				elif kb.is_pressed('2'): #가장 아래 매도 
					print("2")
					driver.find_element_by_css_selector('section.ty01 .tabB li:nth-of-type(2)').click() #매도 창
					driver.find_element_by_css_selector('section.ty01 div.scrollB tbody > tr:nth-of-type(10)').click() #윗호가 클릭
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.inputB .minus').click() #호가 -
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB .btn').click() # 수량 선택버튼
					ti.sleep(0.1)
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB li:nth-of-type(1)').click() # 100% 버튼
					driver.find_element_by_css_selector('section.ty01 .orderB .btnB > li:nth-of-type(2)').click() #주문 버튼
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a:nth-child(2)').click() #팝업 결정
					ti.sleep(0.1)
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a').click() #팝업 최종확인

				elif kb.is_pressed('3'):
					driver.find_element_by_css_selector('section.ty01 .tabB li:nth-of-type(3)').click() #취소 창you
					driver.find_element_by_css_selector('section.ty01 .orderB .btn').click() #취소 창
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a:nth-child(2)').click() #팝업 결정
					ti.sleep(0.1)
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a').click() #팝업 최종확인
				

				elif kb.is_pressed('`'): #비트 페이지 이동
					url = "https://www.upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC"
					driver.get(url)
					ti.sleep(0.1)

					# driver.find_element_by_css_selector('section.ty01 .tabB li:nth-of-type(2)').click() #매도 창
					# driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB .btn').click() # 수량 선택버튼
					# driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB li:nth-of-type(1)').click() # 100% 버튼
					# driver.find_element_by_css_selector('section.ty01 div.scrollB tbody > tr:nth-of-type(10)').click() #윗호가 클릭
					# driver.find_element_by_css_selector('section.ty01 .orderB dl div.inputB .minus').click() #호가 -
					# driver.find_element_by_css_selector('section.ty01 .orderB .btnB > li:nth-of-type(2)').click() #주문 버튼
					# driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a:nth-child(2)').click() #팝업 결정
					# ti.sleep(0.1)
					# driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a').click() #팝업 최종확인

				elif kb.is_pressed('*'): #현재 페이지 자동 매수
					driver.find_element_by_css_selector('section.ty01 .tabB li:nth-of-type(1)').click() #매수 창
					driver.find_element_by_css_selector('section.ty01 div.scrollB tbody > tr:nth-of-type(10)').click() #윗호가 클릭
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB .btn').click() # 수량 선택버튼
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB li:nth-of-type(1)').click() # 100% 버튼
					driver.find_element_by_css_selector('section.ty01 .orderB .btnB > li:nth-of-type(2)').click() #주문 버튼
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a:nth-child(2)').click() #팝업 결정
					ti.sleep(0.1)
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a').click() #팝업 최종확인

				elif kb.is_pressed('-'): #현재 페이지 자동 매도
					driver.find_element_by_css_selector('section.ty01 .tabB li:nth-of-type(2)').click() #매도 창
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB .btn').click() # 수량 선택버튼
					driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB li:nth-of-type(1)').click() # 100% 버튼
					driver.find_element_by_css_selector('section.ty01 div.scrollB tbody > tr:nth-of-type(11)').click() #아래호가 클릭
					driver.find_element_by_css_selector('section.ty01 .orderB .btnB > li:nth-of-type(2)').click() #주문 버튼
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a:nth-child(2)').click() #팝업 결정
					ti.sleep(0.1)
					driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a').click() #팝업 최종확인

			else:
				pass
		except:
			print("error")
			

		ti.sleep(0.01)

	#F1 매수 > 수량 > 원하는 만큼선택 > 아래호가 선택 > +버튼 선택 > 매수 버튼 
	#F2 매도 > 수량 > 100퍼센트 선택 > 윗호가 선택 > -버튼 선택 > 매도 버튼
	#F3 취소 > 취소 > 팝업 확인 > 최종 확인 

	#driver.find_element_by_css_selector('section.ty01 .orderB .btnB > li:nth-of-type(2)').click() #주문 버튼
				
	#driver.find_element_by_css_selector('section.ty01 .orderB dl div.layerB .btn').click() # 수량 선택버튼
				
	#driver.find_element_by_css_selector('section.ty01 .orderB dl /div.layerB li:nth-of-type(1)').click() # 100% 버튼
				
	#driver.find_element_by_css_selector('section.ty01 div.scrollB tbody > tr:nth-of-type(10)').click() #윗호가 클릭
	#driver.find_element_by_css_selector('section.ty01 div.scrollB tbody > tr:nth-of-type(11)').click() #아래호가 클릭
				
	#driver.find_element_by_css_selector('section.ty01 .orderB dl div.inputB .plus').click() #호가 +
	#driver.find_element_by_css_selector('section.ty01 .orderB dl div.inputB .minus').click() #호가 -
				
	#driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a:nth-child(2)').click() #팝업 결정
	#ti.sleep(0.1)
	#driver.find_element_by_css_selector('#checkVerifMethodModal > div > section > article > span > a').click() #팝업 최종확인

	#driver.find_element_by_css_selector('section.ty01 .tabB li:nth-of-type(1)').click() #매수 창
	#driver.find_element_by_css_selector('section.ty01 .tabB li:nth-of-type(2)').click() #매도 창
	#driver.find_element_by_css_selector('section.ty01 .tabB li:nth-of-type(3)').click() #취소 창


				