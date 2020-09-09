#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-04 12:02
# @Author  : Colorful.Jiang
import pytest
import time
# from tools.pageUtils import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestCase.pageUtils import *


def login():
    try:
        print("11111111111111")
        # url = "https://oablink.qq.com/b2bshop/index/industrySites/235676754772303872"
        # login_name = "colorful"
        # login_password = "123@qq"
        #
        # wb = webutils(browser='chrome')
      

        wb.driver.get(url)
        # wb.driver.delete_all_cookies()
        # time.sleep(2)
        # cookie = {"name":"_authI","value":"FL_zNH6UD8KUAkZF9ys2xDd5iwEdL6le6AA8kWvy-u8Px1YQLsI59vpfTuaeEoqsY3kfXz9852lWgInxd8YAb3XzIHcicV0mXTyNks7XBeWb-8PaEdnilb7IWS9H5yUAUiH3FmtifzRi-ATQnPR-MRG0y5M5LdKxUz8Ld24-y98uwQ6MP2slWcqUlljPB471FBpDEasTYwkrIP1ecuedE_jJ0BASMObS5LPdpBAV17Pn68HkNO_lYgDxRX4972UZkFSml9V3LHDtRhpCWf7RdJAcHyHTevh9mPZCxsCy8q1NBm-uy9WuFHxYuolKdKEat8sGJZ2EL1nMAzPmaWSO-FuPASUQLKq5mRfGNkaODWEhzHjFtJP3BFGxz290qMHNJywCp8e58WiYiHUPpzzbtKQAsD64cP7eGplgq-vmnHNaR0zkHCEhohHAt7ZdgMv75TE5l6Dql1IUB1ZDPSW_FnnQbSH97-bmkYDnZvml4UcBRc1QxZpd-iKok-BzlZKAL5LY_8E0sTE6s7JZGiq6jrkNiTdkAOa2rGiopjKguSVUQoaKOwKMwN0FKa-dvWse0_25orHnefCfdnveOnrqny4cT2ZXi-ewrTjfEwQFGaIz3uHWUN606DJcoQnuRK3utAKEI26HgXpMXwseSS-QTiY-lOGunGQG9KsCO3BY35vGDEipitWRtZhJPmQ_-TtEM_Af5TkN9Td4JZLuiKGY7Sia-1Ug3EMap-4HsjDtgcKthhKU2pAc60uk2ibJ3tjuuprGukjHgGUBXxOjDfxxKnhPvHbnvPiAKybHCY-bCvvG2QEBFEnHjg0IZx1KmLB60F__8_ImJ6GUoC1Nt_-r-QP44a3Lua34zBOeWXgnLYo2hZVGmOQckc_lR0w46_mA5C3tbJQU1v85ZsZI654TFiqAe7zC3AMWSzcV-e94KFwdZ2d9a4YyRrN0Pi75A21cI76"}
        # time.sleep(2)
        # wb.driver.add_cookie(cookie)
        # time.sleep(2)
        # wb.driver.get(url)
        wb.driver.maximize_window()
        # 切换到iframe
        # wb.driver.switch_to_frame("_QD_INVITE_IFRAME_ID_PREFIX_2852150878")
        # wb.getElement("class","btn-text").click()
        # wb.driver.switch_to.default_content()
        time.sleep(5)
        # 点击【请登录】
        # wb.ExcuteJs(
        #     "document.querySelector('#b2bShopApp > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div.user > div > a.sign-btn.primary__color.primary__link-hover.sign-in.cursor-pointer').click()")
        test = wb.isElementExist("//div[@class='no-auth']")
        if test == True:
            wb.getElement("xpath",
                          "//a[@class='sign-btn primary__color primary__link-hover sign-in cursor-pointer']").click()
            # wb.getElement("xpath", "//a[@class='sign-btn primary__color primary__link-hover sign-in cursor-pointer']").click()
            time.sleep(5)
            # 切换到登录框
            wb.driver.switch_to_frame("SignIn-ZH_CN")
            wb.wait_element(["name", "username"])
            wb.getElement("name", "username").send_keys(login_name)
            time.sleep(2)
            wb.wait_element(["name", "password"])
            wb.getElement("name", "password").send_keys(login_password)
            wb.wait_element(["xpath", "/html/body/div/section/form/div/div[4]/div/button"])
            # wb.ExcuteJs("document.getElementsByClassName(\"v-button v-button--primary v-button--medium\")[0].click()")
            wb.getElement("xpath", "/html/body/div/section/form/div/div[4]/div/button").click()
            time.sleep(5)
            wb.driver.switch_to_frame("tcaptcha_iframe")

        text1 = None
        # while status == "请控制拼图块对齐缺口" or status == "Put the piece right into the slot":
        while text1 == None:
            block = wb.getElement("id", "tcaptcha_drag_thumb")
            wb.getElement("xpath", "//*[@id='reload']/div").click()

            time.sleep(3)
            action = ActionChains(wb.driver)
            time.sleep(3)
            action.click_and_hold(block).move_by_offset(210, 0).release().perform()
            text1 = wb.find_element_check("//*[@id='statusSuccess']")
            print(text1)
            # # 定位滑块
            # status = '请控制拼图块对齐缺口'
            # while status == "请控制拼图块对齐缺口" or status == "Put the piece right into the slot":
            #
            #     block = wb.getElement("id", "tcaptcha_drag_thumb")
            #     wb.getElement("xpath", "//*[@id='reload']/div").click()
            #     time.sleep(3)
            #     action = ActionChains(wb.driver)
            #     time.sleep(3)
            #     action.click_and_hold(block).move_by_offset(210, 0).release().perform()
            #
            #     # status = wb.getElement("id", "statusSuccess")
            #     time.sleep(3)
            #     try:
            #         wb.wait_element(["xpath", "//*[@id='tcaptcha_note']"])
            #         status = wb.getElement("xpath", "//*[@id='tcaptcha_note']").text
            #     except:
            #         status = ''
            #     print(status)

            # 关闭专属推荐
        time.sleep(5)
        try:
            wb.wait_element(["xpath",
                             "//div[@class='common-button__box mpsi-button common-button__box--default primary__link-hover primary__border-hover']"])
            wb.getElement("xpath",
                          "//div[@class='common-button__box mpsi-button common-button__box--default primary__link-hover primary__border-hover']").click()
        except:
            pass

            # check_login(wb)
            # #关闭专属推荐
            # wb.getElement("xpath","//*[@id='b2bShopApp']/div[1]/div/footer/div[2]").click()
            # # wb.ExcuteJs("document.getElementsByClassName(\"common-button__box mpsi-button common-button__box--default primary__link-hover primary__border-hover\")[0].click()")
            # wb.wait(3)

            # # assert login nane
            # get_login_name = wb.driver.find_element_by_xpath(
            #     "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/a").text
            # print(get_login_name)
            # assert get_login_name in login_name
        #         return wb
        #     else:
        #         return wb
        # except:
        #     # print("异常原因%s" % msg)
        #     wb.get_screenshot()
        #     raise
    except:

        wb.get_screenshot()
        raise

    return wb


