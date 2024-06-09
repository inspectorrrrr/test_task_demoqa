import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def setup():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
