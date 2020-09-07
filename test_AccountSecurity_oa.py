#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 17:59
# @Author  : Colorful.Jiang
import time
from TestCase.test_loginpage import login
from selenium.webdriver.common.keys import Keys

def test_account_ChangePassword():# 买家中心-账号安全--修改密码--取消
    wb = login()
    wb.wait(1)
    # 点击买家中心
    wb.getElement("xpath", "//*[text()='买家中心']").click()
    # 点击我的关注
    wb.wait(1)
    wb.getElement("xpath", "//*[text()='我的关注']").click()
    wb.wait(1)
    # 点击账号安全
    wb.getElement("xpath", "//*[text()='账号安全']").click()
    wb.wait(2)
    # 点击修改密码
    wb.getElement("xpath", "//*[text()='修改密码']").click()
    wb.wait(2)
    # 输入当前密码
    wb.getElement("xpath", "//*[@id='b2bShopApp']/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/section[2]/div/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div[2]/div/input").send_keys("123@qq")
    # 输入登录密码
    wb.getElement("xpath",
                  "//*[@id='b2bShopApp']/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/section[2]/div/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div/input").send_keys(
        "123@qqq")
    wb.wait(2)
    # 输入确认密码
    wb.getElement("xpath",
                  "//*[@id='b2bShopApp']/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/section[2]/div/div/div[3]/div/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/input").send_keys(
        "123@qqq")
    wb.wait(2)
    # 点击【取消】
    time.sleep(3)

    wb.getElement("xpath", "/html/body/div[20]/div[3]/button[2]").click()
    wb.wait(2)
    wb.driver.close()

def test_account_Unbund_phone():# 买家中心-账号安全--手机号解绑-取消
    wb = login()
    wb.wait(1)
    # 点击买家中心
    wb.getElement("xpath", "//*[text()='买家中心']").click()
    # 点击我的关注
    wb.wait(1)
    wb.getElement("xpath", "//*[text()='我的关注']").click()
    wb.wait(1)
    # 点击账号安全
    time.sleep(2)
    wb.getElement("xpath", "//*[text()='账号安全']").click()
    wb.wait(2)
    # 点击手机号解绑
    wb.getElement("xpath", "//*[@id='b2bShopApp']/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/section[3]/div/div[3]/div[2]/div[4]/span[1]").click()

    wb.wait(2)
    # 点击【取消】

    js = "var q=document.documentElement.scrollTop=500"
    wb.ExcuteJs(js)
    time.sleep(2)
    print("ready click cancel")
    wb.wait_element(["xpath","/html/body/div[21]/div[3]/button[2]"])
    #wb.getElement("xpath", "/html/body/div[33]/div[3]/button[2]").click()
    wb.ExcuteJs("document.querySelector('body > div:nth-child(33) > div.v-popconfirm__ft > button.v-popconfirm__button.v-popconfirm__button--cancel.v-button.v-button--default.v-button--medium').click()")

    wb.wait(2)
    wb.driver.close()
#
# def test_account_Unbund_wechat():# 买家中心-账号安全--微信号解绑-取消
#     wb = login()
#     wb.wait(1)
#     # 点击买家中心
#     wb.getElement("xpath", "//*[text()='买家中心']").click()
#     # 点击我的关注
#     wb.wait(1)
#     wb.getElement("xpath", "//*[text()='我的关注']").click()
#     wb.wait(1)
#     # 点击账号安全
#     wb.getElement("xpath", "//*[text()='账号安全']").click()
#     wb.wait(2)
#     # 点击微信号解绑
#     wb.getElement("xpath", "//*[@id='b2bShopApp']/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/section[3]/div/div[1]/div[2]/div[3]/span[1]").click()
#     wb.wait(2)
#     # 点击【取消】
#
#     wb.getElement("xpath", "/html/body/div[19]/div[3]/button[2]/span").click()
#     wb.wait(2)
#     wb.driver.close()