# def check_login(wb):
#     print("开始检查状态")
#     #检查登录状态
#     status=wb.isElementExist("message-status")
#     if status==True:
#         print("登录成功")
#         return wb
#     else:
#         test = wb.isElementExist("//div[@class='no-auth']")
#         if test ==True:
#             print("重新登录")
#             login()
#         else:
#             print("error-----message——status&no-auth")


def test_baseinfo():
    wb = login()
    try:
        baseinfo = "基础信息"
        businessName = "企业名称"

        # 点击基本资料
        # time.sleep(30)
        # 点击colorful

        time.sleep(5)
        p = wb.getElement("xpath", "//div[@class='tb-userinfo-list']/div[1]/a").text
        print("loglog_________________" + p)
        wb.getElement("xpath", "//div[@class='tb-userinfo-list']").click()
        # wb.wait_element(["xpath", "//*[text()='colorful']"])
        # wb.wait_element(["//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/a"])
        # wb.getElement("//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/a").click()
        time.sleep(3)
        # 点击基础资料
        wb.getElement("xpath", "//a[@href='https://oablink.qq.com/seller/memberself/index/view/1']").click()
        # wb.wait_element(["xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/ul/li[1]/a"])
        # wb.getElement("xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/ul/li[1]/a").click()
        # wb.getElement("xpath", "//*[text()='基础资料']").click()
        time.sleep(2)

        # # assert 基础信息title
        # get_baseinfo_title = wb.driver.find_element_by_xpath("//*[@id='b2bShopApp']/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/section[2]/h3").text
        # print(get_baseinfo_title)
        # assert get_baseinfo_title in baseinfo
        # # assert 企业名称
        # get_businessName = wb.driver.find_element_by_xpath(
        #     "//*[@id='b2bShopApp']/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/section[2]/div/div/div[3]/div/div[1]/label/div/div/span").text
        # print(get_businessName)
        # assert get_businessName in businessName

        wb.driver.close()
    except:
        wb.get_screenshot()
        raise


