#coding:utf-8
from appium import webdriver
import unittest,time

class ZQY(unittest.TestCase):
    def setUp(self):
        desired_caps={
            'platformName':'Android',
            'deviceName':'127.0.0.1:62001',
            'platformVersion':'4.4.2',
            'appPackage':'com.berchina.prod.fcloud',
            'appActivity':'com.berchina.prod.fcloud.ui.activity.SplashActivity',
            #实现中文输入
            'unicodeKeyboard':'True',
            'resetKeyboard':'True',
            'automationName':'uiautomator2'
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def jichu(self):
        driver=self.driver
        # 等主页面activity出现,30秒内
        driver.wait_activity(".base.ui.MainActivity", 20)
        id_text='resourceId("com.berchina.prod.fcloud:id/radioMy").text("我的")'
        driver.find_element_by_android_uiautomator(id_text).click()
        class_text='className("android.widget.TextView").text("基础数据")'
        driver.find_element_by_android_uiautomator(class_text).click()
        # driver.find_element_by_link_text("基础数据").click()
        id_text1='resourceId("com.berchina.prod.fcloud:id/txtMenuName").text("供应商管理")'
        driver.find_element_by_android_uiautomator(id_text1).click()
        time.sleep(3)

    #添加供应商信息
    def addGYS(self):
        #self.jichu()
        driver=self.driver
        driver.find_element_by_id("com.berchina.prod.fcloud:id/imbRight").click()
        driver.implicitly_wait(10)
        id_text2='resourceId("com.berchina.prod.fcloud:id/edtPersonCharge").text("请输入联系人")'
        driver.find_element_by_android_uiautomator(id_text2).send_keys(u"赵六")
        id_text3='resourceId("com.berchina.prod.fcloud:id/edtCustomerName").text("请输入公司")'
        driver.find_element_by_android_uiautomator(id_text3).send_keys(u"天地壹号有限公司")
        # driver.find_element_by_id("com.berchina.prod.fcloud:id/edtPhone").send_keys(u"13444252425")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtMobile").send_keys("13444252425")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtMail").send_keys("12413434@qq.com")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtFax").send_keys("1233432")
        id_text4='resourceId("com.berchina.prod.fcloud:id/edtBankName").text("请输入银行")'
        driver.find_element_by_android_uiautomator(id_text4).send_keys(u"招商银行")
        id_text5='resourceId("com.berchina.prod.fcloud:id/edtBankPerson").text("请输入户名")'
        driver.find_element_by_android_uiautomator(id_text5).send_keys(u"赵六")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtBankNumber").send_keys("1234444433333455676")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/txtProvince").click()
        driver.swipe(113,1090,113,1057,500)
        driver.swipe(350,1090,350,1057,500)
        driver.swipe(600,1090,600,1057,500)
        driver.find_element_by_id("com.berchina.prod.fcloud:id/btn_confirm").click()
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtAddress").send_keys(u"银环路尹新华苑202")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtRemark").send_keys(u"这是备注")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/btnRight").click()
        time.sleep(3)

    #修改供应商信息
    def updGYS(self):
        #self.jichu()
        driver=self.driver
        driver.find_elements_by_id("com.berchina.prod.fcloud:id/txtCustomerName")[0].click()
        driver.find_element_by_id("com.berchina.prod.fcloud:id/imbRight").click()
        # 定位到悬浮层/弹出层里的修改功能位置，并点击
        driver.swipe(550,120,560,130,500)
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtPersonCharge").clear()
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtPersonCharge").send_keys(u"钱七")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtCustomerName").clear()
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtCustomerName").send_keys(u"清风原木有限公司")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtMobile").clear()
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtMobile").send_keys("18744252425")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtAddress").clear()
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtAddress").send_keys(u"科院北环立交金正大厦'1202'号")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtRemark").clear()
        driver.find_element_by_id("com.berchina.prod.fcloud:id/edtRemark").send_keys(u"这是修改后的备注")
        driver.find_element_by_id("com.berchina.prod.fcloud:id/btnRight").click()
        time.sleep(3)

    #删除供应商信息
    def test_ZQY_dele(self):
        self.jichu()
        self.addGYS()
        self.updGYS()
        driver=self.driver
        driver.find_elements_by_id("com.berchina.prod.fcloud:id/txtCustomerName")[0].click()
        time.sleep(3)
        driver.find_element_by_id("com.berchina.prod.fcloud:id/imbRight").click()
        #定位到悬浮层/弹出层里的删除功能位置，并点击
        driver.swipe(550,190,560,195,500)
        #点击弹出框里的确定按钮
        driver.find_element_by_id("com.berchina.prod.fcloud:id/txtDialogConfirm").click()
        time.sleep(3)


    #进行清理工作
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()




