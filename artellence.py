from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import PySimpleGUI as sg

sg.theme('DarkTeal12')

layout = [
    [sg.T('find in artellence')],
    [sg.HorizontalSeparator()],
    [sg.T('режим работы')],
    [sg.Radio('by number', 'RADIO1', key='num1', default=True), sg.Radio('by links', 'RADIO1', key='link1', )],
    [sg.Button('начать')]
    ]

window = sg.Window('TGspamer', layout, finalize=True, size=(600,400), resizable=True)

window.set_min_size((600, 400))

window.finalize()

def find():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get('https://lab.artellence.com/single')
    driver.find_element(By.ID, 'email').send_keys('oleh.panshutin@cyberpolice.gov.ua') 
    driver.find_element(By.ID, 'password').send_keys('cysnzNDwda') 
    driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div > div.loginForm > form > button').click() 
    driver.find_element(By.CSS_SELECTOR, '#root > div > main > div.modal.manualPopup > div.modal__content > div.manualPopup__close > svg').click()
    with open('numbers.txt', 'r', encoding='UTF-8') as f:
        num = f.readlines()
    with open('people.txt', 'w', encoding='UTF-8') as w:
        for number in num:
            driver.find_element(By.CSS_SELECTOR, '#phone').send_keys(number)
            sleep(2)
            driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > section > div.searchButtons > div > button.searchButtons__search-btn.btn.btn-neuro').click()
            rez = 'Пошук'
            while rez == 'Пошук':
                rez = driver.find_element(By.CSS_SELECTOR, '#root > div > main > aside > div.taskTabs > div > div.taskTab__info > div.taskTab__title').text
                sleep(2)
            if rez == 'Результати (0)':
                pass
            else:
                w.write(number)
            driver.get('https://lab.artellence.com/single')
    sg.popup('нажмите OK чтобы закрыть браузер')

def find1():
    with open('links.txt', 'r', encoding='UTF-8') as l:
        links = l.readlines()
    driver = webdriver.Chrome()
    driver.get('https://lab.artellence.com/single')
    driver.implicitly_wait(30)
    driver.find_element(By.ID, 'email').send_keys('oleh.panshutin@cyberpolice.gov.ua')
    driver.find_element(By.ID, 'password').send_keys('cysnzNDwda')
    driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div > div.loginForm > form > button').click()
    driver.find_element(By.CSS_SELECTOR, '#root > div > main > div.modal.manualPopup > div.modal__content > div.manualPopup__close > svg').click()
    with open('people.txt', 'w', encoding='UTF-8') as w:
        for link in links:
            driver.find_element(By.CSS_SELECTOR, '#links').send_keys(link)
            sleep(2)
            driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > section > div.searchButtons > div > button.searchButtons__search-btn.btn.btn-neuro').click()
            rez = 'Пошук'
            while rez == 'Пошук':
                rez = driver.find_element(By.CSS_SELECTOR, '#root > div > main > aside > div.taskTabs > div > div.taskTab__info > div.taskTab__title').text
                sleep(2)
            link1 = f'{link}{rez}\n'  
            w.write(link1)
            driver.get('https://lab.artellence.com/single')
    sg.popup('нажмите OK чтобы закрыть браузер')

while True:
    try:

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break        

        if event == 'начать':
            if values['num1']:
                window.close()
                find()
            else:
                window.close()
                find1()

    except Exception as a:
        sg.popup('error')
        print(a)