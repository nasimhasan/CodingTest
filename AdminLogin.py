import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class DemoExam(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path='D:\geckodriver\geckodriver.exe')
        cls.driver.get("https://lms.celt.vip/login")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_A(self):
        self.driver.find_element_by_xpath("//input[@id='example-input-1']").send_keys('elgunulu@gmail.com')
        self.driver.find_element_by_xpath("//input[@id='example-input-2']").send_keys(12345678)
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div/div/form/div[5]/button").click()
        time.sleep(5)

    def test_B(self):
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[13]/a[1]/span[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[@href='/super-admin/exams/701/edit']//button[@type='button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[@class='v-tab']").click()
        self.driver.find_element_by_xpath("//div[@class='d-flex flex-row-reverse']//button[@type='button']//span[@class='v-btn__content']//i[@class='v-icon notranslate mdi mdi-plus theme--dark']").click()
        self.driver.find_element_by_xpath("//div[@class='col-sm-12 col-md-12 col-12']//div[@class='form-group']//div[@class='v-input theme--light v-text-field v-text-field--single-line v-text-field--solo v-text-field--is-booted v-text-field--enclosed']//div[@class='v-input__control']//div[@class='v-input__slot']").send_keys("Test Parent Question")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]").send_keys("Description")
        self.driver.find_element_by_xpath("//div[@class='v-input v-input--is-focused theme--light v-text-field v-text-field--single-line v-text-field--solo v-text-field--is-booted v-text-field--enclosed v-select v-select--is-menu-active v-autocomplete primary--text']//div[@class='v-input__control']//div[@class='v-input__slot']").send_keys("Parent")
        self.driver.find_element_by_id("//div[@class='col-sm-12 col-md-6 col-12']//div[@class='form-group']//div[@class='v-input theme--light v-text-field v-text-field--single-line v-text-field--solo v-text-field--is-booted v-text-field--enclosed']//div[@class='v-input__control']//div[@class='v-input__slot']").send_keys(1)
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]").click()
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[5]/div[2]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/p[1]/div[1]/button[1]/span[1]/i[1]").click()
        self.driver.find_element_by_id('input-5594').send_keys(
            "Test child Question")
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]").send_keys("Description")
        self.driver.find_element_by_id('input-5601').send_keys('Single choice')

        self.driver.find_element_by_id("input-5607").send_keys(2)
        self.driver.find_element_by_id("input-5783").send_keys("Answer 1")
        self.driver.find_element_by_id("input-5783").send_keys("Answer 2")
        self.driver.find_element_by_id("input-5797").send_keys("Answer 3")
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[7]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/label[1]').click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/button[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[1]/div[2]/div/div/ul/li[6]/a/span').click()
        self.driver.find_element_by_id("input-3372").send_keys("student_qa_01@gmail.com")
        self.driver.set_page_load_timeout(5)
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr/td[6]/div/button[1]/span/i").click()
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/a[5]").click()
        self.driver.find_element_by_xpath("//input[@id='input-6129']").click()
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
        self.driver.set_page_load_timeout(5)
        self.driver.find_element_by_xpath("//input[@id='input-6135']").click()
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]").click()
        self.driver.set_page_load_timeout(10)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[6]/td[3]/div[1]/button[1]/span[1]/i[1]').click()
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]').click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__== '__main__':
    unittest.main(verbosity=2)







