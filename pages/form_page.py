from selene.support.shared import browser
from selene import have, command
from locators.form_page_locators import FormPageLocators
import os


class FormPage:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_first_name(self, first_name):
        browser.element(FormPageLocators.FIRST_NAME).type(first_name)
        return self

    def fill_last_name(self, last_name):
        browser.element(FormPageLocators.LAST_NAME).type(last_name)
        return self

    def fill_email(self, email):
        browser.element(FormPageLocators.EMAIL).type(email)
        return self

    def select_gender(self, gender):
        browser.element(FormPageLocators.GENDER.format(gender=gender)).click()
        return self

    def fill_mobile(self, mobile):
        browser.element(FormPageLocators.MOBILE).type(mobile)
        return self

    def set_date_of_birth(self, day, month, year):
        browser.element(FormPageLocators.DATE_OF_BIRTH_INPUT).click()
        browser.element(FormPageLocators.DATE_OF_BIRTH_MONTH_SELECT).send_keys(month)
        browser.element(FormPageLocators.DATE_OF_BIRTH_YEAR_SELECT).send_keys(year)
        browser.element(FormPageLocators.DATE_OF_BIRTH_DAY.format(day=day)).click()
        return self

    def fill_subjects(self, subjects):
        for subject in subjects:
            browser.element(FormPageLocators.SUBJECTS_INPUT).type(subject).press_enter()
        return self

    def select_hobbies(self, hobbies):
        hobby_map = {
            "Sports": "1",
            "Reading": "2",
            "Music": "3"
        }
        for hobby in hobbies:
            browser.element(FormPageLocators.HOBBY.format(index=hobby_map[hobby])).click()
        return self

    def upload_picture(self, picture_path):
        absolute_path = os.path.abspath(picture_path)
        browser.element(FormPageLocators.UPLOAD_PICTURE).send_keys(absolute_path)
        return self

    def fill_current_address(self, address):
        browser.element(FormPageLocators.CURRENT_ADDRESS).type(address)
        return self

    def select_state_and_city(self, state, city):
        browser.element(FormPageLocators.STATE).click()
        browser.element(FormPageLocators.STATE_OPTION.format(
            index=["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"].index(state))).should(have.text(state)).click()
        browser.element(FormPageLocators.CITY).click()
        browser.element(FormPageLocators.CITY_OPTION.format(index=["Delhi", "Gurgaon", "Noida"].index(city))).should(
            have.text(city)).click()
        return self

    def submit(self):
        browser.element(FormPageLocators.SUBMIT).click()
        return self
