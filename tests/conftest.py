from selene import browser, be, have
import pytest

@pytest.fixture()
def browser_window():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()