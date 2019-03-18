import unittest
from demo import RunMain

class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'https://coding.imooc.com/api/prelearn'
        data = {
            'token': '0e1f9768a6de44ad3f62f3f809241c36',
            'timestamp': '1551773496894',
            'uid': '1914562',
            'cid': '309',
            'secrect': '906108abe9d6dda2bf2a515f0301a017',
            'apiname': 'prelearn'
        }
        res = self.run.run_main(url,'GET',data).json()
        res = self.assertEqual(res['errorCode'], 1007, '测试失败')
        print(res)
        print('这是第一个case')

    def test_02(self):
        url = 'https://coding.imooc.com/api/prelearn'
        data = {
            'token': '0e1f9768a6de44ad3f62f3f809241c36',
            'timestamp': '1551773496894',
            'uid': '1914561',
            'cid': '309',
            'secrect': '906108abe9d6dda2bf2a515f0301a017',
            'apiname': 'prelearn'
        }
        res = self.run.run_main(url, 'POST', data).json()
        res = self.assertEqual(res['errorCode'],1007,'测试失败')
        print(res)
        print('这是第二个case')


if __name__ == '__main__':
    unittest.main()