# def test_account():
#     wb = login()
#     try:
#
#         account = "账号安全"
#         # wb.wait_element(["xpath", "//*[text()='colorful']"])
#         # 点击colorful
#         time.sleep(5)
#         p = wb.getElement("xpath", "//div[@class='tb-userinfo-list']/div[1]/a").text
#         print("loglog_________________" + p)
#         wb.getElement("xpath", "//div[@class='tb-userinfo-list']").click()
#         # wb.ExcuteJs("document.querySelector('#b2bShopApp > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div.user > div > div.tb-userinfo-list > div').click()")
#         # wb.wait_element(["xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/a"])
#         # wb.getElement("xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/a").click()
#         time.sleep(3)
#         # 点击账户安全
#         wb.getElement("xpath", "//a[@href='https://oablink.qq.com/seller/userinfo/index/view']").click()
#         # wb.wait_element(["xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/ul/li[2]/a"])
#         # wb.getElement("xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/ul/li[2]/a").click()
#         # wb.getElement("xpath", "//*[text()='账户安全']").click()
#         # assert 账号安全
#         # get_account_title = wb.driver.find_element_by_xpath("").test
#         # print(get_account_title)
#         # assert get_account_title in account
#         # assert 账号绑定
#
#         time.sleep(2)
#         # wb.ExcuteJs("document.querySelector(\"#b2bShopApp > div > div:nth-child(1) > div > div > div > div.user > div > div.tb-userinfo-list > ul > li:nth-child(2) > a\").click()")
#         wb.driver.close()
#     except:
#         wb.get_screenshot()
#         raise
#
#
# def test_logout():
#     wb = login()
#     try:
#
#         logout_name = "请登录"
#         # 点击colorful
#         time.sleep(5)
#         p = wb.getElement("xpath", "//div[@class='tb-userinfo-list']/div[1]/a").text
#         print("loglog_________________" + p)
#         wb.getElement("xpath", "//div[@class='tb-userinfo-list']").click()
#         # wb.ExcuteJs(
#         #     "document.querySelector('#b2bShopApp > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div.user > div > div.tb-userinfo-list > div').click()")
#         # wb.wait_element(["xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/a"])
#         # wb.getElement("xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/a").click()
#         # wb.wait_element(["xpath", "//*[text()='colorful']"])
#         # wb.getElement("xpath", "//*[text()='colorful']").click()
#         # wb.getElement("xpath", "//*[text()='退出登录']").click()
#         time.sleep(3)
#         # 点击退出登录
#         wb.getElement("xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/ul/li[3]/a").click()
#         # wb.wait_element(["xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/ul/li[3]/a"])
#         # wb.getElement("xpath", "//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/ul/li[3]/a").click()
#         time.sleep(2)
#
#         # # assert logout
#         # get_logout_name = wb.driver.find_element_by_xpath("//*[@id='b2bShopApp']/div/div[1]/div/div/div/div[1]/div[2]/div/a[1]").text
#         # print(get_logout_name)
#         # assert get_logout_name in logout_name
#         wb.driver.close()
#     except:
#         wb.get_screenshot()
#         raise


if __name__ == '__main__':
    login()
    # pytest.main(['--html=report/report.html'])
