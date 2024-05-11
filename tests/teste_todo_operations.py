from selene import browser


def test_complete_todo():

    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')

    browser.element('#firstName').type('Testova')
    browser.all(selector)
