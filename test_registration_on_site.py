from selene.support.shared import browser
from selene import have, be
import pytest


@pytest.fixture
def browser_config():
    browser.config.browser_name = 'firefox'
    browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_register(browser_config):
    link = 'https://demoqa.com/automation-practice-form'
    browser.open(link)
    browser.element('[id=firstName]').type('Kirill')
    browser.element('[id=lastName]').type('Popov')
    browser.element('[id="userEmail"]').type('soladef290@aosod.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type('1234567891')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="0"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1993"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--002 react-datepicker__day--weekend"]').click()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('[id="currentAddress"]').type('Nizhny Novgorod')
    browser.element('button#submit').click()
    assert browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))


def test_register_negative(browser_config):
    link = 'https://demoqa.com/automation-practice-form'
    browser.open(link)
    browser.element('[id=firstName]').type('Kirill')
    browser.element('[id=lastName]').type('Popov')
    browser.element('[id="userEmail"]').type('soladef290@aosod.com')
    browser.element('[id="userNumber"]').type('1234567891')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="0"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1993"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--002 react-datepicker__day--weekend"]').click()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('[id="currentAddress"]').type('Nizhny Novgorod')
    assert browser.element('button#submit').should(be.clickable)
