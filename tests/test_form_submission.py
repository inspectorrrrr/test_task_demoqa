import pytest
from pages.form_page import FormPage
from pages.result_page import ResultPage
from data.test_data import test_data


def test_form_submission():
    form_page = FormPage().open()
    form_page.fill_first_name(test_data['first_name']) \
        .fill_last_name(test_data['last_name']) \
        .fill_email(test_data['email']) \
        .select_gender(test_data['gender']) \
        .fill_mobile(test_data['mobile']) \
        .set_date_of_birth(test_data['date_of_birth']['day'], test_data['date_of_birth']['month'],
                           test_data['date_of_birth']['year']) \
        .fill_subjects(test_data['subjects']) \
        .select_hobbies(test_data['hobbies']) \
        .upload_picture(test_data['picture']) \
        .fill_current_address(test_data['current_address']) \
        .select_state_and_city(test_data['state'], test_data['city']) \
        .submit()

    result_page = ResultPage()
    result_page.should_have_text(test_data['first_name']) \
        .should_have_text(test_data['last_name']) \
        .should_have_text(test_data['email']) \
        .should_have_text(test_data['gender']) \
        .should_have_text(test_data['mobile']) \
        .should_have_text(test_data['date_of_birth']['day']) \
        .should_have_text(test_data['date_of_birth']['month']) \
        .should_have_text(test_data['date_of_birth']['year']) \
        .should_have_text(test_data['subjects'][0]) \
        .should_have_hobbies(test_data['hobbies']) \
        .should_have_text(test_data['current_address']) \
        .should_have_text(test_data['state']) \
        .should_have_text(test_data['city']) \
        .close()
