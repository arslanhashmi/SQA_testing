from behave import given, then, when
from time import sleep

@given('I have to open "{url}"')
def i_have_a_new_item(context, url):
    context.browser.open_url(url)

@when('I find and click on "{button}" button')
def click_to_the_button(context, button):
    context.browser.find_and_click(button)

@given('I find and click on "{button}" button')
def click_to_the_button(context, button):
    context.browser.find_and_click(button)

@given('I find and click on "{button}" button "{element_num}" in class list')
def click_to_the_button(context, button, element_num):
    context.browser.find_and_click_by_css(button, int(element_num))

@when('I find and click on "{button}" anchor "{anchor_num}" in "{list_num}" number search by class')
def click_to_the_button(context, button, anchor_num, list_num):
    context.browser.get_anchor_from_element(button, int(anchor_num), int(list_num))

@given('I assert "{url}" page should be opened')
def getting_a_message (context, url):
    assert url == context.browser.get_current_url()

@when('I enter "{text}" in "{field}" field')
def enter_text(context, text, field):
    context.browser.input_text(text, field)

@when('I enter "{text}" in "{field}" readonly field')
def enter_text(context, text, field):
    context.browser.input_text_to_readonly(text, field)

@then('I wait for "{time}" sec')
def go_to_sleep(context, time):
    sleep(int(time))

@then('I assert "{text}" is here in "{path}"')
def check_text(context, text, path):
    found_text = context.browser.find_text(path)
    assert text in found_text

@when('I select "{option}" in "{dropdown}" dropdown')
def select_option_in_dropdown(context, option, dropdown):
    context.browser.select_option_in_dropdown(option, dropdown)

@then('I assert "{url}" page should be opened')
def getting_a_message (context, url):
    print(context.browser.get_current_url())
    assert url == context.browser.get_current_url()









