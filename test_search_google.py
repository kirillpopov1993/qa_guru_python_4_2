from selene.support.shared import browser
from selene import have, be
import pytest


@pytest.fixture
def browser_config():
    browser.config.browser_name = 'firefox'
    browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_search_positive(browser_config):
    link = 'https://www.google.com/'
    browser.open(link)
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_negative(browser_config):
    link = 'https://www.google.com/'
    browser.open(link)
    browser.element('[name="q"]').should(be.blank).type('dfdsgshfdhfdhdgfhfdhfdhdh').press_enter()
    browser.element('.card-section').should(have.text('По запросу dfdsgshfdhfdhdgfhfdhfdhdh ничего не найдено. '))
