
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import sys
from chromeDriverManager import ChromeDriverManager

class SteamzgAutoCheckIn:

    def __init__(self, cookies = "", account = "", password = ""):
        self.url = 'https://steamzg.com'
        self.checkInUrl = 'https://steamzg.com/account/lottery'
        self.cookies = cookies
        self.account = account
        self.password = password
        self.timeout = 5
        
        
    def Initdriver(self):
        

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
        # chrome_options.add_argument('--headless')

        # chromeManager = ChromeDriverManager()
        # chromeDirverPath = chromeManager.checkChromeDriver()
        # self.driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = chromeDirverPath)
        self.driver = webdriver.Chrome(chrome_options = chrome_options)
        print("Init driver finished")

    def AddCookies(self):
        self.driver.get(self.url)
        self.ClickWelcomeButton()
        for cookie in self.cookies.split(';'):
            name, value = cookie.strip().split('=', 1)
            self.driver.add_cookie({'name': name, 'value': value})
        print("Add cookies finished")
        
    def AccountLogin(self):
        try:
            # find class=<div id="inn-sign__login-btn__container" class="inn-sign__login-btn__container"><a class="inn-sign__login-btn">登录</a></div>
            loginButton = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inn-sign__login-btn"))
            ).click()
        except WebDriverException:
            print("login button lost")
        try:
            # find <input type="email" name="email" class="poi-form__control" placeholder="您的邮箱" title="您的邮箱" required="" tabindex="1" minlength="5" value="" data-gtm-form-interact-field-id="0">
            emailInput = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
            )
            emailInput.send_keys(self.account)
        except WebDriverException:
            print("email input lost")
        try:
            # find <input name="pwd" type="password" class="poi-form__control pwd" placeholder="密码" title="密码" required="" tabindex="1" value="" data-gtm-form-interact-field-id="1">
            passwordInput = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//input[@name="pwd"]'))  
            )
            passwordInput.send_keys(self.password)
        except WebDriverException:
            print("password input lost")
        try:
            # find <button type="submit" class="poi-dialog__footer__btn poi-dialog__footer__btn_success" tabindex="1"><span class="poi-icon fa-arrow-alt-circle-right fas fa-fw" aria-hidden="true"></span> <span class="poi-icon__text">登录</span></button>
            loginButton = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
            )
            loginButton.click()
        except WebDriverException:
            print("login button lost")

    def CheckLogin(self):
        self.driver.get(self.url)
        self.ClickWelcomeButton()
        try:
            # find <div class="inn-user-menu__nav__avatar-btn"><a class="inn-user-menu__nav__avatar-btn__link"><img class="inn-user-menu__nav__avatar-btn__img inn-avatar__img" src="https://cravatar.cn/avatar/8a81a26892c7552fd346025ef9d836dd?s=96&amp;r=g" width="50" height="50" alt="十六夜清酒"></a><div class="inn-user-menu__nav"><div class="inn-user-menu__nav__portal"><a title="钻石" class="inn-user-menu__nav__portal__item" href="https://steamzg.com/author/110200/"><span class="poi-icon fa-gem fas fa-fw" aria-hidden="true"></span> <span class="poi-icon__text">钻石: 5,818</span></a></div><div class="inn-user-menu__nav__item__container"><div class="inn-user-menu__nav__item"><div class="inn-user-menu__nav__item__title"><div class="inn-user-menu__nav__item__title__icon"><span class="poi-icon fa-paint-brush fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__title__text">文章管理</div></div><a href="https://steamzg.com/account/posts/" title="我的作品" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-thumbtack fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">我的作品</div></a><a href="https://steamzg.com/author/110200/fav/" title="收藏夹" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-heart fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">收藏夹</div></a><a href="https://steamzg.com/account/comments/" title="我的评论" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-comments fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">我的评论</div></a></div><div class="inn-user-menu__nav__item"><div class="inn-user-menu__nav__item__title"><div class="inn-user-menu__nav__item__title__icon"><span class="poi-icon fa-bell fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__title__text">消息管理</div></div><a href="https://steamzg.com/account/histories/" title="积分历史" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-history fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">积分历史</div></a><a href="https://steamzg.com/account/noti/" title="我的提醒" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-bell fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">我的提醒</div></a><a href="https://steamzg.com/account/pm/" title="站内信" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-envelope fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">站内信</div></a></div><div class="inn-user-menu__nav__item"><div class="inn-user-menu__nav__item__title"><div class="inn-user-menu__nav__item__title__icon"><span class="poi-icon fa-circle-notch fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__title__text">我的圈子</div></div><a href="https://steamzg.com/home/" title="我的首页" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-circle-notch fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">我的首页</div></a><a href="https://steamzg.com/account/followers/" title="我关注的人" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-users fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">我关注的人</div></a><a href="https://steamzg.com/account/fans/" title="我的粉丝" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-users fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">我的粉丝</div></a></div><div class="inn-user-menu__nav__item"><div class="inn-user-menu__nav__item__title"><div class="inn-user-menu__nav__item__title__icon"><span class="poi-icon fa-gamepad fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__title__text">游戏中心</div></div><a href="https://steamzg.com/account/bomb/" title="炸弹游戏" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-bomb fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">炸弹游戏</div></a><a href="https://steamzg.com/account/medal/" title="勋章中心" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-bookmark fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">勋章中心</div></a><a href="https://steamzg.com/account/avatar-box/" title="头像框中心" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-user-circle fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">头像框中心</div></a><a href="https://steamzg.com/account/lottery/" title="抽奖" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-gift fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">抽奖</div></a></div><div class="inn-user-menu__nav__item"><div class="inn-user-menu__nav__item__title"><div class="inn-user-menu__nav__item__title__icon"><span class="poi-icon fa-address-card fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__title__text">个人设置</div></div><a href="https://steamzg.com/author/110200/" title="我的概述" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-address-card fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">我的概述</div></a><a href="https://steamzg.com/account/settings/" title="我的设置" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-cog fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">我的设置</div></a><a href="https://steamzg.com/wp-admin/admin-ajax.php?action=d93cdf81145ea7f862f1c848075e9fc9&amp;redirectUrl=https%3A%2F%2Fsteamzg.com%2F" title="登出" class="inn-user-menu__nav__item__link"><div class="inn-user-menu__nav__item__link__icon"><span class="poi-icon fa-power-off fas fa-fw" aria-hidden="true"></span></div><div class="inn-user-menu__nav__item__link__text">登出</div></a></div></div></div></div>
            userMenu = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inn-user-menu__nav__avatar-btn"))
            )
            return True
        except WebDriverException:
            return False
        # try:
        #     # find class=<div id="inn-sign__login-btn__container" class="inn-sign__login-btn__container"><a class="inn-sign__login-btn">登录</a></div>
        #     loginButton = WebDriverWait(self.driver, self.timeout).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "inn-sign__login-btn"))
        #     )
        #     if loginButton.text == "登录":
        #         return False
        #     else:
        #         return True
        # except:
        #     print("login button lost")
        #     return False
        
    def Login(self):
        self.AddCookies()
        isLogin = self.CheckLogin()
        if not isLogin:
            self.AccountLogin()
            time.sleep(1)
        isLogin = self.CheckLogin()
        if not isLogin:
            print("Login failed")
            exit()
        print("Login finished")
        self.SaveCookies()
    
    def SaveCookies(self):
        cookies = self.driver.get_cookies()
        cookies = [cookie['name'] + "=" + cookie['value'] for cookie in cookies]
        cookies = "; ".join(cookies)
        # open("cookies.txt", "w").write(cookies)
        # print("Save cookies finished")
        # write cookies to github secret

    def ClickWelcomeButton(self):
        try:
            # find class="poi-dialog__footer__btn poi-dialog__footer__btn_default"
            welcomeButton = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, "poi-dialog__footer__btn_default"))
            )
            welcomeButton.click()
        except WebDriverException:
            print("welcome button lost")

    def AutoCheckIn(self):
        # "签到"
        self.driver.get(self.checkInUrl)
        checked = True
        try:
            checkIn = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//span[@class="poi-icon__text" and text()="签到"]/ancestor::a[@class="poi-tooltip is-bottom inn-nav__point-sign-daily__btn"]'))
            )
            checked = False
        except WebDriverException:
            print("checkIn button lost")
        if not checked:
            checkIn.click()
        print("CheckIn finished")
        # "白送模式"
        while True:
            self.driver.get(self.checkInUrl)
            freeModeSelect = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//h3[contains(text(), "白送模式")]/..'))
            )
            freeModeSelect.click()
            goButton = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//span[@class="poi-icon__text" and text()="GO"]'))
            )
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            goButton.click()
            # Check if the times reach the limit
            reachLimit = True
            alrtMsg = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="poi-alert__msg"]'))
            )
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
            zeroRiskModeSelect = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//h3[contains(text(), "0风险白嫖抽奖")]/..'))
            )
            zeroRiskModeSelect.click()
            goButton = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//span[@class="poi-icon__text" and text()="GO"]'))
            )
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            goButton.click()
            # Check if the times reach the limit
            reachLimit = True
            alrtMsg = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="poi-alert__msg"]'))
            )
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
    try:
        account = os.getenv("account")
        password = os.getenv("password")
        cookies = os.getenv("cookies")
    except:
        pass

    if cookies == None:
        cookies = open("cookies.txt", "r").read()
    if cookies == None:
        print("cookies not found")
    if account == None or password == None:
        accountMessage = open("account.txt", "r").read()
        # find account by "acoount: "
        account = accountMessage.split("account: ")[1].split("\n")[0]
        # find password by "password: "
        password = accountMessage.split("password: ")[1].split("\n")[0]
    if account == None or password == None:
        print("account or password not found")
        exit()
    autoCheckIn = SteamzgAutoCheckIn(cookies = cookies, account = account, password = password)
    autoCheckIn.Initdriver()
    autoCheckIn.Login()
    autoCheckIn.AutoCheckIn()
    print("Auto CheckIn finished")
    # input("press any key to exit")