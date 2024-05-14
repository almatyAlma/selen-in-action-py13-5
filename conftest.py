import pytest



@pytest.fixture(scope='function', autouse=True)
def browser_managment():
        browser.config.base_url = 'https://demoqa.com/automation-practice-form'
        browser.config.window_height = 800
        browser.config.window_width = 1200
        yield
        browser.quit()