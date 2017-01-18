#!/usr/bin/python
#!-*- coding:utf-8 -*-
__author__ = 'Administrator'

import unittest
import time
import sys
import os

from selenium import webdriver

#鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
#键盘事件
from selenium.webdriver.common.keys import  Keys
#超时等待
from selenium.webdriver.support.ui import WebDriverWait

#导入公共的类
from package import common
from package import user_info
from package import resource

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = 'http://w.test88.mianshui365.net'
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.maximize_window()
        driver.implicitly_wait(30)

        # dialog_x = driver.find_element_by_xpath(".//*[@id='msjpop']/div[1]/div[2]")
        # dialog_x.click()

        login = driver.find_element_by_xpath(".//*[@id='txt_user_login']")
        login.click()

        driver.implicitly_wait(15)
        driver.switch_to.frame('dialogIframe')

        login_name = driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[2]/input')
        login_name.clear()
        login_name.send_keys("cjz_test")

        login_pass = driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[4]/input')
        login_pass.clear()
        login_pass.send_keys('123456')

        #login_submit = common.findID(driver, "login-submit")
        login_submit = driver.find_element_by_xpath(".//*[@id='login-submit']")
        login_submit.click()

        #testText = common.findID(driver, "user_welcome").text
        testText = driver.find_element_by_xpath(".//*[@id='user_welcome']").text

        try:
            self.assertEqual(u'欢迎，cjz_test', testText)
        except AssertionError as e:
            self.verificationErrors.append(str(e))


    def tearDown(self):
        driver=self.driver
        driver.quit()
        self.assertEqual([],self.verificationErrors)


if __name__=='__main__':
    unittest.main()