import pytest
import time
from selenium import webdriver

class TestButton():

	def test_button_add_present_on_page(self, browser):
	    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	    browser.get(link)
	    time.sleep(3)
	    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
	    assert button, "The button is not displayed"

