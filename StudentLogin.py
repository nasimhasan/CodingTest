import unittest
from selenium import webdriver


class StudentExam(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path='D:\geckodriver\geckodriver.exe')
        cls.driver.get("https://lms.celt.vip/login")
        cls.driver.maximize_window()

    def test_1(self):
        self.driver.find_element_by_xpath('//*[@id="example-input-1"]').send_keys('student_qa_01@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="example-input-2"]').send_keys(12345678)
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div/div/form/div[5]/button").click()

    def test_2(self):
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[1]/div[2]/div/div/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[6]/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[3]/td[4]/a').click()
        self.driver.set_page_load_timeout(10)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__== '__main__':
    unittest.main(verbosity=2)