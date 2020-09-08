import pytest
from selenium import webdriver
import time

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestCase.pageUtils import *


def login():
    url = "https://blink.qq.com/b2bshop/index/industrySites/174133321650266123"
    login_name = "testSeller03"
    login_password = "123@qq"
    wb = webutils(browser='chrome')
    wb.driver.get(url)
    wb.driver.maximize_window()
    time.sleep(5)
    # # 切换到iframe
    # wb.driver.switch_to_frame("_QD_INVITE_IFRAME_ID_PREFIX_2852150878")
    # wb.getElement("class", "btn-text").click()
    # wb.driver.switch_to.default_content()
    # wb.ExcuteJs(
    #     "document.getElementsByClassName(\"sign-btn primary__color primary__link-hover sign-in cursor-pointer\")[0].click()")
    # 点击登录按钮
    wb.getElement("xpath", "//a[@class='sign-btn primary__color primary__link-hover sign-in cursor-pointer']").click()

    # 切换到登录框
    wb.driver.switch_to_frame("SignIn-ZH_CN")
    wb.getElement("name", "username").send_keys(login_name)
    time.sleep(2)
    wb.getElement("name", "password").send_keys(login_password)
    wb.ExcuteJs("document.getElementsByClassName(\"v-button v-button--primary v-button--medium\")[0].click()")
    time.sleep(5)
    # wb.wait(10)
    print(123)
    wb.driver.switch_to_frame("tcaptcha_iframe")
    # # 定位滑块
    # block = wb.getElement("id", "tcaptcha_drag_thumb")
    # action = ActionChains(wb.driver)
    # action.click_and_hold(block).move_by_offset(210, 0).release().perform()
    # wb.driver.switch_to.default_content()
    # time.sleep(6)

    # 定位滑块
    status = '请控制拼图块对齐缺口'
    while status == "请控制拼图块对齐缺口" or status == "Put the piece right into the slot":

        block = wb.getElement("id", "tcaptcha_drag_thumb")
        wb.getElement("xpath", "//*[@id='reload']/div").click()

        time.sleep(3)
        action = ActionChains(wb.driver)
        time.sleep(3)
        action.click_and_hold(block).move_by_offset(210, 0).release().perform()

        # status = wb.getElement("id", "statusSuccess")
        # time.sleep(2)
        try:
            WebDriverWait(wb, 5).until(EC.presence_of_all_elements_located(By.XPATH("//*[@id='tcaptcha_note']")))
            wb.wait_element(["xpath", "//*[@id='tcaptcha_note']"])
            status = wb.getElement("xpath", "//*[@id='tcaptcha_note']").text
        except:
            status = ''
        print(status)
        # if status == "请控制拼图块对齐缺口":
        #
        #     print("pass")

        # else:
        #     time.sleep(6)
        #     wb.getElement("xpath", "//*[@id='reload']/div").click()
        #     time.sleep(6)
        #     block = wb.getElement("id", "tcaptcha_drag_thumb")
        #     action = ActionChains(wb.driver)
        #     action.click_and_hold(block).move_by_offset(210, 0).release().perform()

    print("--testtestest--")
    wb.driver.switch_to.default_content()
    # close
    time.sleep(5)
    # wb.getElement("class","common-button__text")[2].click()

    try:
        wb.wait_element(["xpath", "//*[@id='b2bShopApp']/div[1]/div/footer/div[2]"])
        wb.getElement("xpath", "//*[@id='b2bShopApp']/div[1]/div/footer/div[2]").click()
    except:
        pass
    # assert login nane

    # get_login_name=wb.driver.find_element_by_xpath("//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[2]/div/div[1]/div/a").text
    # print(get_login_name)
    # assert get_login_name in login_name
    return wb


# def test_baseinfo():
#     wb = login()
#     # 点击基本资料
#     time.sleep(3)
#     wb.getElement("xpath", "//*[text()='testSeller03']").click()
#     time.sleep(1)
#     wb.getElement("xpath", "//*[text()='基础资料']").click()


#     time.sleep(3)
#     wb.driver.close()
#
#
# def test_account():
#     wb = login()
#     # 点击账户安全
#     time.sleep(1)
#     wb.getElement("xpath", "//*[text()='testSeller03']").click()
#     time.sleep(1)
#     wb.getElement("xpath", "//*[text()='账户安全']").click()
#     time.sleep(3)
#     # wb.ExcuteJs("document.querySelector(\"#b2bShopApp > div > div:nth-child(1) > div > div > div > div.user > div > div.tb-userinfo-list > ul > li:nth-child(2) > a\").click()")
#     wb.driver.close()

#
def test_logout():
    wb = login()
    time.sleep(1)
    wb.getElement("xpath", "//*[text()='testSeller03']").click()
    time.sleep(1)
    wb.getElement("xpath", "//*[text()='退出登录']").click()
    time.sleep(3)


if __name__ == '__main__':
    login()
