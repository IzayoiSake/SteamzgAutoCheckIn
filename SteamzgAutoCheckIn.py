
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import sys
class SteamzgAutoCheckIn:

    def __init__(self, cookies = ""):
        self.url = 'https://steamzg.com'
        self.checkInUrl = 'https://steamzg.com/account/lottery'
        self.cookies = cookies
        
        
    def Initdriver(self):
        # chenck system platform
        if sys.platform.startswith('win'):
            chrome_path = os.path.join("drivers", "chromedriver.exe")
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            chrome_path = os.path.join("drivers", "chromedriver")

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--connect-timeout=10')
        # disable infobars
        chrome_options.add_argument('--disable-infobars')
        # disable notifications
        chrome_options.add_argument('--disable-notifications')


        chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = chrome_path)
        print("Init driver finished")
    def AddCookies(self):
        self.driver.get(self.url)
        for cookie in self.cookies.split(';'):
            name, value = cookie.strip().split('=', 1)
            self.driver.add_cookie({'name': name, 'value': value})
        print("Add cookies finished")
    def ClickWelcomeButton(self):
        try:
            # find class="poi-dialog__footer__btn poi-dialog__footer__btn_default"
            welcomeButton = self.driver.find_element_by_class_name("poi-dialog__footer__btn_default")
            welcomeButton.click()
        except WebDriverException:
            print("welcome button lost")
    def AutoCheckIn(self):
        # "签到"
        self.driver.get(self.checkInUrl)
        checked = True
        try:
            checkIn = self.driver.find_element_by_xpath('//span[@class="poi-icon__text" and text()="签到"]/ancestor::a[@class="poi-tooltip is-bottom inn-nav__point-sign-daily__btn"]')
            checked = False
        except WebDriverException:
            print("checkIn button lost")
        if not checked:
            # wait 2s
            time.sleep(2)
            checkIn.click()
        print("CheckIn finished")
        # "白送模式"
        while True:
            self.driver.get(self.checkInUrl)
            freeModeSelect = self.driver.find_element_by_xpath('//h3[contains(text(), "白送模式")]/..')
            freeModeSelect.click()
            time.sleep(2)
            goButton = self.driver.find_element_by_xpath('//span[@class="poi-icon__text" and text()="GO"]')
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", goButton)
            goButton.click()
            # Check if the times reach the limit
            reachLimit = True
            time.sleep(2)
            alrtMsg = self.driver.find_element_by_xpath('//div[@class="poi-alert__msg"]')
            if "达到最大抽奖次数" in alrtMsg.text:
                reachLimit = True
            elif "恭喜你" in alrtMsg.text:
                reachLimit = False
            elif "很不幸运" in alrtMsg.text:
                reachLimit = False
            else:
                reachLimit = False
            
            if reachLimit:
                break
        print("FreeMode finished")
        # "0风险白嫖抽奖"
        while True:
            self.driver.get(self.checkInUrl)
            zeroRiskModeSelect = self.driver.find_element_by_xpath('//h3[contains(text(), "0风险白嫖抽奖")]/..')
            zeroRiskModeSelect.click()
            time.sleep(2)
            goButton = self.driver.find_element_by_xpath('//span[@class="poi-icon__text" and text()="GO"]')
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", goButton)
            goButton.click()
            # Check if the times reach the limit
            reachLimit = True
            time.sleep(2)
            alrtMsg = self.driver.find_element_by_xpath('//div[@class="poi-alert__msg"]')
            if "达到最大抽奖次数" in alrtMsg.text:
                reachLimit = True
            elif "恭喜你" in alrtMsg.text:
                reachLimit = False
            elif "很不幸运" in alrtMsg.text:
                reachLimit = False
            else:
                reachLimit = False
            
            if reachLimit:
                break
        print("ZeroRiskMode finished")
if __name__ == "__main__":
    cookies = os.getenv("cookies")
    if cookies == None:
        cookies = open("cookies.txt", "r").read()
    if cookies == None:
        print("cookies not found")
        exit()
    autoCheckIn = SteamzgAutoCheckIn()
    autoCheckIn.Initdriver()
    autoCheckIn.AddCookies()
    autoCheckIn.AutoCheckIn()
    print("Auto CheckIn finished")
    # input("press any key to exit")