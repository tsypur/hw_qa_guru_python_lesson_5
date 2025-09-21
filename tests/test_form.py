from selene import browser, have
from selenium.webdriver.chrome.options import Options


def test_form():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    browser.config.driver_options = options
    #browser.config.timeout = 15

    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Vasya')
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

    # browser.element('#uploadPicture').click() хз как

    browser.element('#currentAddress').type('some address')

    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('tr').should(have.texts(
        'Student Name', 'Vasilisa Pupkina',
        'Student Email', 'vpupkina@gmail.com',
        'Gender', 'Female',
        'Mobile', '88005553322',
        'Date of Birth', '08 August,2007',
        'Subjects', 'Chemistry',
        'Hobbies', 'Music',
        'Picture', '',
        'Address', 'some address',
        'State and City', 'NCR Delhi'
    ))