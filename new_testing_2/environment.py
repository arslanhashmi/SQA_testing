from selenium import webdriver
from selenium.webdriver.support.ui import Select
import string
import random


class App:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def quit(self):
        self.driver.quit()

    def open_url(self,url):
        self.driver.get(url)

    def input_text(self,text,field_xpath):
        text = update_text(text)
        self.driver.find_element_by_xpath(field_xpath).clear()
        self.driver.find_element_by_xpath(field_xpath).send_keys(text)

    def input_text_to_readonly(self,text,field_name):
        text = update_text(text)
        self.driver.execute_script('document.getElementsByName("'+field_name+'")[0].removeAttribute("readonly")')
        self.driver.find_element_by_name(field_name).send_keys("/") # readonly fields can't be cleared before changing value, not sure why!
        self.driver.find_element_by_name(field_name).clear()
        self.driver.find_element_by_name(field_name).send_keys(text)

    def find_and_click(self,element_xpath):
        self.driver.find_element_by_xpath(element_xpath).click()

    def find_and_click_by_css(self,class_name, element_num):
        a=self.driver.find_elements_by_class_name(class_name)[element_num].find_element_by_tag_name("li").click()

    def get_anchor_from_element(self, class_name, anchor_number, list_num):
        a=self.driver.find_elements_by_class_name(class_name)[list_num].find_elements_by_tag_name("a")[anchor_number].click()

    def get_current_url(self):
        return self.driver.current_url

    def find_text(self, element_xpath):
        return self.driver.find_element_by_xpath(element_xpath).text

    def select_option_in_dropdown(self, option, drop_down_name):
        select = Select(self.driver.find_element_by_name(drop_down_name))
        select.select_by_visible_text(option)

def before_all(context):
    context.browser = App()


def after_all(context):
    context.browser.quit()

def update_text(text):
    text = (''.join([random.choice(string.ascii_letters + string.digits) for _ in
                     range(int(text.split(':')[1]))])) + '@gmail.com' if "RANDOM-STRING-EMAIL" in text else text
    text = ''.join([random.choice(string.ascii_letters + string.digits) for _ in
                    range(int(text.split(':')[1]))]) if "RANDOM-STRING" in text else text
    return text


