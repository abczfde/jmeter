#coding:utf-8
import unittest
import HTMLTestRunnerChinese
import zqy

testunit=unittest.TestSuite() #实例化测试套件
testunit.addTest(unittest.makeSuite(zqy.ZQY))   #将测试用例加入到测试套件中，zqy.ZQY，zqy指的是用例文件名称，ZQY指的是用例类（class）名
filename="D:\\Jekins\\workspace\\appium\\appiumPythonReport\\result.html"  #指定文件存放路径，以及要生成的报告文件名称
fp=open(filename,"wb")   #保存执行结果至文件
runner=HTMLTestRunnerChinese.HTMLTestRunner(stream=fp,title= u"测试报告",description=u"用例执行情况：")
runner.run(testunit)  #执行用例