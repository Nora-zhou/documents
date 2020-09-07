#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 15:01
# @Author  : Colorful.Jiang
import time
from TestCase.test_loginpage import login


def test_recommend_more():  # 专属推荐-查看更多-全选-取消全选
    wb = login()
    wb.wait(2)
    #点击专属推荐
    wb.getElement("xpath","//*[text()='专属推荐']").click()
    wb.wait(2)
    # 点击查看更多
    wb.getElement("xpath", "//*[text()='查看更多']").click()
    wb.wait(2)
    # 选择行业-全选
    time.sleep(3)
    # wb.getElement("xpath",
    #               "//*[@id='b2bShopApp']/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[4]/div/section/dl[1]/dd/span").click()
    wb.getElement("xpath", "//section/dl/dd/span").click()
    wb.wait(2)
    time.sleep(5)
    # 取消全选
    wb.getElement("xpath", "//section/dl/dd/span").click()
    # 点击取消
    # wb.getElement("xpath", "//*[text()='取消']").click()
    wb.wait(2)
    wb.driver.close()
#     # 点击生成专属推荐
#     wb.getElement("xpath", "//*[text()='生成专属推荐']").click()
#     wb.wait(2)
#     # 选择行业-取消全选
#     wb.getElement("xpath",
#                   "//*[@id='b2bShopApp']/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[4]/div/section/dl[1]/dd/span").click()
#     wb.wait(2)
#     # 点击生成专属推荐
#     wb.getElement("xpath", "//*[text()='生成专属推荐']").click()
#     wb.wait(2)
#     wb.driver.close()
#
# def test_recommend_follow():#专属推荐-关注-全选-取消全选
#     wb = login()
#     wb.wait(2)
#     # 点击专属推荐
#     wb.getElement("xpath","//*[text()='专属推荐']").click()
#     wb.wait(2)
#     # 点击关注
#     wb.getElement("xpath", "//*[@id='b2bShopApp']/div/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/span").click()
#     wb.wait(2)
#     # 选择行业-全选
#     wb.getElement("xpath",
#                   "//*[@id='b2bShopApp']/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[4]/div/section/dl[1]/dd/span").click()
#     wb.wait(2)
#     # 点击生成专属推荐
#     wb.getElement("xpath", "//*[text()='生成专属推荐']").click()
#     wb.wait(2)
#     # 选择行业-取消全选
#     wb.getElement("xpath",
#                   "//*[@id='b2bShopApp']/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[4]/div/section/dl[1]/dd/span").click()
#     wb.wait(2)
#     # 点击生成专属推荐
#     wb.getElement("xpath", "//*[text()='生成专属推荐']").click()
#     wb.wait(2)
#     wb.driver.close()
#
#
#
# def test_recommend():#专属推荐-全选-更新时间-默认-下一页-商品详情页-返回专属推荐-取消全选
#     wb = login()
#     wb.wait(2)
#     # 点击专属推荐
#     wb.getElement("xpath","//*[text()='专属推荐']").click()
#     # wb.getElement("xpath","//*[@id='b2bShopApp']/div/div[2]/div/div/div/div[5]/div/div[3]/span/a").click()
#     wb.wait(2)
#     # 点击查看更多
#     wb.getElement("xpath", "//*[text()='查看更多']").click()
#     # wb.getElement("xpath", "//*[@id='b2bShopApp']/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[3]").click()
#     wb.wait(2)
#     # 选择行业-全选
#     wb.getElement("xpath", "//*[@id='b2bShopApp']/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[4]/div/section/dl[1]/dd/span").click()
#     wb.wait(2)
#     # 点击生成专属推荐
#     wb.getElement("xpath", "//*[text()='生成专属推荐']").click()
#     wb.driver.close()
#
#     # wb.getElement("xpath","//*[@id='b2bShopApp']/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[4]/div/footer/div[1]/span").click()
#     wb.wait(2)
#     # 进入店铺
#     wb.getElement("xpath","//*[text()='BlackPink']").click()
#     wb.wait(2)
#     wb.SwitchWindow_Two()
#     wb.wait(2)
#     # 点击更新时间
#     wb.ExcuteJs("document.getElementsByClassName(\"component-sort-btn condition-label sort-btn-el primary__border-bottom\")[0].click()")
#     wb.wait(2)
#     # 点击默认
#     wb.getElement("xpath", "//*[text()='默认']").click()
#     wb.wait(2)
#     # 点击第二页
#     wb.getElement("xpath","//*[text()='2']").click()
#     wb.wait(2)
#     # 点击商品详情页
#     wb.getElement("xpath",
#                   "//*[text()='维达抽纸 7箱']").click()
#     wb.wait(2)
#     wb.SwitchWindow_Two()
#     # 返回专属推荐
#     wb.getElement("xpath",
#                   "//*[text()='专属推荐']").click()
#     wb.wait(2)
#     # 点击查看更多
#     wb.getElement("xpath",
#                   "//*[text()='查看更多']").click()
#     wb.wait(2)
#     # 选择行业-取消全选
#     wb.getElement("xpath",
#                   "//*[@id='b2bShopApp']/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[4]/div/section/dl[1]/dd/span").click()
#     wb.wait(2)
#     # 点击生成专属推荐
#     wb.getElement("xpath", "//*[text()='生成专属推荐']").click()
#     wb.wait(2)
#     wb.driver.close()
