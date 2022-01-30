from behave import *
from selenium import webdriver


@given(u'launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()



@when(u'open orangehrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'verify that logo present on the page')
def step_impl(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then(u'close the browser')
def step_impl(context):
    context.driver.close()
