from time import sleep
from pages.form_page import FillFormPage



class TestFormPage:


    def test_form_fill(self, driver):
        fill_form = FillFormPage(driver, 'https://google.com')
        fill_form.open_page()
        sleep(60)
        fill_form.fill_student_registration_form()
        