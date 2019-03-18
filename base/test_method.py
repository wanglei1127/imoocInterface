#coding=utf-8
import unittest
from base.demo0314 import RunMain
import HTMLTestRunner

class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'https://coding.m.imooc.com/api/courselist'
        data = {
            'page': 2
        }
        res = self.run.run_main(url,'GET',data)
        print(res)

    # @unittest.skip('test_02')
    def test_02(self):
        url = 'https://coding.m.imooc.com/api/courselist'
        data = {
            'page': 1
        }
        res = self.run.run_main(url, 'GET', data)
        print(res)

if __name__ == '__main__':
    filename = '../report/htmlreport.html'
    fp = open(filename,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='My test',description='This is a test')
    runner.run(suite)

