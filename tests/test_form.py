from selene import browser, have
from selenium.webdriver.chrome.options import Options


def test_form(browser_window):
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Vasilisa')
    browser.element('#lastName').type('Pupkina')
    browser.element('#userEmail').type('vpupkina@gmail.com')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('88005553322')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('option[value="7"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="2007"]').click()
    browser.element('.react-datepicker__day--008').click()

    browser.element('#subjectsInput').type('Chemistry').press_enter()
    browser.element('label[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').send_keys('D:\pic.png')

    browser.element('#currentAddress').type('some address')

    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('tr').should(have.texts(
        'Label Values', 'Student Name Vasilisa Pupkina', 'Student Email vpupkina@gmail.com',
                    'Gender Female', 'Mobile 8800555332', 'Date of Birth 08 August,2007', 'Subjects Chemistry',
                    'Hobbies Music', 'Picture pic.png', 'Address some address', 'State and City NCR Delhi'))


